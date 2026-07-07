import streamlit as st
from utils.style import setup_page, hero, section
from utils.sidebar import data_sidebar
from utils.constants import REQUIRED_COLS
from utils.data import add_date_parts
from utils.charts import line_chart, corr_heatmap
from utils.assets import show_banner

setup_page("Phân tích dữ liệu")
hero("📈 Phân tích dữ liệu", "Khám phá CPI, USD/VND, Brent và giá dầu DO 0,05S-II", ["Data Analytics", "Correlation", "Trend"])
show_banner("data_analytics.jpg")

df, ok = data_sidebar()
if not ok:
    st.stop()

df = add_date_parts(df)

section("Bảng dữ liệu")
st.dataframe(df, use_container_width=True, hide_index=True)

section("Thống kê mô tả")
st.dataframe(df[REQUIRED_COLS].describe().T.round(3), use_container_width=True)

section("Biểu đồ xu hướng")
selected = st.multiselect("Chọn biến", REQUIRED_COLS, default=["Gia_DO", "Brent"])
if selected:
    st.plotly_chart(line_chart(df, "Thang", selected, "Xu hướng dữ liệu theo tháng"), use_container_width=True)

section("Ma trận tương quan")
corr = df[REQUIRED_COLS].corr().round(3)
st.plotly_chart(corr_heatmap(corr), use_container_width=True)
