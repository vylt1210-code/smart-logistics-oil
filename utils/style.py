import streamlit as st

def setup_page(title="FuelInsight AI"):
    st.set_page_config(page_title=title,page_icon="⛽",layout="wide")
    st.markdown("""
    <style>
    .block-container{padding-top:1.1rem;max-width:1250px}.hero{padding:30px;border-radius:30px;background:radial-gradient(circle at top right,rgba(14,165,233,.45),transparent 32%),linear-gradient(135deg,#020617,#0f172a 46%,#075985);color:white;margin-bottom:22px;box-shadow:0 18px 55px rgba(2,6,23,.22)}.hero h1{margin:0;font-size:42px;font-weight:950;letter-spacing:-.8px}.hero p{margin-top:9px;font-size:17px;opacity:.95}.metric-card{background:rgba(255,255,255,.96);border:1px solid #e5e7eb;padding:18px;border-radius:22px;box-shadow:0 10px 28px rgba(15,23,42,.08);margin-bottom:14px}.metric-label{color:#475569;font-weight:850;font-size:14px}.metric-value{color:#0f172a;font-size:30px;font-weight:950}.section-title{font-size:26px;font-weight:950;color:#0f172a;margin:18px 0 12px}.soft-card{background:white;padding:20px;border-radius:22px;border:1px solid #e2e8f0;box-shadow:0 8px 28px rgba(15,23,42,.06);margin-bottom:14px}
    </style>
    """,unsafe_allow_html=True)

def hero(title,subtitle):
    st.markdown(f"<div class='hero'><h1>{title}</h1><p>{subtitle}</p></div>",unsafe_allow_html=True)

def metric_card(label,value,icon="📌"):
    st.markdown(f"<div class='metric-card'><div class='metric-label'>{icon} {label}</div><div class='metric-value'>{value}</div></div>",unsafe_allow_html=True)

def section(title): st.markdown(f"<div class='section-title'>{title}</div>",unsafe_allow_html=True)
def soft_card(text): st.markdown(f"<div class='soft-card'>{text}</div>",unsafe_allow_html=True)
