# QR Attendance System — Week 1 Setup

## What this Week 1 code does
- Runs a basic Flask web server
- Connects to an SQLite database and shows sample student records
- Generates a test QR code and displays it in the browser

This confirms your entire toolchain (Flask + SQLite + qrcode library) works before you add the harder logic in Week 2 (token rotation).

## Folder structure
```
qr_attendance/
├── app.py              # Main Flask application
├── init_db.py          # Run once to create the database
├── schema.sql          # Database table definitions
├── requirements.txt    # Python dependencies
├── templates/
│   ├── home.html
│   └── students.html
└── static/
    └── style.css
```

## Setup steps (run these on your own laptop)

1. **Install Python** (3.9+) if you don't have it already: https://www.python.org/downloads/

2. **Open a terminal in the `qr_attendance` folder** and create a virtual environment (recommended, keeps things clean):
   ```
   python -m venv venv
   ```
   Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install the dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Initialize the database** (creates `attendance.db` with sample students):
   ```
   python init_db.py
   ```
   You should see: `Database initialized successfully as attendance.db`

5. **Run the app:**
   ```
   python app.py
   ```
   You should see something like:
   ```
   * Running on http://127.0.0.1:5000
   ```

6. **Open your browser** and go to `http://127.0.0.1:5000`

   - Click "View sample students" → should show a table of 3 students pulled from the database
   - Click "View a test QR code" → should show a scannable QR code (try scanning it with your phone's camera, it'll just show the test text)

## Troubleshooting

- **"ModuleNotFoundError: No module named 'flask'"** → your virtual environment isn't activated, or the install step failed. Re-run step 2 and 3.
- **"sqlite3.OperationalError: no such table"** → you skipped `python init_db.py`. Run it before starting the app.
- **Port 5000 already in use** → close other running Flask apps, or change the last line in `app.py` to `app.run(debug=True, port=5001)`.

## Week 1 checkpoint (what "done" looks like)
- [ ] App runs without errors
- [ ] `/students` page shows 3 sample students from the database
- [ ] `/test_qr` page shows a working QR code

Once all three are working, you're ready for Week 2: making the QR code auto-generate a new token every few seconds instead of showing fixed text.
