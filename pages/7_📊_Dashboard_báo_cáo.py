import streamlit as st
from utils.style import setup_page, hero, metric_card, section
from utils.sidebar import data_sidebar
from utils.constants import MODEL_R2_REFERENCE
from models.ols import predict_default_ols
from utils.export import to_excel_bytes, simple_pdf_report
from utils.charts import line_chart
from utils.assets import show_banner

setup_page("Dashboard & báo cáo")
hero("📊 Dashboard & báo cáo", "Tổng hợp KPI, sai lệch dự báo và xuất báo cáo", ["KPI", "Excel", "PDF"])
show_banner("report_export.jpg")

df, ok = data_sidebar()
if not ok:
    st.stop()

report = df.copy()
report["OLS_Du_Bao"] = predict_default_ols(report["CPI"], report["USD_VND"], report["Brent"])
report["Sai_Lech"] = report["Gia_DO"] - report["OLS_Du_Bao"]

c1, c2, c3, c4 = st.columns(4)
with c1:
    metric_card("Số quan sát", len(report), "📌")
with c2:
    metric_card("R² tham chiếu", f"{MODEL_R2_REFERENCE:.3f}", "✅")
with c3:
    metric_card("Sai lệch TB", f"{report['Sai_Lech'].abs().mean():,.0f}", "📉")
with c4:
    metric_card("Giá DO TB", f"{report['Gia_DO'].mean():,.0f}", "⛽")

section("Biểu đồ tổng hợp")
st.plotly_chart(line_chart(report, "Thang", ["Gia_DO", "OLS_Du_Bao"], "Giá thực tế và giá dự báo"), use_container_width=True)

section("Bảng báo cáo")
st.dataframe(report.round(2), use_container_width=True, hide_index=True)

excel = to_excel_bytes({"Report": report})
st.download_button(
    "⬇️ Tải Excel",
    data=excel,
    file_name="FuelInsight_Report.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

pdf_lines = [
    "FuelInsight AI v2.0",
    f"So quan sat: {len(report)}",
    f"R2 tham chieu: {MODEL_R2_REFERENCE}",
    f"Sai lech trung binh tuyet doi: {report['Sai_Lech'].abs().mean():,.0f} VND/lit",
    f"Gia DO trung binh: {report['Gia_DO'].mean():,.0f} VND/lit",
]
pdf = simple_pdf_report("FuelInsight AI Report", pdf_lines)
st.download_button(
    "⬇️ Tải PDF tóm tắt",
    data=pdf,
    file_name="FuelInsight_Summary.pdf",
    mime="application/pdf"
)
