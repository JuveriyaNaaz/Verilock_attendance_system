# -*- coding: utf-8 -*-
"""
Script to generate the complete, comprehensive Word Document:
'Verilock_Mini_Project_Report.docx'
"""
import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_chapter_heading(doc, chapter_num, chapter_title):
    p1 = doc.add_paragraph()
    p1.paragraph_format.space_before = Pt(28)
    p1.paragraph_format.space_after = Pt(4)
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p1.add_run(f"CHAPTER {chapter_num}")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(16)
    r1.bold = True
    r1.font.color.rgb = RGBColor(0, 51, 102)

    p2 = doc.add_paragraph()
    p2.paragraph_format.space_before = Pt(2)
    p2.paragraph_format.space_after = Pt(18)
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run(chapter_title)
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(15)
    r2.bold = True
    r2.font.color.rgb = RGBColor(0, 51, 102)

def add_sec_heading(doc, sec_num, sec_title, level=2):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    if level == 2:
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(f"{sec_num}  {sec_title}")
        r.font.size = Pt(13)
        r.bold = True
        r.font.color.rgb = RGBColor(0, 51, 102)
    elif level == 3:
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(f"{sec_num}  {sec_title}")
        r.font.size = Pt(12)
        r.bold = True
        r.font.color.rgb = RGBColor(30, 41, 59)
    r.font.name = 'Times New Roman'
    return p

def add_body_p(doc, text, bold_prefix="", italic=False, space_after=6, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.3
    p.alignment = align
    if bold_prefix:
        r_bold = p.add_run(bold_prefix)
        r_bold.font.name = 'Times New Roman'
        r_bold.font.size = Pt(12)
        r_bold.bold = True
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.italic = italic
    return p

def add_bullet_p(doc, bold_title, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.25
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_title = p.add_run(bold_title)
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(12)
    r_title.bold = True
    r_text = p.add_run(text)
    r_text.font.name = 'Times New Roman'
    r_text.font.size = Pt(12)
    return p

def add_code_box(doc, code_str):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(code_str)
    run.font.name = 'Consolas'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(15, 23, 42)
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(6)

def add_styled_table(doc, col_widths, headers, data):
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Headers
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], "1E3A8A")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=80, right=80)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
            
    # Rows
    for row_idx, row_data in enumerate(data):
        row = table.rows[row_idx + 1]
        bg = "FFFFFF" if row_idx % 2 == 0 else "F8FAFC"
        for col_idx, cell_value in enumerate(row_data):
            cell = row.cells[col_idx]
            cell.text = str(cell_value)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.15
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(9.5)
                
    for row in table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width
            
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_after = Pt(6)
    return table

def add_figure_caption(doc, fig_num, caption_text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(12)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_label = p.add_run(f"Figure {fig_num}: ")
    r_label.font.name = 'Times New Roman'
    r_label.font.size = Pt(11)
    r_label.bold = True
    r_cap = p.add_run(caption_text)
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(11)
    r_cap.italic = True

def add_table_caption(doc, tbl_num, caption_text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_label = p.add_run(f"Table {tbl_num}: ")
    r_label.font.name = 'Times New Roman'
    r_label.font.size = Pt(11)
    r_label.bold = True
    r_cap = p.add_run(caption_text)
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(11)
    r_cap.italic = True

print("Make report helpers defined.")
