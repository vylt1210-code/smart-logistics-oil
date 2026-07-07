import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

# Optional ML libraries
try:
    import statsmodels.api as sm
except Exception:
    sm = None

try:
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, r2_score
except Exception:
    RandomForestRegressor = None

st.set_page_config(
    page_title="FuelInsight AI",
    page_icon="⛽",
    layout="wide"
)

# =========================
# DEFAULT OLS COEFFICIENTS
# =========================
CONST = -10270
BETA_CPI = 67590
BETA_USD = 0.5234
BETA_BRENT = 188.8192
MODEL_R2 = 0.921

# =========================
# STYLE
# =========================
st.markdown("""
<style>
.block-container {padding-top: 1rem; max-width: 1200px;}
.hero {
    padding: 26px;
    border-radius: 24px;
    background: linear-gradient(135deg, #0f172a, #0369a1, #0ea5e9);
    color: white;
    margin-bottom: 20px;
}
.hero h1 {margin: 0; font-size: 38px; font-weight: 900;}
.hero p {margin-top: 8px; font-size: 17px;}
.card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0 8px 24px rgba(15,23,42,.08);
}
</style>
""", unsafe_allow_html=True)

# =========================
# FUNCTIONS
# =========================
def predict_ols(cpi, usd_vnd, brent):
    return CONST + BETA_CPI * cpi + BETA_USD * usd_vnd + BETA_BRENT * brent

def make_sample_data():
    months = pd.date_range("2020-01-01", periods=72, freq="MS")
    np.random.seed(14)
    brent = np.linspace(45, 85, 72) + np.random.normal(0, 8, 72)
    usd = np.linspace(23200, 25300, 72) + np.random.normal(0, 250, 72)
    cpi = np.random.normal(0.035, 0.012, 72)
    do = CONST + BETA_CPI*cpi + BETA_USD*usd + BETA_BRENT*brent + np.random.normal(0, 900, 72)
    return pd.DataFrame({
        "Thang": months.strftime("%Y-%m"),
        "CPI": cpi,
        "USD_VND": usd.round(0),
        "Brent": brent.round(2),
        "Gia_DO": do.round(0)
    })

def normalize_columns(df):
    rename_map = {}
    for col in df.columns:
        c = col.strip().lower()
        if c in ["tháng", "thang", "month", "date", "ngay"]:
            rename_map[col] = "Thang"
        elif c in ["cpi"]:
            rename_map[col] = "CPI"
        elif c in ["usd_vnd", "usd/vnd", "ty_gia", "tỷ giá", "ty gia"]:
            rename_map[col] = "USD_VND"
        elif c in ["brent", "gia_brent", "giá brent", "gia dau brent"]:
            rename_map[col] = "Brent"
        elif c in ["gia_do", "giá do", "gia dau do", "gia_do_005s_ii", "do"]:
            rename_map[col] = "Gia_DO"
    return df.rename(columns=rename_map)

def to_excel_bytes(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Report")
    return output.getvalue()

def risk_level(predicted_price, brent, usd_vnd):
    if predicted_price >= 26000 or brent >= 95 or usd_vnd >= 26000:
        return "RỦI RO CAO", "Giá dầu/tỷ giá đang ở vùng cần cảnh báo. Doanh nghiệp nên rà soát giá cước và kế hoạch nhiên liệu."
    if predicted_price >= 23000 or brent >= 85 or usd_vnd >= 25500:
        return "RỦI RO TRUNG BÌNH", "Cần theo dõi biến động Brent và USD/VND, chuẩn bị kịch bản tăng chi phí."
    return "RỦI RO THẤP", "Biến động hiện tại tương đối ổn định, tiếp tục theo dõi định kỳ."

# =========================
# SIDEBAR
# =========================
st.sidebar.title("⛽ FuelInsight AI")
page = st.sidebar.radio(
    "Điều hướng",
    [
        "🏠 Trang chủ",
        "📈 Phân tích dữ liệu",
        "🔮 Dự báo giá dầu",
        "🚛 Chi phí logistics",
        "⚠️ Cảnh báo rủi ro",
        "📊 Dashboard & báo cáo"
    ]
)

uploaded = st.sidebar.file_uploader("Tải dataset CSV/Excel", type=["csv", "xlsx"])

if uploaded:
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)
    df = normalize_columns(df)
