import streamlit as st
from utils.data import load_uploaded_data, validate_data
from utils.assets import show_logo

def data_sidebar():
    show_logo()
    st.sidebar.markdown("## FuelInsight AI")
    uploaded = st.sidebar.file_uploader("Tải dataset CSV/Excel", type=["csv", "xlsx"])
    df = load_uploaded_data(uploaded)
    ok, missing = validate_data(df)
    if not ok:
        st.sidebar.error("Thiếu cột: " + ", ".join(missing))
    else:
        st.sidebar.success("Dữ liệu hợp lệ")
    return df, ok
