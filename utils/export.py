from io import BytesIO
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
def to_excel_bytes(sheets):
    out=BytesIO()
    with pd.ExcelWriter(out,engine="xlsxwriter") as writer:
        for name,df in sheets.items(): df.to_excel(writer,index=False,sheet_name=name[:31])
    return out.getvalue()
def simple_pdf_report(title,lines):
    b=BytesIO(); c=canvas.Canvas(b,pagesize=A4); w,h=A4; y=h-60
    c.setFont("Helvetica-Bold",16); c.drawString(50,y,title); y-=35; c.setFont("Helvetica",11)
    for line in lines:
        if y<60: c.showPage(); y=h-60; c.setFont("Helvetica",11)
        c.drawString(50,y,str(line)[:95]); y-=20
    c.save(); b.seek(0); return b.getvalue()
