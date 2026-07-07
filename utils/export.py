from io import BytesIO
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def to_excel_bytes(sheets: dict):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        for name, df in sheets.items():
            df.to_excel(writer, index=False, sheet_name=name[:31])
    return output.getvalue()

def simple_pdf_report(title, lines):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 60
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, title)
    y -= 35
    c.setFont("Helvetica", 11)
    for line in lines:
        if y < 60:
            c.showPage()
            y = height - 60
            c.setFont("Helvetica", 11)
        c.drawString(50, y, str(line)[:95])
        y -= 20
    c.save()
    buffer.seek(0)
    return buffer.getvalue()
