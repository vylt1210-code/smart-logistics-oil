import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Fuel Forecast", layout="wide")

st.title("⛽ Smart Fuel Forecast")
st.caption("Dự báo giá dầu DO 0,05S-II dựa trên CPI, USD/VND và giá dầu Brent")

# Hệ số hồi quy từ bài của bạn
CONST = -10270
BETA_CPI = 67590
BETA_USD = 0.5234
BETA_BRENT = 188.8192

st.sidebar.header("Nhập dữ liệu dự báo")

cpi = st.sidebar.number_input("CPI", value=0.0340, step=0.001, format="%.4f")
usd_vnd = st.sidebar.number_input("Tỷ giá USD/VND", value=25300, step=100)
brent = st.sidebar.number_input("Giá dầu Brent USD/thùng", value=82.0, step=1.0)

predicted_price = CONST + BETA_CPI * cpi + BETA_USD * usd_vnd + BETA_BRENT * brent

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPI", f"{cpi:.4f}")

with col2:
    st.metric("USD/VND", f"{usd_vnd:,.0f}")

with col3:
    st.metric("Brent", f"{brent:.2f} USD/thùng")

st.markdown("---")

st.subheader("🔮 Kết quả dự báo")

st.metric(
    "Giá dầu DO 0,05S-II dự báo",
    f"{predicted_price:,.0f} đồng/lít"
)

st.info(
    "Mô hình dùng hồi quy tuyến tính đa biến OLS với 3 biến: CPI, tỷ giá USD/VND và giá dầu Brent."
)

st.subheader("📊 Mức đóng góp của từng yếu tố")

impact_df = pd.DataFrame({
    "Yếu tố": ["CPI", "USD/VND", "Brent"],
    "Tác động ước tính": [
        BETA_CPI * cpi,
        BETA_USD * usd_vnd,
        BETA_BRENT * brent
    ]
})

st.dataframe(impact_df, use_container_width=True, hide_index=True)

st.bar_chart(impact_df.set_index("Yếu tố"))

st.subheader("🧠 Nhận xét tự động")

strongest = impact_df.sort_values("Tác động ước tính", ascending=False).iloc[0]["Yếu tố"]

st.write(
    f"Yếu tố đang tác động mạnh nhất đến giá dầu dự báo là **{strongest}**. "
    "Nếu giá Brent hoặc tỷ giá USD/VND tăng, giá dầu DO trong nước có xu hướng tăng theo."
)