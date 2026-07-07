import streamlit as st
from utils.style import setup_page, hero, section
from utils.sidebar import data_sidebar
from models.ml import train_ml_models
from models.ols import predict_default_ols
from utils.assets import show_banner

setup_page("Machine Learning")
hero("🤖 Machine Learning", "So sánh Random Forest và Gradient Boosting với OLS", ["Random Forest", "Gradient Boosting", "Future LSTM"])
show_banner("dashboard_overview.jpg")

df, ok = data_sidebar()
if not ok:
    st.stop()

models, results = train_ml_models(df)

section("Bảng đánh giá mô hình")
st.dataframe(results.round(3), use_container_width=True, hide_index=True)
st.bar_chart(results.set_index("Mô hình")[["R²"]])

section("Dự báo thử")
cpi = st.number_input("CPI", value=0.0340, step=0.001, format="%.4f")
usd_vnd = st.number_input("USD/VND", value=25300, step=100)
brent = st.number_input("Brent", value=82.0, step=1.0)

input_row = [[cpi, usd_vnd, brent]]
ols_pred = predict_default_ols(cpi, usd_vnd, brent)

preds = {"OLS": ols_pred}
for name, model in models.items():
    preds[name] = model.predict(input_row)[0]

st.dataframe(
    [{"Mô hình": k, "Dự báo VNĐ/lít": round(v, 0)} for k, v in preds.items()],
    use_container_width=True,
    hide_index=True
)

st.info("LSTM nên thêm sau khi có dữ liệu dài hơn theo ngày/tuần; dữ liệu tháng 72 quan sát còn khá ngắn.")
