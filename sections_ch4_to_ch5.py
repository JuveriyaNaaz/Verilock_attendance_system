# -*- coding: utf-8 -*-
"""
Generates Chapters 4 and 5 for the Verilock Mini Project Report.
"""
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL

def add_ch4_to_ch5(doc, add_chap, add_sec, add_body, add_bullet, add_table, add_fig_cap, add_tbl_cap, add_code_box):
    # ========================================================
    # CHAPTER 4 — SYSTEM ANALYSIS AND DESIGN
    # ========================================================
    add_chap(doc, 4, "SYSTEM ANALYSIS AND DESIGN")

    add_sec(doc, "4.1", "EXISTING SYSTEM AND OPERATIONAL BOTTLENECKS", level=2)
    add_body(doc,
        "In existing academic environments, student attendance recording is dominated by two paradigms: traditional pen-and-paper registers and static digital approaches (such as fixed QR codes or standalone biometric finger scanners). Both systems introduce severe operational friction and security deficiencies:"
    )
    add_bullet(doc, "Instructional Time Loss: ", "Calling individual student roll numbers during a 50-minute lecture consumes 10 to 15 minutes of instructional time, reducing effective teaching duration by up to 25%.")
    add_bullet(doc, "Prevalence of Proxy Attendance: ", "Paper sign-in sheets circulated among students enable friends to sign on behalf of absent peers with virtually zero immediate accountability.")
    add_bullet(doc, "Static QR Screenshot Exploits: ", "Institutions utilizing printed or projected static QR codes suffer from instant image sharing. A present student simply photographs the projected code and forwards it to absent friends via instant messaging, allowing remote fraudulent check-ins.")
    add_bullet(doc, "High Biometric Infrastructure Costs: ", "Dedicated fingerprint or RFID hardware devices require heavy initial capital expenditure, continuous wiring maintenance, and produce severe physical congestion at classroom doorways before lectures begin.")
    add_bullet(doc, "Absence of Proactive Analytics: ", "Existing systems record attendance purely as static historical records. Faculty members only discover severe attendance deficits at the end of the semester when detaining students, leaving zero time for academic corrective intervention.")

    add_sec(doc, "4.2", "PROBLEM STATEMENT", level=2)
    add_body(doc,
        "Conventional attendance systems fail to balance speed, operational security, and cost efficiency. Static digital identifiers permit effortless remote proxy marking via screenshot sharing, while dedicated biometric hardware creates prohibitive infrastructure costs and classroom entry bottlenecks. Furthermore, existing platforms lack predictive intelligence to identify students trending toward attendance shortages before it is too late.",
        bold_prefix="Core Problem Statement: "
    )
    add_body(doc,
        "Hence, there is a compelling need for a zero-hardware, browser-accessible, anti-proxy attendance management platform that mathematically invalidates captured credentials within seconds, eliminates duplicate records, and embeds machine learning models to provide actionable early-warning retention alerts."
    )

    add_sec(doc, "4.3", "PROPOSED VERILOCK SYSTEM", level=2)
    add_body(doc,
        "The proposed system, VERILOCK — SMART QR ATTENDANCE SYSTEM, resolves these limitations by synthesizing ephemeral dynamic QR cryptography with web technologies and supervised machine learning. Rather than relying on static images, Verilock generates time-bound tokens that refresh every 8 seconds on the instructor's classroom screen."
    )
    add_body(doc,
        "Table 4.1 summarizes the architectural and operational improvements introduced by Verilock compared to legacy systems."
    )

    add_tbl_cap(doc, "4.1", "Comparison Between Existing and Proposed Attendance Systems")
    tbl_compare_headers = ["Parameter", "Manual / Paper Register", "Static QR Code System", "Proposed Verilock System"]
    tbl_compare_data = [
        ["Time Consumption", "10–15 minutes per lecture", "3–5 minutes", "Under 1 minute (concurrent)"],
        ["Proxy Resistance", "Extremely Low (buddy signing)", "Zero (screenshot forwarding)", "Very High (8s token expiry)"],
        ["Hardware Requirements", "Paper registers / pens", "Projector / Printed sheet", "Zero extra (standard phones/PC)"],
        ["Entry Bottlenecks", "None (circulated in class)", "None", "None (distributed scanning)"],
        ["Subject-Wise Breakdown", "Manual paper collation", "Requires periodic export", "Real-time automated portal"],
        ["Attendance Analytics", "None (post-semester)", "Static percentages only", "AI Logistic Regression risk prediction"],
        ["Cost & Deployment", "Recurring stationery cost", "Low software cost", "Zero hardware; open web deployment"]
    ]
    add_table(doc, [Inches(1.8), Inches(1.8), Inches(1.8), Inches(1.8)], tbl_compare_headers, tbl_compare_data)

    add_sec(doc, "4.4", "PROJECT MODULES", level=2)
    add_body(doc,
        "Verilock is engineered into five modular, decoupled software subsystems designed for high cohesion and clear separation of responsibilities:"
    )
    add_bullet(doc, "1. Student Module: ", "Manages student registration, credential validation, individual session portal, real-time subject-wise percentage cards, session attendance history, in-browser HTML5 camera scanning, manual token fallback, and personalized AI risk badges.")
    add_bullet(doc, "2. Faculty / Admin Module: ", "Handles administrator authentication, class session initialization, curriculum subject selection (SNLP, OS, WIT, OOAD, ML, etc.), live animated countdown display, active headcount telemetry, and the comprehensive AI risk report.")
    add_bullet(doc, "3. Dynamic QR Authentication Module: ", "Executes server-side cryptographically secure pseudorandom token generation (secrets.token_urlsafe(16)), computes strict 8-second expiration timestamps, streams dynamic QR matrix images in PNG format, and rejects expired codes.")
    add_bullet(doc, "4. Attendance Tracking Module: ", "Verifies active session state, performs duplicate attendance checks against SQLite table constraints, records precise ISO timestamps upon successful marking, and renders aggregate subject breakdown statistics.")
    add_bullet(doc, "5. AI Risk Prediction Module: ", "Extracts early-window attendance percentage and temporal trajectory across the initial 15 sessions, feeds features into a serialized Scikit-learn Logistic Regression model, and computes class probabilities to stratify students into Safe, Watch, and Critical tiers.")

    add_sec(doc, "4.5", "PROCESS MODEL USED WITH JUSTIFICATION", level=2)
    add_body(doc,
        "For the systematic design, implementation, and verification of Verilock, the SDLC Umbrella (Waterfall-based Systematic) Model was adopted, aligning with standard institutional software engineering practices."
    )
    add_bullet(doc, "Requirement Gathering: ", "Identification of classroom pain points, proxy vectors, instructor needs, and 75% attendance university mandates.")
    add_bullet(doc, "Analysis Stage: ", "Formulation of mathematical constraints for token TTL (8 seconds), database schema dependencies, and ML feature formulation.")
    add_bullet(doc, "Designing Stage: ", "Creation of UML architectural blueprints (Use Case, Class, Sequence, Activity, Component, Deployment, DFD, and ER schemas).")
    add_bullet(doc, "Development (Coding) Stage: ", "Iterative coding of Flask endpoints, SQLite database migrations, HTML5-QRCode integration, and Scikit-learn model training.")
    add_bullet(doc, "Integration & Testing Stage: ", "End-to-end verification of camera scanning, token rotation timers, duplicate rejection, and cross-browser responsiveness.")
    add_bullet(doc, "Installation & Acceptance: ", "Deployment onto local and staged web server environments (e.g., local Flask server exposed via secure HTTPS tunneling).")
    add_bullet(doc, "Maintenance: ", "Continuous monitoring of token expiration accuracy, synthetic model calibration, and feedback collection.")

    add_sec(doc, "4.6", "SOFTWARE REQUIREMENT SPECIFICATION (SRS)", level=2)
    add_body(doc,
        "The Software Requirements Specification establishes the precise operational parameters, functional requirements, non-functional criteria, and environment prerequisites for Verilock."
    )
    add_sec(doc, "4.6.1", "Functional Requirements", level=3)
    add_bullet(doc, "FR1 - User Registration & Authentication: ", "The system shall allow students to register with Name, Roll Number, and Password, and allow faculty to register with Username and Password.")
    add_bullet(doc, "FR2 - Session Initialization: ", "Instructors shall select a curriculum course and launch an active attendance session.")
    add_bullet(doc, "FR3 - Dynamic Token Rotation: ", "The server shall generate a new 16-byte random token and refresh the projected QR code strictly every 8 seconds.")
    add_bullet(doc, "FR4 - In-Browser Scanning: ", "The student portal shall access the client device's camera stream to scan and decode the projected QR code in real time.")
    add_bullet(doc, "FR5 - Manual Entry Fallback: ", "The student portal shall provide a text field allowing students to manually submit the displayed token if camera access fails.")
    add_bullet(doc, "FR6 - Duplicate Prevention: ", "The database shall enforce a unique constraint on (session_id, student_id) to prevent multiple markings for the same session.")
    add_bullet(doc, "FR7 - Real-Time Dashboard Updates: ", "The faculty dashboard shall poll attendance data every 3 seconds to display the live list of present students.")
    add_bullet(doc, "FR8 - Predictive Risk Reporting: ", "The system shall calculate early attendance metrics and output risk categories (Safe, Watch, Critical) with calibrated probabilities.")

    add_sec(doc, "4.6.2", "Non-Functional Requirements", level=3)
    add_bullet(doc, "NFR1 - Security: ", "Tokens must be cryptographically unpredictable and strictly expire after 8 seconds to prevent replay attacks.")
    add_bullet(doc, "NFR2 - Performance & Latency: ", "QR validation and database insertion must complete within 200 milliseconds to support concurrent student submissions.")
    add_bullet(doc, "NFR3 - Usability & Accessibility: ", "The web interface must be clean, responsive, and render flawlessly on mobile, tablet, and desktop screens without dedicated app installations.")
    add_bullet(doc, "NFR4 - Reliability: ", "Database transactions must satisfy ACID compliance using SQLite WAL journaling to avoid lock contentions.")

    add_sec(doc, "4.6.3", "Hardware and Software Requirements", level=3)
    add_body(doc,
        "The minimal hardware and software environments required for hosting and operating Verilock are specified below."
    )
    add_tbl_cap(doc, "4.2", "Hardware Requirements Specification")
    tbl_hw_headers = ["Component", "Minimum Requirement (Server / Faculty)", "Minimum Requirement (Student Client)"]
    tbl_hw_data = [
        ["Processor", "Dual-Core 2.0 GHz Intel / AMD / ARM", "Modern Smartphone / Tablet / Laptop Processor"],
        ["RAM", "2 GB RAM", "1 GB RAM"],
        ["Display", "1080p Classroom Screen / Projector / Monitor", "Smartphone Touchscreen (HD 720p minimum)"],
        ["Camera", "Not Required on Host Server", "Integrated 2MP+ Autofocus Smartphone/Web Camera"],
        ["Network", "Local Wi-Fi / LAN with Internet connectivity", "Wi-Fi or 4G/5G Mobile Cellular Data"]
    ]
    add_table(doc, [Inches(1.8), Inches(2.7), Inches(2.7)], tbl_hw_headers, tbl_hw_data)

    add_tbl_cap(doc, "4.3", "Software Requirements Specification")
    tbl_sw_headers = ["Category", "Specification / Tool Employed"]
    tbl_sw_data = [
        ["Operating System", "Microsoft Windows 10/11, Ubuntu Linux 20.04+, or macOS"],
        ["Programming Language", "Python 3.10+ (Server-Side), JavaScript ES6 (Client-Side)"],
        ["Web Framework", "Flask 2.3+ (WSGI Application Server)"],
        ["Database Engine", "SQLite 3 (Relational Embedded Database)"],
        ["Machine Learning Library", "Scikit-learn 1.3+, NumPy, Joblib"],
        ["QR Code Libraries", "qrcode (Python generation), HTML5-QRCode 2.3.8 (JS decoding)"],
        ["Web Client / Browser", "Google Chrome 90+, Mozilla Firefox, Safari, Edge with WebRTC support"]
    ]
    add_table(doc, [Inches(2.5), Inches(4.7)], tbl_sw_headers, tbl_sw_data)

    add_sec(doc, "4.7", "FEASIBILITY STUDY", level=2)
    add_bullet(doc, "Technical Feasibility: ", "The platform leverages widely adopted web technologies (Python, Flask, SQLite, WebRTC). Browser-based camera access via HTML5 APIs is natively supported across all modern Android and iOS devices, requiring zero third-party mobile installations. Hence, the system is technically fully feasible.")
    add_bullet(doc, "Operational Feasibility: ", "The workflow requires minimal cognitive overhead: instructors click 'Start Session', and students click 'Mark Attendance' and point their camera. The intuitive UI ensures immediate adoption by students and faculty without training.")
    add_bullet(doc, "Economic Feasibility: ", "Unlike biometric systems requiring costly scanners (e.g., $150-$500 per room) or RFID readers, Verilock relies entirely on open-source software and existing consumer smartphones/projectors. Capital expenditure is zero.")

    add_sec(doc, "4.8", "SYSTEM DESIGN AND UML MODELING", level=2)
    add_body(doc,
        "System design translates software requirements into concrete architectural blueprints. Unified Modeling Language (UML) diagrams and Data Flow Diagrams (DFDs) provide standard visual representations of the system's structural and behavioral properties."
    )

    add_sec(doc, "4.8.1", "Use Case Modeling", level=3)
    add_body(doc,
        "The Use Case Diagram defines the functional boundary between the primary actors (Student and Faculty Administrator) and the application core."
    )
    add_code_box(doc,
"""+-----------------------------------------------------------------------------------+
|                        VERILOCK SMART ATTENDANCE SYSTEM                            |
|                                                                                   |
|      +---------------------+                  +------------------------------+     |
|      |       STUDENT       |                  |       FACULTY / ADMIN        |     |
|      +----------+----------+                  +--------------+---------------+     |
|                 |                                            |                     |
|                 +---> [ Student Sign Up / Login ]            +---> [ Admin Login ] |
|                 |                                            |                     |
|                 +---> [ View Overall Attendance % ]          +---> [ Start Session]|
|                 |                                            |     (Choose Subject)|
|                 +---> [ View Subject-Wise Table ]            |                     |
|                 |                                            +---> [ Display Live  |
|                 +---> [ Scan Live QR (HTML5 Camera) ]        |       Rotating QR ] |
|                 |                                            |                     |
|                 +---> [ Manual Token Entry Fallback ]        +---> [ Monitor Live  |
|                 |                                            |       Headcount ]   |
|                 +---> [ View AI Attendance Risk Badge ]      |                     |
|                 |                                            +---> [ End Session ] |
|                 +---> [ View Attendance History Log ]        |                     |
|                                                              +---> [ View AI Risk  |
|                                                                      Report Table ]|
+-----------------------------------------------------------------------------------+"""
    )
    add_fig_cap(doc, "4.3", "Use Case Model for Student and Faculty Actors")

    add_sec(doc, "4.8.2", "Class Diagram", level=3)
    add_body(doc,
        "The Class Diagram models the core entity objects, attributes, and relationships implemented in the Flask/SQLite backend."
    )
    add_code_box(doc,
"""+-----------------------+              +------------------------+
|        Student        |              |         Admin          |
+-----------------------+              +------------------------+
| - id: int             |              | - id: int              |
| - name: str           |              | - username: str        |
| - roll_number: str    |              | - password: str        |
| - password: str       |              +------------------------+
+-----------------------+              | + login()              |
| + register()          |              | + start_session()      |
| + login()             |              | + end_session()        |
| + scan_qr()           |              | + view_risk_report()   |
| + get_risk_status()   |              +------------------------+
+-----------+-----------+                          |
            | 1                                    | 1
            |                                      | manages
            | records                              v 0..*
            | 0..*                     +------------------------+
+-----------v-----------+              |        Session         |
|      Attendance       |              +------------------------+
+-----------------------+        0..*  | - id: int              |
| - id: int             | >------------+ - subject: str         |
| - session_id: int     |              | - date: str            |
| - student_id: int     |              | - start_time: str      |
| - marked_at: str      |              | - is_active: int       |
+-----------------------+              +------------------------+
| + record_entry()      |                          | 1
+-----------------------+                          | generates
                                                   v 1..*
                                       +------------------------+
                                       |         Token          |
                                       +------------------------+
                                       | - id: int              |
                                       | - session_id: int      |
                                       | - token_value: str     |
                                       | - created_at: str      |
                                       | - expires_at: str      |
                                       +------------------------+
                                       | + is_valid(): bool     |
                                       | + rotate(): void       |
                                       +------------------------+"""
    )
    add_fig_cap(doc, "4.4", "Class Diagram Depicting System Entities, Attributes, and Associations")

    add_sec(doc, "4.8.3", "Sequence Diagram", level=3)
    add_body(doc,
        "The Sequence Diagram details the chronological message interactions during dynamic token generation, QR scanning, server validation, and database persistence."
    )
    add_code_box(doc,
"""Student Browser          Faculty Display          Flask Backend           SQLite DB
      |                         |                       |                     |
      |                         |--- Start Session ---->|                     |
      |                         |    (Pick Subject)     |--- Insert Session ->|
      |                         |                       |<-- Session ID ------|
      |                         |<-- Render Dashboard --|                     |
      |                         |                       |                     |
      |                         |--- Get Current QR --->|                     |
      |                         |                       |-- Generate Token -->|
      |                         |                       |   (secrets 16B)     |
      |                         |                       |-- Insert Token ---->|
      |                         |<-- Stream QR (8s TTL)-|                     |
      |                         |                       |                     |
      |--- Scan QR Matrix ----->|                       |                     |
      |--- POST /mark_attendance (token) -------------->|                     |
      |    [HTTP JSON Request]                          |-- Query Token ----->|
      |                                                 |<-- Token Record ----|
      |                                                 |                     |
      |                                                 |-- Validate Expire --|
      |                                                 |   (now <= expiry)   |
      |                                                 |                     |
      |                                                 |-- Check Duplicate ->|
      |                                                 |<-- Prior Records ---|
      |                                                 |                     |
      |                                                 |-- Insert Attendance>|
      |                                                 |<-- Success Commit --|
      |<-- 200 OK ("Attendance marked successfully!")---|                     |
      |                                                 |                     |
      |                         |--- Poll Headcount --->|                     |
      |                         |<-- Live Present List -|                     |"""
    )
    add_fig_cap(doc, "4.5", "Sequence Diagram for Dynamic Token Verification and Attendance Marking")

    add_sec(doc, "4.8.4", "Activity Diagram", level=3)
    add_body(doc,
        "The Activity Diagram maps the execution flow of activities from the moment a student attempts to register attendance to the system's final feedback response."
    )
    add_code_box(doc,
"""       [ Start: Student Opens Portal ]
                      |
                      v
             [ Point Camera at Screen ]
                      |
                      v
            < QR Code Detected? >
             /                 \\
          (Yes)                (No)
           /                     \\
          v                       v
   [ Decode Token String ]   [ Enter Code Manually ]
          \\                       /
           +----------+----------+
                      |
                      v
       [ POST Token to Server Endpoint ]
                      |
                      v
        < Token Exists in DB? >
         /                 \\
      (No)                 (Yes)
       /                     \\
      v                       v
 [ Reject: Invalid Code ]   < Expired? (now > expires_at) >
                              /                     \\
                           (Yes)                    (No)
                            /                         \\
                           v                           v
              [ Reject: Code Expired ]      < Already Marked Today? >
                                              /                 \\
                                           (Yes)                (No)
                                            /                     \\
                                           v                       v
                                  [ Reject Duplicate ]    [ Insert Attendance ]
                                                                   |
                                                                   v
                                                         [ Return Success Msg ]
                                                                   |
                                                                   v
                                                         [ Refresh Student UI ]"""
    )
    add_fig_cap(doc, "4.6", "Activity Diagram of Attendance Marking and Token Rotation")

    add_sec(doc, "4.8.5", "Component and Deployment Diagrams", level=3)
    add_body(doc,
        "The Component Diagram models the software packages and runtime libraries, while the Deployment Diagram depicts the physical mapping of software artifacts onto network nodes."
    )
    add_code_box(doc,
"""[ COMPONENT ARCHITECTURE ]
+---------------------------------------------------------------------------------+
| CLIENT LAYER (Browser Runtime)                                                  |
|   +-----------------------+    +-------------------------+                      |
|   |  Jinja2 HTML5 Views   |    |  HTML5-QRCode Library   |                      |
|   +-----------+-----------+    +------------+------------+                      |
+---------------|-----------------------------|-----------------------------------+
                | HTTP GET                    | JSON POST
                v                             v
+---------------------------------------------------------------------------------+
| SERVER APPLICATION LAYER (Flask Web Engine)                                     |
|   +-----------------------+    +-------------------------+                      |
|   |  Route Controllers    |--->|  Dynamic Token Manager  |                      |
|   |  (app.py endpoints)   |    |  (secrets & qrcode)     |                      |
|   +-----------+-----------+    +------------+------------+                      |
|               |                             |                                   |
|               v                             v                                   |
|   +-----------------------+    +-------------------------+                      |
|   |  Session Auth Manager |    |  ML Risk Engine         |                      |
|   |  (Cookie Sessions)    |    |  (Joblib / Scikit-Learn)|                      |
|   +-----------+-----------+    +------------+------------+                      |
+---------------|-----------------------------|-----------------------------------+
                v                             v
+---------------------------------------------------------------------------------+
| DATA PERSISTENCE LAYER                                                          |
|   +------------------------------------------------------+                      |
|   |  SQLite 3 Database (attendance.db)                   |                      |
|   |  Tables: students, admins, sessions, tokens, attend  |                      |
|   +------------------------------------------------------+                      |
+---------------------------------------------------------------------------------+"""
    )
    add_fig_cap(doc, "4.7", "Component Diagram Depicting Architectural Modules")

    add_code_box(doc,
"""[ DEPLOYMENT ARCHITECTURE ]
+-------------------------------+                  +-------------------------------+
|     CLIENT NODE (Student)     |                  |     CLIENT NODE (Faculty)     |
| +---------------------------+ |                  | +---------------------------+ |
| | Mobile / Desktop Browser  | |                  | | Large Classroom Display   | |
| | (Chrome, Firefox, Safari) | |                  | | In-Browser Live Dashboard | |
| +-------------+-------------+ |                  | +-------------+-------------+ |
+---------------|---------------+                  +---------------|---------------+
                | HTTPS / TLS 1.3                                  | HTTPS / TLS 1.3
                +-----------------------+  +-----------------------+
                                        |  |
                                        v  v
                        +-----------------------------------+
                        |         HOST SERVER NODE          |
                        | +-------------------------------+ |
                        | | Python 3.10+ WSGI Environment | |
                        | | Flask Web Application Engine  | |
                        | | Scikit-learn Risk Predictor   | |
                        | +---------------+---------------+ |
                        |                 | Direct File I/O |
                        | +---------------v---------------+ |
                        | | SQLite Database Storage       | |
                        | | (attendance.db, risk_model)   | |
                        | +-------------------------------+ |
                        +-----------------------------------+"""
    )
    add_fig_cap(doc, "4.8", "Deployment Diagram of Verilock Web Server and Database Nodes")

    add_sec(doc, "4.8.6", "Data Flow Diagrams (DFD Level 0 and Level 1)", level=3)
    add_body(doc,
        "Data Flow Diagrams track the path and transformation of data inputs into database outputs. Level 0 (Context Diagram) establishes the high-level system boundary, while Level 1 decomposes the internal processes."
    )
    add_code_box(doc,
"""[ DFD LEVEL 0: CONTEXT DIAGRAM ]

  +---------------+    Login Credentials, Scanned Token     +--------------------+
  |               | --------------------------------------> |                    |
  |    STUDENT    |                                         |      VERILOCK      |
  |               | <-------------------------------------- |     ATTENDANCE     |
  +---------------+    Attendance Confirmation, Risk Badge  |       SYSTEM       |
                                                            |                    |
  +---------------+    Session Commands, Subject Choice     |                    |
  |   FACULTY /   | --------------------------------------> |                    |
  |     ADMIN     | <-------------------------------------- |                    |
  +---------------+    Live Rotating QR, Headcount List     +--------------------+"""
    )
    add_fig_cap(doc, "4.9", "Data Flow Diagram — Level 0 Context Diagram")

    add_code_box(doc,
"""[ DFD LEVEL 1: DETAILED FUNCTIONAL DATA FLOW ]

  (Student) ----> [ 1.0 Auth Process ] <====> (D1: students)
                         |
                         v (Valid Session)
  (Student) ----> [ 2.0 Ingest Token ]
                         |
                         +--------> [ 3.0 Validate Expiry ] <====> (D2: tokens)
                                           |
                                           v (Token Fresh)
                                    [ 4.0 Check Duplicate ] <====> (D3: attendance)
                                           |
                                           v (Not Marked)
                                    [ 5.0 Record Attendance ] ====> (D3: attendance)
                                           |
                                           v
  (Faculty) <--- [ 6.0 Headcount Telemetry ]
                         |
  (ML Engine) <- [ 7.0 Feature Extraction ] <==== (D3: attendance & sessions)
                         |
                         v
                 [ 8.0 Logistic Regression ] ====> Risk Badge to Student & Faculty"""
    )
    add_fig_cap(doc, "4.10", "Data Flow Diagram — Level 1 Detailed Functional Flow")

    add_sec(doc, "4.8.7", "Database Design and Data Dictionary", level=3)
    add_body(doc,
        "The relational schema is implemented in SQLite 3 via 'schema.sql'. The data dictionary detailing attributes, types, keys, and constraints is provided in Table 4.4."
    )
    add_tbl_cap(doc, "4.4", "Database Schema Data Dictionary for Verilock")
    tbl_db_headers = ["Table Name", "Column Name", "Data Type", "Constraint", "Description"]
    tbl_db_data = [
        ["students", "id", "INTEGER", "PRIMARY KEY AUTOINCREMENT", "Unique internal student identifier"],
        ["students", "name", "TEXT", "NOT NULL", "Student full legal name"],
        ["students", "roll_number", "TEXT", "UNIQUE NOT NULL", "University institutional roll number"],
        ["students", "password", "TEXT", "NOT NULL", "Account authentication secret"],
        ["admins", "id", "INTEGER", "PRIMARY KEY AUTOINCREMENT", "Unique internal administrator identifier"],
        ["admins", "username", "TEXT", "UNIQUE NOT NULL", "Faculty login username"],
        ["admins", "password", "TEXT", "NOT NULL", "Faculty authentication secret"],
        ["sessions", "id", "INTEGER", "PRIMARY KEY AUTOINCREMENT", "Unique classroom session identifier"],
        ["sessions", "subject", "TEXT", "NOT NULL", "Academic subject name (e.g., SNLP, ML)"],
        ["sessions", "date", "TEXT", "NOT NULL", "Calendar date of class session (YYYY-MM-DD)"],
        ["sessions", "start_time", "TEXT", "NOT NULL", "Session initiation timestamp (HH:MM)"],
        ["sessions", "is_active", "INTEGER", "DEFAULT 1", "Session active status flag (1=active, 0=closed)"],
        ["tokens", "id", "INTEGER", "PRIMARY KEY AUTOINCREMENT", "Unique generated token record ID"],
        ["tokens", "session_id", "INTEGER", "FOREIGN KEY (sessions.id)", "Reference to parent active session"],
        ["tokens", "token_value", "TEXT", "NOT NULL", "16-byte cryptographically secure random string"],
        ["tokens", "created_at", "TEXT", "NOT NULL", "ISO timestamp of token generation"],
        ["tokens", "expires_at", "TEXT", "NOT NULL", "ISO timestamp of token expiration (created+8s)"],
        ["attendance", "id", "INTEGER", "PRIMARY KEY AUTOINCREMENT", "Unique attendance transaction ID"],
        ["attendance", "session_id", "INTEGER", "FOREIGN KEY (sessions.id)", "Reference to active session marked"],
        ["attendance", "student_id", "INTEGER", "FOREIGN KEY (students.id)", "Reference to student marked present"],
        ["attendance", "marked_at", "TEXT", "NOT NULL", "ISO timestamp of successful attendance verification"]
    ]
    add_table(doc, [Inches(1.2), Inches(1.3), Inches(1.0), Inches(1.8), Inches(1.9)], tbl_db_headers, tbl_db_data)

    # ========================================================
    # CHAPTER 5 — ALGORITHMS AND TECHNIQUES
    # ========================================================
    add_chap(doc, 5, "ALGORITHMS AND TECHNIQUES")

    add_sec(doc, "5.1", "CRYPTOGRAPHICALLY SECURE DYNAMIC TOKEN GENERATION", level=2)
    add_body(doc,
        "A critical vulnerability in legacy QR systems is the predictability or permanence of attendance tokens. If an attacker can guess subsequent tokens or reuse a captured token, the anti-proxy guarantee collapses. Verilock guarantees high entropy and zero predictability by utilizing Python's 'secrets' module, which queries the operating system's kernel cryptographic random number generator (CryptGenRandom on Windows, /dev/urandom on Linux/macOS)."
    )
    add_code_box(doc,
"""Algorithm 1: Dynamic Token Generation and QR Matrix Streaming
Input: session_id (Active Class Session Identifier)
Output: token_value, QR_Code_Image_Stream
Constants: TOKEN_VALID_SECONDS = 8

1.  Function GenerateDynamicToken(session_id):
2.      token_value <- secrets.token_urlsafe(nbytes = 16)
3.      now <- CurrentSystemTimestamp()
4.      expires_at <- now + Seconds(TOKEN_VALID_SECONDS)
5.      ExecuteSQL("INSERT INTO tokens (session_id, token_value, created_at, expires_at) 
                    VALUES (?, ?, ?, ?)", session_id, token_value, now.ISO(), expires_at.ISO())
6.      CommitTransaction()
7.      qr_matrix <- qrcode.make(token_value)
8.      image_buffer <- CreateInMemoryBytesBuffer()
9.      qr_matrix.save(image_buffer, format = "PNG")
10.     image_buffer.seek(0)
11.     Return image_buffer"""
    )
    add_body(doc,
        "Because each token contains 16 bytes of entropy (yielding 2^128 possible permutations encoded in URL-safe base64), brute-force token enumeration within an 8-second window is computationally impossible."
    )

    add_sec(doc, "5.2", "EPHEMERAL TOKEN EXPIRATION AND VALIDATION ALGORITHM", level=2)
    add_body(doc,
        "When an incoming token is submitted via HTTP POST to the '/mark_attendance' endpoint, the server must verify both existence and temporal validity before accepting attendance."
    )
    add_code_box(doc,
"""Algorithm 2: Ephemeral Token Freshness Verification
Input: submitted_token (String received from student scan)
Output: matched_session_id (Integer or NULL)

1.  Function FindSessionForValidToken(submitted_token):
2.      row <- ExecuteSQL("SELECT * FROM tokens WHERE token_value = ? 
                          ORDER BY id DESC LIMIT 1", submitted_token).FetchOne()
3.      If row is NULL Then:
4.          Return NULL  // Token was never generated
5.      End If
6.      token_expires_at <- ParseISOTimestamp(row['expires_at'])
7.      current_time <- CurrentSystemTimestamp()
8.      If current_time > token_expires_at Then:
9.          Return NULL  // Token has expired (> 8 seconds elapsed)
10.     Else:
11.         Return row['session_id']  // Token is valid and fresh
12.     End If"""
    )

    add_sec(doc, "5.3", "ATTENDANCE RECORDING AND DUPLICATE CHECKING", level=2)
    add_body(doc,
        "Once a token is confirmed valid, the system prevents duplicate markings for the same student within the same class session, ensuring data integrity."
    )
    add_code_box(doc,
"""Algorithm 3: Attendance Recording and Anti-Duplicate Verification
Input: student_id, submitted_token
Output: JSON Response (Success Status, Message)

1.  Function MarkStudentAttendance(student_id, submitted_token):
2.      If student_id is NOT in ActiveSession Then:
3.          Return HTTP_401("Unauthorized: Please log in first.")
4.      End If
5.      session_id <- FindSessionForValidToken(submitted_token)
6.      If session_id is NULL Then:
7.          Return HTTP_400("This code has expired. Scan the current one.")
8.      End If
9.      already_marked <- ExecuteSQL("SELECT id FROM attendance 
                                     WHERE session_id = ? AND student_id = ?", 
                                     session_id, student_id).FetchOne()
10.     If already_marked is NOT NULL Then:
11.         subject_name <- GetSessionSubject(session_id)
12.         Return HTTP_400("You're already marked present for " + subject_name + " today.")
13.     End If
14.     mark_time <- CurrentSystemTimestamp().ISO()
15.     ExecuteSQL("INSERT INTO attendance (session_id, student_id, marked_at) 
                    VALUES (?, ?, ?)", session_id, student_id, mark_time)
16.     CommitTransaction()
17.     Return HTTP_200("Attendance marked successfully!")"""
    )

    add_sec(doc, "5.4", "MACHINE LEARNING: LOGISTIC REGRESSION FOR RISK PREDICTION", level=2)
    add_body(doc,
        "The predictive analytics component of Verilock identifies students likely to finish the semester with less than 75% attendance based on their early behavioral pattern. Binary Logistic Regression models the probability P that a given student belongs to the 'at-risk' class (y = 1)."
    )
    add_body(doc,
        "z = w_1 · x_1 + w_2 · x_2 + b",
        bold_prefix="Logit Score: ",
        italic=True,
        align=WD_ALIGN_PARAGRAPH.CENTER
    )
    add_body(doc,
        "P(y = 1) = 1 / (1 + e^-z)",
        bold_prefix="Sigmoid Probability: ",
        italic=True,
        align=WD_ALIGN_PARAGRAPH.CENTER
    )
    add_body(doc,
        "During model fitting ('train_risk_model.py'), Logistic Regression optimizes parameters w and b by minimizing binary cross-entropy loss via the L-BFGS numerical solver:"
    )
    add_body(doc,
        "Loss = - (1/N) * sum[ y_i * log(p_i) + (1 - y_i) * log(1 - p_i) ]",
        bold_prefix="Cross-Entropy Objective: ",
        italic=True,
        align=WD_ALIGN_PARAGRAPH.CENTER
    )

    add_sec(doc, "5.5", "FEATURE ENGINEERING AND TEMPORAL TREND EXTRACTION", level=2)
    add_body(doc,
        "Rather than relying on raw session counts, the model extracts two scale-invariant behavioral features across an early observation window of the first 15 sessions (W = 15):"
    )
    add_bullet(doc, "Feature 1 — Early Attendance Percentage (x_1): ", "The percentage of sessions attended during the early window: x_1 = (sum(record[0..W-1]) / W) * 100.")
    add_bullet(doc, "Feature 2 — Attendance Trend (x_2): ", "The differential rate of change between the second half and first half of the window: x_2 = [mean(record[W/2..W-1]) - mean(record[0..W/2-1])] * 100. A positive trend indicates improving consistency, whereas a negative trend indicates deteriorating attendance.")

    add_sec(doc, "5.6", "SYNTHETIC TRAINING DATA GENERATION", level=2)
    add_body(doc,
        "Because any newly deployed attendance system suffers from the 'cold-start' problem (i.e., lacking historical multi-semester attendance records), Verilock simulates 2,000 synthetic student semester trajectories. In educational settings, student reliability is non-uniform; most students maintain satisfactory attendance, while a minority exhibits irregular habits. To mirror real classrooms, each synthetic student is assigned an intrinsic reliability score r drawn from a Beta distribution:"
    )
    add_body(doc,
        "r ~ Beta(alpha = 5, beta = 2)",
        bold_prefix="Beta Reliability Prior: ",
        italic=True,
        align=WD_ALIGN_PARAGRAPH.CENTER
    )
    add_body(doc,
        "Daily attendance across 60 sessions is generated as a Bernoulli trial: attendance_k = 1 if Uniform(0,1) < (r + N(0, 0.05)), else 0. Students finishing with final semester attendance below 75% are labeled as at-risk (y = 1). Training on these 2,000 synthetic trajectories yielded an empirical training accuracy of 84.35% with learned weights w_1 = -0.1596 and w_2 = -0.0016. The negative weights confirm the intuitive domain reality: higher early attendance and positive attendance trends decrease the probability of falling below the 75% threshold."
    )

    add_sec(doc, "5.7", "RISK CATEGORIZATION AND DECISION THRESHOLDS", level=2)
    add_body(doc,
        "To provide actionable guidance for faculty, the continuous risk probability P_risk is mapped into three stratified categories as shown in Table 5.2."
    )
    add_tbl_cap(doc, "5.2", "Risk Classification Thresholds and Color Indicators")
    tbl_risk_headers = ["Probability Range", "Risk Category", "Visual Badge", "Actionable Academic Guidance"]
    tbl_risk_data = [
        ["P_risk < 30%", "Safe", "Green Circle (🟢 Safe)", "Student exhibits high attendance consistency; no intervention required."],
        ["30% <= P_risk < 60%", "Watch", "Yellow Circle (🟡 Watch)", "Student exhibits early irregularity; faculty advisory recommended."],
        ["P_risk >= 60%", "Critical", "Red Circle (🔴 Critical)", "High likelihood of shortage (<75%); immediate counselor notice issued."]
    ]
    add_table(doc, [Inches(1.5), Inches(1.3), Inches(1.8), Inches(2.6)], tbl_risk_headers, tbl_risk_data)

    print("Chapters 4 and 5 added.")
