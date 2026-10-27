"""
Full app with subject-wise attendance:
- Faculty logs in, picks a subject, starts a session -> live QR tied to that subject
- Students scan to mark attendance for whichever subject session is currently live
- Student portal shows a subject-wise attendance table (held / attended / %)
"""
from flask import Flask, render_template, send_file, jsonify, request, session, redirect, url_for
import sqlite3
import qrcode
import io
import secrets
import datetime
import os
import joblib

app = Flask(__name__)
app.secret_key = 'change-this-secret-key-before-real-deployment'
DB_NAME = 'attendance.db'

TOKEN_VALID_SECONDS = 8

SUBJECTS = ["SNLP", "OS", "WIT", "OOAD", "ML", "OS Lab", "ML Lab", "CD", "Mini Project"]

RISK_MODEL_PATH = 'risk_model.pkl'
risk_model = joblib.load(RISK_MODEL_PATH) if os.path.exists(RISK_MODEL_PATH) else None
EARLY_WINDOW = 15  # must match train_risk_model.py


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_new_token(session_id):
    token_value = secrets.token_urlsafe(16)
    now = datetime.datetime.now()
    expires_at = now + datetime.timedelta(seconds=TOKEN_VALID_SECONDS)
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO tokens (session_id, token_value, created_at, expires_at) VALUES (?, ?, ?, ?)',
        (session_id, token_value, now.isoformat(), expires_at.isoformat())
    )
    conn.commit()
    conn.close()
    return token_value, now, expires_at


def get_current_token_info(session_id):
    """Returns (token, created_at, expires_at) for the given class session, rotating as needed."""
    conn = get_db_connection()
    latest = conn.execute(
        'SELECT * FROM tokens WHERE session_id = ? ORDER BY id DESC LIMIT 1', (session_id,)
    ).fetchone()
    conn.close()

    now = datetime.datetime.now()

    if latest is None:
        return create_new_token(session_id)

    expires_at = datetime.datetime.fromisoformat(latest['expires_at'])
    if now > expires_at:
        return create_new_token(session_id)
    else:
        created_at = datetime.datetime.fromisoformat(latest['created_at'])
        return latest['token_value'], created_at, expires_at


def find_session_for_valid_token(token_value):
    """Given a scanned/typed token, find which class session it belongs to, if it's still valid."""
    conn = get_db_connection()
    row = conn.execute(
        'SELECT * FROM tokens WHERE token_value = ? ORDER BY id DESC LIMIT 1', (token_value,)
    ).fetchone()
    conn.close()

    if row is None:
        return None

    expires_at = datetime.datetime.fromisoformat(row['expires_at'])
    if datetime.datetime.now() > expires_at:
        return None

    return row['session_id']


def get_student_risk(student_id):
    """
    Computes the same two features the model was trained on
    (early attendance %, and trend within that early window),
    using this student's REAL attendance history, then asks the
    trained model for a risk probability.

    Returns None if there isn't enough data yet, or if the model
    file is missing.
    """
    if risk_model is None:
        return None

    conn = get_db_connection()
    all_sessions = conn.execute(
        'SELECT id FROM sessions ORDER BY id ASC LIMIT ?', (EARLY_WINDOW,)
    ).fetchall()

    if len(all_sessions) < 4:  # need at least a few sessions to say anything meaningful
        conn.close()
        return None

    session_ids = [row['id'] for row in all_sessions]
    placeholders = ','.join('?' for _ in session_ids)

    attended_rows = conn.execute(
        f'SELECT session_id FROM attendance WHERE student_id = ? AND session_id IN ({placeholders})',
        [student_id] + session_ids
    ).fetchall()
    conn.close()

    attended_ids = set(row['session_id'] for row in attended_rows)
    record = [1 if sid in attended_ids else 0 for sid in session_ids]

    window = len(record)
    early_percentage = (sum(record) / window) * 100

    half = window // 2
    first_half = record[:half] or [0]
    second_half = record[half:] or [0]
    trend = ((sum(second_half) / len(second_half)) - (sum(first_half) / len(first_half))) * 100

    probability_at_risk = risk_model.predict_proba([[early_percentage, trend]])[0][1]

    if probability_at_risk >= 0.6:
        label = 'Critical'
    elif probability_at_risk >= 0.3:
        label = 'Watch'
    else:
        label = 'Safe'

    return {
        'probability': round(probability_at_risk * 100, 1),
        'label': label,
        'sessions_considered': window
    }


# ---------- Public / home ----------

@app.route('/')
def home():
    return render_template('home.html')


# ---------- Student auth ----------