else:
    df = make_sample_data()

required_cols = ["CPI", "USD_VND", "Brent", "Gia_DO"]
has_data = all(c in df.columns for c in required_cols)

# =========================
# HEADER
# =========================
st.markdown("""
<div class='hero'>
<h1>FuelInsight AI</h1>
<p>Hệ thống phân tích, dự báo giá dầu DO 0,05S-II và hỗ trợ quản trị chi phí logistics</p>
</div>
""", unsafe_allow_html=True)

# =========================
# PAGES
# =========================
if page == "🏠 Trang chủ":
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Mô hình", "OLS")
    c2.metric("Biến độc lập", "3")
    c3.metric("R² tham chiếu", f"{MODEL_R2:.3f}")
    c4.metric("Dữ liệu", f"{len(df)} dòng")

    st.subheader("Mục tiêu hệ thống")
    st.write("""
    Ứng dụng này phát triển từ đề tài hồi quy giá dầu DO 0,05S-II.
    Hệ thống giúp phân tích dữ liệu, dự báo giá dầu, ước tính chi phí logistics,
    cảnh báo rủi ro biến động nhiên liệu và xuất báo cáo quản trị.
    """)

    st.subheader("5 module chính")
    st.write("📈 Phân tích dữ liệu • 🔮 Dự báo OLS/ML • 🚛 Chi phí logistics • ⚠️ Cảnh báo rủi ro • 📊 Dashboard & báo cáo")

elif page == "📈 Phân tích dữ liệu":
    st.subheader("📈 Phân tích dữ liệu")

    if not has_data:
        st.error("Dataset cần có cột: CPI, USD_VND, Brent, Gia_DO")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.subheader("Thống kê mô tả")
        st.dataframe(df[required_cols].describe().T, use_container_width=True)

        st.subheader("Biểu đồ xu hướng")
        chart_cols = st.multiselect("Chọn biến hiển thị", required_cols, default=["Gia_DO", "Brent"])
        if chart_cols:
            st.line_chart(df[chart_cols])

        st.subheader("Ma trận tương quan")
        st.dataframe(df[required_cols].corr().round(3), use_container_width=True)

elif page == "🔮 Dự báo giá dầu":
    st.subheader("🔮 Dự báo giá dầu DO 0,05S-II")

    cpi = st.number_input("CPI", value=0.0340, step=0.001, format="%.4f")
    usd_vnd = st.number_input("USD/VND", value=25300, step=100)
    brent = st.number_input("Brent USD/thùng", value=82.0, step=1.0)

    predicted = predict_ols(cpi, usd_vnd, brent)

    c1, c2 = st.columns([1, 1])
    with c1:
        st.metric("Giá dầu DO dự báo", f"{predicted:,.0f} VNĐ/lít")
        st.caption("Công thức: DO = β0 + β1*CPI + β2*USD/VND + β3*Brent")

    with c2:
        impact = pd.DataFrame({
            "Yếu tố": ["CPI", "USD/VND", "Brent"],
            "Tác động": [BETA_CPI*cpi, BETA_USD*usd_vnd, BETA_BRENT*brent]
        })
        st.dataframe(impact, use_container_width=True, hide_index=True)
        st.bar_chart(impact.set_index("Yếu tố"))

    st.subheader("So sánh mô hình sau này")
    if RandomForestRegressor and has_data and len(df) >= 20:
        X = df[["CPI", "USD_VND", "Brent"]]
        y = df["Gia_DO"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=14)
        rf = RandomForestRegressor(n_estimators=150, random_state=14)
        rf.fit(X_train, y_train)
        rf_pred = rf.predict([[cpi, usd_vnd, brent]])[0]
        test_pred = rf.predict(X_test)

        m1, m2, m3 = st.columns(3)
        m1.metric("OLS dự báo", f"{predicted:,.0f}")
        m2.metric("Random Forest dự báo", f"{rf_pred:,.0f}")
        m3.metric("RF R² test", f"{r2_score(y_test, test_pred):.3f}")
    else:
        st.info("Có thể thêm Random Forest, XGBoost, LSTM khi dataset thật đầy đủ hơn.")

