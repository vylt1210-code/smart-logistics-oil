import streamlit as st
from datetime import datetime
import pandas as pd
from utils.style import setup_page, hero, section
from models.ols import predict_default_ols
from utils.risk import classify_risk
from utils.data import read_history, save_history
from utils.assets import show_banner

setup_page("Dự báo giá dầu")
hero("🔮 Dự báo giá dầu", "Nhập CPI, USD/VND và Brent để dự báo giá dầu DO 0,05S-II", ["Forecast", "Scenario", "Risk"])
show_banner("oil_forecast.jpg")

c1, c2, c3 = st.columns(3)
with c1:
    cpi = st.number_input("CPI", value=0.0340, step=0.001, format="%.4f")
with c2:
    usd_vnd = st.number_input("USD/VND", value=25300, step=100)
with c3:
    brent = st.number_input("Brent USD/thùng", value=82.0, step=1.0)

pred = predict_default_ols(cpi, usd_vnd, brent)
level, color, advice = classify_risk(pred, brent, usd_vnd)

st.metric("Giá dầu DO 0,05S-II dự báo", f"{pred:,.0f} VNĐ/lít")
if color == "red":
    st.error(f"{level}: {advice}")
elif color == "yellow":
    st.warning(f"{level}: {advice}")
else:
    st.success(f"{level}: {advice}")

note = st.text_input("Ghi chú cho lần dự báo", value="Dự báo thủ công")
if st.button("💾 Lưu lịch sử dự báo", use_container_width=True):
    his = read_history()
    new = pd.DataFrame([{
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "CPI": cpi,
        "USD_VND": usd_vnd,
        "Brent": brent,
        "OLS_Prediction": round(pred, 0),
        "Risk_Level": level,
        "Note": note
    }])
    save_history(pd.concat([his, new], ignore_index=True))
    st.success("Đã lưu lịch sử dự báo.")

section("Lịch sử dự báo")
st.dataframe(read_history(), use_container_width=True, hide_index=True)