@app.route('/signup', methods=['GET', 'POST'])
def student_signup():
    error = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        roll_number = request.form.get('roll_number', '').strip()
        password = request.form.get('password', '').strip()

        if not name or not roll_number or not password:
            error = 'Please fill in all fields.'
        else:
            conn = get_db_connection()
            existing = conn.execute(
                'SELECT * FROM students WHERE roll_number = ?', (roll_number,)
            ).fetchone()

            if existing:
                conn.close()
                error = 'That roll number is already registered. Try logging in instead.'
            else:
                conn.execute(
                    'INSERT INTO students (name, roll_number, password) VALUES (?, ?, ?)',
                    (name, roll_number, password)
                )
                conn.commit()
                conn.close()
                return redirect(url_for('student_login'))

    return render_template('signup.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def student_login():
    error = None
    if request.method == 'POST':
        roll_number = request.form.get('roll_number', '').strip()
        password = request.form.get('password', '').strip()

        conn = get_db_connection()
        student = conn.execute(
            'SELECT * FROM students WHERE roll_number = ?', (roll_number,)
        ).fetchone()
        conn.close()

        if student and student['password'] == password:
            session['student_id'] = student['id']
            session['student_name'] = student['name']
            session['student_roll'] = student['roll_number']
            return redirect(url_for('student_portal'))
        else:
            error = 'Incorrect roll number or password.'

    return render_template('login.html', error=error)


@app.route('/logout')
def student_logout():
    session.pop('student_id', None)
    session.pop('student_name', None)
    session.pop('student_roll', None)
    return redirect(url_for('home'))


@app.route('/portal')
def student_portal():
    if 'student_id' not in session:
        return redirect(url_for('student_login'))

    student_id = session['student_id']
    conn = get_db_connection()

    # Subject-wise breakdown: how many sessions held per subject vs how many this student attended
    subject_rows = []
    for subject in SUBJECTS:
        held = conn.execute(
            'SELECT COUNT(*) as c FROM sessions WHERE subject = ?', (subject,)
        ).fetchone()['c']

        attended = conn.execute('''
            SELECT COUNT(*) as c FROM attendance
            JOIN sessions ON sessions.id = attendance.session_id
            WHERE attendance.student_id = ? AND sessions.subject = ?
        ''', (student_id, subject)).fetchone()['c']

        pct = round((attended / held) * 100, 1) if held > 0 else None
        subject_rows.append({
            'subject': subject, 'held': held, 'attended': attended, 'percentage': pct
        })

    total_sessions = conn.execute('SELECT COUNT(*) as c FROM sessions').fetchone()['c']

    history = conn.execute('''
        SELECT sessions.subject, sessions.date, attendance.marked_at
        FROM attendance
        JOIN sessions ON sessions.id = attendance.session_id
        WHERE attendance.student_id = ?
        ORDER BY attendance.marked_at DESC
        LIMIT 20
    ''', (student_id,)).fetchall()
    conn.close()

    attended_count = len(history)
    overall_percentage = round((attended_count / total_sessions) * 100, 1) if total_sessions > 0 else 0
    last_attendance = history[0]['marked_at'] if history else None

    risk = get_student_risk(student_id)

    return render_template(
        'portal.html',
        name=session['student_name'],
        roll=session['student_roll'],
        subject_rows=subject_rows,
        total_sessions=total_sessions,
        attended_count=attended_count,
        overall_percentage=overall_percentage,
        last_attendance=last_attendance,
        history=history,
        refresh_seconds=TOKEN_VALID_SECONDS,
        risk=risk
    )


@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    if 'student_id' not in session:
        return jsonify({'success': False, 'message': 'Please log in first.'}), 401

    data = request.get_json()
    token = data.get('token', '').strip()

    if not token:
        return jsonify({'success': False, 'message': 'Missing code.'}), 400

    matched_session_id = find_session_for_valid_token(token)

    if matched_session_id is None:
        return jsonify({'success': False, 'message': 'This code has expired. Scan the current one.'}), 400

    student_id = session['student_id']
    conn = get_db_connection()

    class_session = conn.execute('SELECT * FROM sessions WHERE id = ?', (matched_session_id,)).fetchone()

    already_marked = conn.execute(
        'SELECT * FROM attendance WHERE session_id = ? AND student_id = ?',
        (matched_session_id, student_id)
    ).fetchone()

    if already_marked:
        conn.close()
        return jsonify({'success': False, 'message': f"You're already marked present for {class_session['subject']} today."}), 400

    now = datetime.datetime.now().isoformat()
    conn.execute(
        'INSERT INTO attendance (session_id, student_id, marked_at) VALUES (?, ?, ?)',
        (matched_session_id, student_id, now)
    )
    conn.commit()
    conn.close()

    return jsonify({'success': True, 'message': f"Attendance marked for {class_session['subject']}!"})


# ---------- Faculty / admin auth ----------

@app.route('/admin/signup', methods=['GET', 'POST'])
def admin_signup():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            error = 'Please fill in all fields.'
        else:
            conn = get_db_connection()
            existing = conn.execute(
                'SELECT * FROM admins WHERE username = ?', (username,)
            ).fetchone()

            if existing:
                conn.close()
                error = 'That username is already taken. Try logging in instead.'
            else:
                conn.execute(
                    'INSERT INTO admins (username, password) VALUES (?, ?)',
                    (username, password)
                )
                conn.commit()
                conn.close()
                return redirect(url_for('admin_login'))

    return render_template('admin_signup.html', error=error)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        conn = get_db_connection()
        admin = conn.execute(
            'SELECT * FROM admins WHERE username = ?', (username,)
        ).fetchone()
        conn.close()

        if admin and admin['password'] == password:
            session['is_admin'] = True
            session['admin_username'] = admin['username']
            return redirect(url_for('admin_dashboard'))
        else:
            error = 'Incorrect username or password.'

    return render_template('admin_login.html', error=error)


@app.route('/admin/logout')
def admin_logout():
    session.pop('is_admin', None)
    session.pop('admin_username', None)
    session.pop('active_session_id', None)
    session.pop('active_subject', None)
    return redirect(url_for('home'))


@app.route('/admin/start_session', methods=['GET', 'POST'])
def admin_start_session():
    if not session.get('is_admin'):
        return redirect(url_for('admin_login'))

    if request.method == 'POST':
        subject = request.form.get('subject', '').strip()
        if subject not in SUBJECTS:
            return render_template('admin_start_session.html', subjects=SUBJECTS, error='Please choose a valid subject.')

        conn = get_db_connection()
        cursor = conn.execute(
            'INSERT INTO sessions (subject, date, start_time, is_active) VALUES (?, ?, ?, 1)',
            (subject, str(datetime.date.today()), datetime.datetime.now().strftime('%H:%M'))
        )
        conn.commit()
        new_session_id = cursor.lastrowid
        conn.close()

        session['active_session_id'] = new_session_id
        session['active_subject'] = subject
        return redirect(url_for('admin_dashboard'))

    return render_template('admin_start_session.html', subjects=SUBJECTS, error=None)


@app.route('/admin/end_session')
def admin_end_session():
    if not session.get('is_admin'):
        return redirect(url_for('admin_login'))
    session.pop('active_session_id', None)
    session.pop('active_subject', None)
    return redirect(url_for('admin_start_session'))


@app.route('/admin/risk_report')
def admin_risk_report():
    if not session.get('is_admin'):
        return redirect(url_for('admin_login'))

    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students ORDER BY name').fetchall()
    conn.close()

    report_rows = []
    for student in students:
        risk = get_student_risk(student['id'])
        report_rows.append({
            'name': student['name'],
            'roll_number': student['roll_number'],
            'risk': risk
        })

    # Show highest-risk students first
    report_rows.sort(key=lambda r: r['risk']['probability'] if r['risk'] else -1, reverse=True)

    model_available = risk_model is not None

    return render_template('admin_risk_report.html', report_rows=report_rows, model_available=model_available)


@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('is_admin'):
        return redirect(url_for('admin_login'))
    if 'active_session_id' not in session:
        return redirect(url_for('admin_start_session'))
    return render_template(
        'admin_dashboard.html',
        refresh_seconds=TOKEN_VALID_SECONDS,
        subject=session.get('active_subject')
    )


@app.route('/current_qr')
def current_qr():
    if 'active_session_id' not in session:
        return 'No active session', 400
    token, _, _ = get_current_token_info(session['active_session_id'])
    img = qrcode.make(token)
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    return send_file(img_buffer, mimetype='image/png')


@app.route('/token_timing')
def token_timing():
    if 'active_session_id' not in session:
        return jsonify({'error': 'no active session'}), 400
    token, created_at, expires_at = get_current_token_info(session['active_session_id'])
    now = datetime.datetime.now()
    seconds_left = max(0, (expires_at - now).total_seconds())
    response = {'seconds_left': seconds_left, 'total_seconds': TOKEN_VALID_SECONDS}
    if session.get('is_admin'):
        response['token'] = token
    return jsonify(response)


@app.route('/attendance_data')
def attendance_data():
    if not session.get('is_admin') or 'active_session_id' not in session:
        return jsonify({'error': 'unauthorized'}), 401

    active_session_id = session['active_session_id']
    conn = get_db_connection()
    total_students = conn.execute('SELECT COUNT(*) as c FROM students').fetchone()['c']

    present_rows = conn.execute('''
        SELECT students.name, students.roll_number, attendance.marked_at
        FROM attendance
        JOIN students ON students.id = attendance.student_id
        WHERE attendance.session_id = ?
        ORDER BY attendance.marked_at DESC
    ''', (active_session_id,)).fetchall()
    conn.close()

    present_list = [
        {'name': row['name'], 'roll_number': row['roll_number'], 'marked_at': row['marked_at']}
        for row in present_rows
    ]

    return jsonify({
        'total_students': total_students,
        'present_count': len(present_list),
        'present_list': present_list
    })


if __name__ == '__main__':
    app.run(debug=True)
