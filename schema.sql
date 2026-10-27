-- Database schema for QR-Based Smart Attendance System

DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS tokens;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS admins;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_number TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    date TEXT NOT NULL,
    start_time TEXT NOT NULL,
    is_active INTEGER DEFAULT 1
);

CREATE TABLE tokens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    token_value TEXT NOT NULL,
    created_at TEXT NOT NULL,
    expires_at TEXT NOT NULL,
    FOREIGN KEY (session_id) REFERENCES sessions (id)
);

CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    marked_at TEXT NOT NULL,
    FOREIGN KEY (session_id) REFERENCES sessions (id),
    FOREIGN KEY (student_id) REFERENCES students (id)
);

-- Sample students. Password is same as roll number in lowercase, for easy testing.
-- e.g. roll number CS101 logs in with password cs101
INSERT INTO students (name, roll_number, password) VALUES ('Aarav Sharma', 'CS101', 'cs101');
INSERT INTO students (name, roll_number, password) VALUES ('Priya Reddy', 'CS102', 'cs102');
INSERT INTO students (name, roll_number, password) VALUES ('Karan Mehta', 'CS103', 'cs103');

-- Default admin login: username "admin", password "admin123"
INSERT INTO admins (username, password) VALUES ('admin', 'admin123');
