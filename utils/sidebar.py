import streamlit as st
from utils.data import load_uploaded_data, validate_data
def data_sidebar():
    st.sidebar.markdown("## ⛽ FuelInsight AI")
    uploaded=st.sidebar.file_uploader("Tải dataset CSV/Excel",type=["csv","xlsx"])
    df=load_uploaded_data(uploaded); ok,missing=validate_data(df)
    if ok: st.sidebar.success("Dữ liệu hợp lệ")
    else: st.sidebar.error("Thiếu cột: "+", ".join(missing))
    return df,ok