elif page == "🚛 Chi phí logistics":
    st.subheader("🚛 Ước tính chi phí logistics")

    cpi = st.number_input("CPI dự báo", value=0.0340, step=0.001, format="%.4f")
    usd_vnd = st.number_input("USD/VND dự báo", value=25300, step=100)
    brent = st.number_input("Brent dự báo", value=82.0, step=1.0)

    price = predict_ols(cpi, usd_vnd, brent)

    vehicles = st.number_input("Số xe", min_value=1, value=10)
    km_day = st.number_input("Km/xe/ngày", min_value=1, value=180)
    liter_per_km = st.number_input("Lít/km", min_value=0.01, value=0.28, step=0.01)
    days = st.number_input("Số ngày vận hành/tháng", min_value=1, value=26)

    monthly_liters = vehicles * km_day * liter_per_km * days
    monthly_cost = monthly_liters * price

    c1, c2, c3 = st.columns(3)
    c1.metric("Giá dầu dự báo", f"{price:,.0f} VNĐ/lít")
    c2.metric("Nhiên liệu/tháng", f"{monthly_liters:,.0f} lít")
    c3.metric("Chi phí/tháng", f"{monthly_cost:,.0f} VNĐ")

    scenario = pd.DataFrame({
        "Kịch bản": ["Hiện tại", "Tăng 5%", "Tăng 10%", "Tăng 15%"],
        "Giá dầu": [price, price*1.05, price*1.10, price*1.15],
    })
    scenario["Chi phí tháng"] = scenario["Giá dầu"] * monthly_liters
    scenario["Chi phí tăng thêm"] = scenario["Chi phí tháng"] - monthly_cost

    st.subheader("Kịch bản biến động chi phí")
    st.dataframe(scenario.round(0), use_container_width=True, hide_index=True)

elif page == "⚠️ Cảnh báo rủi ro":
    st.subheader("⚠️ Cảnh báo rủi ro")

    cpi = st.slider("CPI", 0.000, 0.080, 0.034, 0.001)
    usd_vnd = st.slider("USD/VND", 22000, 28000, 25300, 50)
    brent = st.slider("Brent", 40, 130, 82, 1)

    price = predict_ols(cpi, usd_vnd, brent)
    level, advice = risk_level(price, brent, usd_vnd)

    st.metric("Giá dầu DO dự báo", f"{price:,.0f} VNĐ/lít")
    if "CAO" in level:
        st.error(f"{level}: {advice}")
    elif "TRUNG" in level:
        st.warning(f"{level}: {advice}")
    else:
        st.success(f"{level}: {advice}")

    st.subheader("Gợi ý quản trị")
    st.write("""
    - Doanh nghiệp vận tải nên xây dựng phụ phí nhiên liệu theo ngưỡng giá.
    - Doanh nghiệp logistics nên mô phỏng chi phí theo từng kịch bản Brent và USD/VND.
    - Nhà quản trị nên cập nhật mô hình sau mỗi kỳ điều hành giá để giảm sai lệch dự báo.
    """)

elif page == "📊 Dashboard & báo cáo":
    st.subheader("📊 Dashboard quản trị & xuất báo cáo")

    latest = df.iloc[-1] if has_data else None
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Số quan sát", len(df))
    c2.metric("R² mô hình", f"{MODEL_R2:.3f}")
    c3.metric("Biến đầu vào", "CPI, USD, Brent")
    c4.metric("Mục tiêu", "DO 0,05S-II")

    if has_data:
        st.line_chart(df[["Gia_DO", "Brent"]])

        report = df.copy()
        report["OLS_Du_Bao"] = predict_ols(report["CPI"], report["USD_VND"], report["Brent"])
        report["Sai_Lech"] = report["Gia_DO"] - report["OLS_Du_Bao"]

        st.subheader("Báo cáo sai lệch dự báo")
        st.dataframe(report, use_container_width=True, hide_index=True)

        st.download_button(
            "⬇️ Tải báo cáo Excel",
            data=to_excel_bytes(report),
            file_name="FuelInsight_Report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.error("Chưa đủ dữ liệu để xuất báo cáo.")
