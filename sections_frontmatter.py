# -*- coding: utf-8 -*-
"""
Front matter builder for Verilock Mini Project Report.
"""
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL

def add_front_matter(doc):
    # ==========================
    # 1. TITLE / COVER PAGE
    # ==========================
    p_top = doc.add_paragraph()
    p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_top.paragraph_format.space_before = Pt(12)
    p_top.paragraph_format.space_after = Pt(8)
    r = p_top.add_run("A Mini Project Report on")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(14)
    r_t = p_title.add_run('"VERILOCK — SMART QR ATTENDANCE SYSTEM"')
    r_t.font.name = 'Times New Roman'
    r_t.font.size = Pt(17)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(0, 51, 102)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(4)
    p_sub.paragraph_format.space_after = Pt(2)
    r = p_sub.add_run("Submitted to")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

    p_univ = doc.add_paragraph()
    p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_univ.paragraph_format.space_before = Pt(2)
    p_univ.paragraph_format.space_after = Pt(10)
    r = p_univ.add_run("OSMANIA UNIVERSITY, Hyderabad")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True

    p_deg = doc.add_paragraph()
    p_deg.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_deg.paragraph_format.space_before = Pt(4)
    p_deg.paragraph_format.space_after = Pt(2)
    r = p_deg.add_run("in partial fulfillment of the requirements for the award of degree of")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)

    p_deg2 = doc.add_paragraph()
    p_deg2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_deg2.paragraph_format.space_before = Pt(4)
    p_deg2.paragraph_format.space_after = Pt(2)
    r = p_deg2.add_run("BACHELOR OF ENGINEERING\nin\nCOMPUTER SCIENCE AND ENGINEERING\n(ARTIFICIAL INTELLIGENCE & MACHINE LEARNING)")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0, 51, 102)

    p_by = doc.add_paragraph()
    p_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_by.paragraph_format.space_before = Pt(14)
    p_by.paragraph_format.space_after = Pt(6)
    r = p_by.add_run("Submitted by")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True

    # Student names & roll numbers table / placeholders
    tbl_stud = doc.add_table(rows=2, cols=2)
    tbl_stud.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_stud.rows[0].cells[0].text = "[STUDENT NAME 1]"
    tbl_stud.rows[0].cells[1].text = "[ROLL NUMBER 1]"
    tbl_stud.rows[1].cells[0].text = "[STUDENT NAME 2]"
    tbl_stud.rows[1].cells[1].text = "[ROLL NUMBER 2]"
    for row in tbl_stud.rows:
        row.cells[0].width = Inches(3.0)
        row.cells[1].width = Inches(2.5)
        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(11)
                run.font.bold = True

    p_guide = doc.add_paragraph()
    p_guide.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_guide.paragraph_format.space_before = Pt(16)
    p_guide.paragraph_format.space_after = Pt(2)
    r = p_guide.add_run("Under the guidance of\n[GUIDE NAME]\n[GUIDE DESIGNATION / ASSISTANT PROFESSOR], Dept. of CSE")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11.5)
    r.font.bold = True

    p_clg = doc.add_paragraph()
    p_clg.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_clg.paragraph_format.space_before = Pt(20)
    p_clg.paragraph_format.space_after = Pt(2)
    r = p_clg.add_run("DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING\nNAWAB SHAH ALAM KHAN COLLEGE OF ENGINEERING & TECHNOLOGY\n(Autonomous)\nMalakpet, Hyderabad.\n2024–2025")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0, 51, 102)

    # ==========================
    # 2. CERTIFICATE PAGE
    # ==========================
    doc.add_page_break()
    p_c_head = doc.add_paragraph()
    p_c_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_c_head.paragraph_format.space_before = Pt(20)
    p_c_head.paragraph_format.space_after = Pt(2)
    r = p_c_head.add_run("NAWAB SHAH ALAM KHAN\nCOLLEGE OF ENGINEERING & TECHNOLOGY\n(Autonomous)")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.bold = True
    r.font.color.rgb = RGBColor(180, 0, 0)

    p_c_appr = doc.add_paragraph()
    p_c_appr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_c_appr.paragraph_format.space_before = Pt(2)
    p_c_appr.paragraph_format.space_after = Pt(16)
    r = p_c_appr.add_run("Approved by AICTE | Affiliated to Osmania University & SBTET | Accredited by NBA (IT, ME), NAAC 'A'")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(9.5)

    p_c_title = doc.add_paragraph()
    p_c_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_c_title.paragraph_format.space_before = Pt(14)
    p_c_title.paragraph_format.space_after = Pt(20)
    r = p_c_title.add_run("CERTIFICATE")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    r.underline = True

    p_cert_body = doc.add_paragraph()
    p_cert_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_cert_body.paragraph_format.line_spacing = 1.35
    p_cert_body.paragraph_format.space_after = Pt(12)
    r = p_cert_body.add_run('This is to certify that the Mini Project work entitled ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p_cert_body.add_run('"VERILOCK — SMART QR ATTENDANCE SYSTEM"')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.bold = True
    r = p_cert_body.add_run(' is being submitted by the following students:\n')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

    # Placeholders table
    tbl_c = doc.add_table(rows=2, cols=2)
    tbl_c.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_c.rows[0].cells[0].text = "[STUDENT NAME 1]"
    tbl_c.rows[0].cells[1].text = "[ROLL NUMBER 1]"
    tbl_c.rows[1].cells[0].text = "[STUDENT NAME 2]"
    tbl_c.rows[1].cells[1].text = "[ROLL NUMBER 2]"
    for row in tbl_c.rows:
        row.cells[0].width = Inches(3.0)
        row.cells[1].width = Inches(2.5)
        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(11)
                run.font.bold = True

    p_cert_body2 = doc.add_paragraph()
    p_cert_body2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_cert_body2.paragraph_format.line_spacing = 1.35
    p_cert_body2.paragraph_format.space_before = Pt(14)
    p_cert_body2.paragraph_format.space_after = Pt(36)
    r = p_cert_body2.add_run('They have presented the project work during the academic year 2024–2025 in partial fulfillment of the requirements for the award of ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p_cert_body2.add_run('BACHELOR OF ENGINEERING in DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING (AIML) from Osmania University')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.bold = True
    r = p_cert_body2.add_run('. This is a bonafide record work carried out by them under our guidance and supervision. The results of investigation enclosed with this report have been verified and found to be satisfactory.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

    tbl_sig = doc.add_table(rows=2, cols=3)
    tbl_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_sig.rows[0].cells[0].text = "\n\n________________________\nInternal Supervisor"
    tbl_sig.rows[0].cells[1].text = "\n\n________________________\nProject Coordinator"
    tbl_sig.rows[0].cells[2].text = "\n\n________________________\nHead of the Dept."
    tbl_sig.rows[1].cells[1].text = "\n\n________________________\nExternal Examiner"
    for row in tbl_sig.rows:
        row.cells[0].width = Inches(2.1)
        row.cells[1].width = Inches(2.1)
        row.cells[2].width = Inches(2.1)
        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(10.5)
                run.font.bold = True

    # ==========================
    # 3. DECLARATION PAGE
    # ==========================
    doc.add_page_break()
    p_dec_title = doc.add_paragraph()
    p_dec_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dec_title.paragraph_format.space_before = Pt(24)
    p_dec_title.paragraph_format.space_after = Pt(24)
    r = p_dec_title.add_run("DECLARATION")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    r.underline = True

    p_dec_body = doc.add_paragraph()
    p_dec_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_dec_body.paragraph_format.line_spacing = 1.35
    p_dec_body.paragraph_format.space_after = Pt(28)
    r = p_dec_body.add_run('We hereby declare that the project work entitled ')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p_dec_body.add_run('"VERILOCK — SMART QR ATTENDANCE SYSTEM"')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.bold = True
    r = p_dec_body.add_run(' submitted to the department of Computer Science and Engineering (AIML) of NAWAB SHAH ALAM KHAN COLLEGE OF ENGINEERING AND TECHNOLOGY, affiliated to Osmania University, Hyderabad in the partial fulfillment of the requirement for the award of the degree in BACHELOR OF ENGINEERING in CSE (AIML) is a bonafide work done by the undersigned.\n\nWe further declare that the work reported herein has not been submitted either in part or in full to any other University or Institute for the award of any degree or diploma.')
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

    tbl_dec = doc.add_table(rows=2, cols=2)
    tbl_dec.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_dec.rows[0].cells[0].text = "[STUDENT NAME 1]"
    tbl_dec.rows[0].cells[1].text = "[ROLL NUMBER 1]"
    tbl_dec.rows[1].cells[0].text = "[STUDENT NAME 2]"
    tbl_dec.rows[1].cells[1].text = "[ROLL NUMBER 2]"
    for row in tbl_dec.rows:
        row.cells[0].width = Inches(3.0)
        row.cells[1].width = Inches(2.5)
        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(11)
                run.font.bold = True

    # ==========================
    # 4. ACKNOWLEDGEMENT PAGE
    # ==========================
    doc.add_page_break()
    p_ack_title = doc.add_paragraph()
    p_ack_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ack_title.paragraph_format.space_before = Pt(24)
    p_ack_title.paragraph_format.space_after = Pt(20)
    r = p_ack_title.add_run("ACKNOWLEDGEMENT")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    r.underline = True

    p_ack1 = doc.add_paragraph()
    p_ack1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_ack1.paragraph_format.line_spacing = 1.3
    p_ack1.paragraph_format.space_after = Pt(10)
    r = p_ack1.add_run("The satisfaction that accompanies the successful completion of any academic task would be incomplete without the mention of the esteemed individuals who made it possible and whose continuous encouragement and technical guidance have been a source of inspiration throughout this project work.\n\nWe express our profound sense of gratitude to ")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p_ack1.add_run("Dr. Syed Abdul Sattar, Principal")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.bold = True
    r = p_ack1.add_run(", for providing the necessary institutional facilities, academic environment, and constant support towards the development of our project.")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

    p_ack2 = doc.add_paragraph()
    p_ack2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_ack2.paragraph_format.line_spacing = 1.3
    p_ack2.paragraph_format.space_after = Pt(10)
    r = p_ack2.add_run("We would like to express our sincere thanks to ")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p_ack2.add_run("Dr. Mohammad Sanaullah Qaseem, Professor, CSE Department and Dean Computer Studies")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.bold = True
    r = p_ack2.add_run(", for sharing his invaluable knowledge, constructive feedback, and technical experience to enhance our real-time software engineering learning experience.")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

    p_ack3 = doc.add_paragraph()
    p_ack3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_ack3.paragraph_format.line_spacing = 1.3
    p_ack3.paragraph_format.space_after = Pt(10)
    r = p_ack3.add_run("We extend our deep gratitude to ")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p_ack3.add_run("Dr. Shameem Fatima, Assoc. Prof, AIML Dept,")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.bold = True
    r = p_ack3.add_run(" and our Internal Guide ")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r = p_ack3.add_run("[GUIDE NAME / Ms. SYEDA AZKIYA]")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.bold = True
    r = p_ack3.add_run(", for their earnest efforts, continuous mentorship, and timely suggestions that motivated us to complete this project work successfully.")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

    p_ack4 = doc.add_paragraph()
    p_ack4.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_ack4.paragraph_format.line_spacing = 1.3
    p_ack4.paragraph_format.space_after = Pt(28)
    r = p_ack4.add_run("Finally, we thank all the faculty members, lab instructors, non-teaching staff, and fellow students who directly or indirectly supported us in finishing our project work with precision.")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

    tbl_ack_names = doc.add_table(rows=2, cols=2)
    tbl_ack_names.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ack_names.rows[0].cells[0].text = "[STUDENT NAME 1]"
    tbl_ack_names.rows[0].cells[1].text = "[ROLL NUMBER 1]"
    tbl_ack_names.rows[1].cells[0].text = "[STUDENT NAME 2]"
    tbl_ack_names.rows[1].cells[1].text = "[ROLL NUMBER 2]"
    for row in tbl_ack_names.rows:
        row.cells[0].width = Inches(3.0)
        row.cells[1].width = Inches(2.5)
        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(11)
                run.font.bold = True

    # ==========================
    # 5. ABSTRACT & KEYWORDS
    # ==========================
    doc.add_page_break()
    p_abs_title = doc.add_paragraph()
    p_abs_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_abs_title.paragraph_format.space_before = Pt(24)
    p_abs_title.paragraph_format.space_after = Pt(16)
    r = p_abs_title.add_run("ABSTRACT")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    r.underline = True

    p_abs = doc.add_paragraph()
    p_abs.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_abs.paragraph_format.line_spacing = 1.35
    p_abs.paragraph_format.space_after = Pt(14)
    r = p_abs.add_run(
        "Attendance management in educational institutions remains a cornerstone of academic governance, yet traditional roll-call and paper-based sign-in sheets are notoriously time-consuming and vulnerable to proxy marking. Conventional digital solutions, such as static Quick Response (QR) codes or biometric fingerprint sensors, introduce critical drawbacks including QR screenshot sharing over messaging apps, high hardware costs, and classroom bottlenecks. To resolve these challenges, this project presents "
    )
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r_bold = p_abs.add_run("VERILOCK — SMART QR ATTENDANCE SYSTEM")
    r_bold.font.name = 'Times New Roman'
    r_bold.font.size = Pt(12)
    r_bold.bold = True
    r = p_abs.add_run(
        ", a lightweight, anti-proxy web application engineered with Python Flask, SQLite, and embedded machine learning. Verilock implements a dynamic QR rotation protocol wherein the instructor's live session screen displays a QR code encoding a cryptographically generated, ephemeral token that automatically expires every 8 seconds. Students authenticate into their personalized web portal, access their device camera via an HTML5 QR scanner (or utilize a fallback manual token entry), and submit the token in real time. The backend validates token freshness and session validity while enforcing strict database constraints to reject expired codes and eliminate duplicate markings. In addition to real-time attendance tracking and subject-wise metrics, Verilock integrates a supervised Logistic Regression model trained on synthetic semester attendance trajectories (2,000 student records, 84.35% training accuracy) utilizing early attendance percentage and temporal trajectory across the first 15 sessions. The model categorizes students into actionable risk tiers—Safe, Watch, and Critical—enabling proactive faculty intervention before students fall below the mandatory 75% institutional attendance threshold. Experimental evaluation confirms that Verilock delivers rapid sub-second verification, zero-hardware overhead, robust proxy resistance, and actionable academic risk intelligence."
    )
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)

    p_kw = doc.add_paragraph()
    p_kw.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_kw.paragraph_format.space_before = Pt(8)
    p_kw.paragraph_format.space_after = Pt(14)
    r_kw_title = p_kw.add_run("Keywords: ")
    r_kw_title.font.name = 'Times New Roman'
    r_kw_title.font.size = Pt(11.5)
    r_kw_title.bold = True
    r_kw_val = p_kw.add_run("Smart Attendance System, Dynamic QR Code, Anti-Proxy Attendance, Ephemeral Token, Python Flask, SQLite, HTML5-QRCode, Machine Learning, Logistic Regression, Attendance Risk Prediction.")
    r_kw_val.font.name = 'Times New Roman'
    r_kw_val.font.size = Pt(11.5)
    r_kw_val.italic = True

    # ==========================
    # 6. TABLE OF CONTENTS
    # ==========================
    doc.add_page_break()
    p_toc_title = doc.add_paragraph()
    p_toc_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_toc_title.paragraph_format.space_before = Pt(20)
    p_toc_title.paragraph_format.space_after = Pt(16)
    r = p_toc_title.add_run("TABLE OF CONTENTS")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    r.underline = True

    toc_items = [
        ("CERTIFICATE", "ii"),
        ("DECLARATION", "iii"),
        ("ACKNOWLEDGEMENT", "iv"),
        ("ABSTRACT", "v"),
        ("LIST OF FIGURES", "viii"),
        ("LIST OF TABLES", "ix"),
        ("1. INTRODUCTION", "1"),
        ("   1.1 Introduction and Background", "1"),
        ("   1.2 Objective", "3"),
        ("   1.3 Scope of the Project", "4"),
        ("   1.4 Technical Approach", "5"),
        ("   1.5 Organization of the Report", "6"),
        ("2. BACKGROUND CONCEPTS", "7"),
        ("   2.1 Introduction", "7"),
        ("   2.2 Attendance Management Systems and Anti-Proxy Challenges", "7"),
        ("   2.3 Dynamic QR Code Architecture and Ephemeral Tokens", "9"),
        ("   2.4 Web Framework and Relational Storage (Flask & SQLite)", "11"),
        ("   2.5 Machine Learning Concepts for Attendance Risk Prediction", "13"),
        ("   2.6 Chapter Conclusion", "16"),
        ("3. LITERATURE SURVEY", "17"),
        ("   3.1 Introduction", "17"),
        ("   3.2 Survey of Related Work", "17"),
        ("4. SYSTEM ANALYSIS AND DESIGN", "24"),
        ("   4.1 Existing System and Operational Bottlenecks", "24"),
        ("   4.2 Problem Statement", "25"),
        ("   4.3 Proposed Verilock System", "26"),
        ("   4.4 Project Modules", "27"),
        ("   4.5 Process Model Used With Justification (SDLC Waterfall / Umbrella Model)", "30"),
        ("   4.6 Software Requirement Specification (SRS)", "32"),
        ("   4.7 Feasibility Study (Technical, Operational, Economic)", "34"),
        ("   4.8 System Design and UML Modeling", "36"),
        ("5. ALGORITHMS AND TECHNIQUES", "46"),
        ("   5.1 Dynamic Token Generation Algorithm", "46"),
        ("   5.2 Ephemeral Token Expiration & Validation Algorithm", "47"),
        ("   5.3 Attendance Recording & Duplicate Prevention Algorithm", "49"),
        ("   5.4 Machine Learning: Logistic Regression for Student Risk Prediction", "50"),
        ("   5.5 Feature Engineering (Early Attendance Percentage & Trend Analysis)", "52"),
        ("   5.6 Synthetic Data Generation (Beta Reliability Distribution)", "54"),
        ("   5.7 Risk Categorization & Evaluation Parameters", "55"),
        ("6. EXPERIMENTAL RESULTS", "57"),
        ("   6.1 Introduction", "57"),
        ("   6.2 Operational Walkthrough and User Interface Screenshots", "58"),
        ("7. TESTING", "64"),
        ("   7.1 Introduction to Software Testing", "64"),
        ("   7.2 Testing Methodologies (Unit, Integration, System, Acceptance)", "64"),
        ("   7.3 Comprehensive Test Cases and Verification Results", "66"),
        ("8. CONCLUSION AND FUTURE ENHANCEMENT", "71"),
        ("   8.1 Conclusion", "71"),
        ("   8.2 Current Limitations", "72"),
        ("   8.3 Future Enhancements", "73"),
        ("REFERENCES", "75"),
        ("VIVA VOCE PREPARATION & QUESTIONS AND ANSWERS", "77"),
    ]

    tbl_toc = doc.add_table(rows=len(toc_items) + 1, cols=3)
    tbl_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_toc.rows[0].cells[0].text = "S.No."
    tbl_toc.rows[0].cells[1].text = "Description"
    tbl_toc.rows[0].cells[2].text = "Page No."
    for c in tbl_toc.rows[0].cells:
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)
            r.font.bold = True
    for i, (desc, pg) in enumerate(toc_items):
        row = tbl_toc.rows[i + 1]
        row.cells[0].text = str(i + 1)
        row.cells[1].text = desc
        row.cells[2].text = pg
        row.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row.cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for cell in row.cells:
            for r in cell.paragraphs[0].runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10)
    col_w = [Inches(0.8), Inches(4.5), Inches(1.2)]
    for row in tbl_toc.rows:
        for idx, w in enumerate(col_w):
            row.cells[idx].width = w

    # ==========================
    # 7. LIST OF FIGURES & TABLES
    # ==========================
    doc.add_page_break()
    p_lof_title = doc.add_paragraph()
    p_lof_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lof_title.paragraph_format.space_before = Pt(20)
    p_lof_title.paragraph_format.space_after = Pt(14)
    r = p_lof_title.add_run("LIST OF FIGURES")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.bold = True
    r.underline = True

    lof_items = [
        ("Figure 4.1", "SDLC Umbrella Model Lifecycle Stages", "31"),
        ("Figure 4.2", "System Architecture of Verilock Attendance Platform", "37"),
        ("Figure 4.3", "Use Case Diagram for Student and Faculty Actors", "38"),
        ("Figure 4.4", "Class Diagram Depicting System Entities and Methods", "39"),
        ("Figure 4.5", "Sequence Diagram for Dynamic Token Verification Flow", "41"),
        ("Figure 4.6", "Activity Diagram of Attendance Marking and Token Rotation", "42"),
        ("Figure 4.7", "Component Diagram Depicting Architectural Modules", "43"),
        ("Figure 4.8", "Deployment Diagram of Verilock Web Server and Database", "44"),
        ("Figure 4.9", "Data Flow Diagram (Level 0 Context Diagram)", "45"),
        ("Figure 4.10", "Data Flow Diagram (Level 1 Functional Data Flow)", "45"),
        ("Figure 4.11", "Entity-Relationship (E-R) Diagram for Database Schema", "46"),
        ("Figure 5.1", "Logistic Regression Sigmoid Hypothesis Curve", "51"),
        ("Figure 5.2", "Early Feature Extraction Window and Trend Division", "53"),
        ("Figure 6.1", "Verilock Landing / Home Page", "59"),
        ("Figure 6.2", "Student Login Interface", "60"),
        ("Figure 6.3", "Student Portal Dashboard with Subject Attendance and AI Risk Status", "62"),
    ]
    tbl_lof = doc.add_table(rows=len(lof_items) + 1, cols=3)
    tbl_lof.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_lof.rows[0].cells[0].text = "Fig No."
    tbl_lof.rows[0].cells[1].text = "Figure Caption"
    tbl_lof.rows[0].cells[2].text = "Page No."
    for c in tbl_lof.rows[0].cells:
        for r in c.paragraphs[0].runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)
            r.font.bold = True
    for i, (fno, cap, pg) in enumerate(lof_items):
        row = tbl_lof.rows[i + 1]
        row.cells[0].text = fno
        row.cells[1].text = cap
        row.cells[2].text = pg
        row.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row.cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for c in row.cells:
            for r in c.paragraphs[0].runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10)
    for row in tbl_lof.rows:
        for idx, w in enumerate([Inches(1.2), Inches(4.3), Inches(1.0)]):
            row.cells[idx].width = w

    p_lot_title = doc.add_paragraph()
    p_lot_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lot_title.paragraph_format.space_before = Pt(24)
    p_lot_title.paragraph_format.space_after = Pt(14)
    r = p_lot_title.add_run("LIST OF TABLES")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.bold = True
    r.underline = True

    lot_items = [
        ("Table 2.1", "Technology Stack Comparison in Verilock Implementation", "15"),
        ("Table 4.1", "Comparison Between Existing and Proposed Attendance Systems", "27"),
        ("Table 4.2", "Hardware Requirements Specification", "33"),
        ("Table 4.3", "Software Requirements Specification", "34"),
        ("Table 4.4", "Database Schema Data Dictionary for Verilock", "45"),
        ("Table 5.1", "Logistic Regression Confusion Matrix on 2000 Synthetic Records", "55"),
        ("Table 5.2", "Risk Classification Thresholds and Color Indicators", "56"),
        ("Table 7.1", "Comprehensive System Test Cases and Execution Results", "67"),
    ]
    tbl_lot = doc.add_table(rows=len(lot_items) + 1, cols=3)
    tbl_lot.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_lot.rows[0].cells[0].text = "Table No."
    tbl_lot.rows[0].cells[1].text = "Table Description"
    tbl_lot.rows[0].cells[2].text = "Page No."
    for c in tbl_lot.rows[0].cells:
        for r in c.paragraphs[0].runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)
            r.font.bold = True
    for i, (tno, desc, pg) in enumerate(lot_items):
        row = tbl_lot.rows[i + 1]
        row.cells[0].text = tno
        row.cells[1].text = desc
        row.cells[2].text = pg
        row.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row.cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for c in row.cells:
            for r in c.paragraphs[0].runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10)
    for row in tbl_lot.rows:
        for idx, w in enumerate([Inches(1.2), Inches(4.3), Inches(1.0)]):
            row.cells[idx].width = w

    print("Front matter generated.")
