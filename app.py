import streamlit as st
from utils.style import setup_page, hero, metric_card, section, soft_card
from utils.constants import SUBTITLE, MODEL_R2_REFERENCE
from utils.assets import show_logo, show_banner, image_card

setup_page("FuelInsight AI v2.0")
show_logo()

hero(
    "⛽ FuelInsight AI v2.0",
    SUBTITLE,
    chips=["OLS", "Machine Learning", "Logistics Cost", "Risk Alert", "Research Dashboard"]
)

show_banner("hero_fuel_ai.jpg")

c1, c2, c3, c4 = st.columns(4)
with c1:
    metric_card("Mô hình lõi", "OLS", "📐")
with c2:
    metric_card("Biến đầu vào", "3", "📊")
with c3:
    metric_card("R² tham chiếu", f"{MODEL_R2_REFERENCE:.3f}", "✅")
with c4:
    metric_card("Ứng dụng", "Logistics", "🚛")

section("🎯 Mục tiêu hệ thống")
st.write(
    '''
    FuelInsight AI v2.0 chuyển hóa bài nghiên cứu hồi quy giá dầu DO 0,05S-II thành một website
    phân tích dữ liệu và hỗ trợ ra quyết định cho doanh nghiệp logistics. Hệ thống có thể dùng để
    trình bày nghiên cứu, demo sản phẩm hoặc phát triển tiếp thành đồ án/NCKH.
    '''
)

section("🧩 Module chức năng")
col1, col2, col3 = st.columns(3)
with col1:
    image_card("data_analytics.jpg", "Phân tích dữ liệu", "Biểu đồ xu hướng, thống kê mô tả và ma trận tương quan.")
    image_card("oil_forecast.jpg", "Dự báo giá dầu", "Dự báo giá dầu DO 0,05S-II bằng OLS và mô hình học máy.")
with col2:
    image_card("dashboard_overview.jpg", "Dashboard quản trị", "KPI, sai lệch dự báo và báo cáo quản trị.")
    image_card("logistics_truck.jpg", "Chi phí logistics", "Mô phỏng chi phí nhiên liệu theo đội xe và kịch bản tăng giá.")
with col3:
    image_card("risk_alert.jpg", "Cảnh báo rủi ro", "Phân loại rủi ro theo giá dầu, Brent và tỷ giá.")
    image_card("report_export.jpg", "Xuất báo cáo", "Xuất Excel và PDF phục vụ trình bày nghiên cứu.")

section("🌍 Bối cảnh nghiên cứu")
a, b, c = st.columns(3)
with a:
    image_card("oil_refinery.jpg", "Dầu DO 0,05S-II", "Nhiên liệu quan trọng cho vận tải, logistics và sản xuất.")
with b:
    image_card("brent_market.jpg", "Giá dầu Brent", "Biến thượng nguồn có ảnh hưởng mạnh đến giá dầu trong nước.")
with c:
    image_card("currency_exchange.jpg", "USD/VND", "Tỷ giá tác động đến chi phí nhập khẩu nhiên liệu.")

section("🚀 Hướng dẫn")
st.info("Dùng menu bên trái để mở từng trang. Dataset mẫu đã có sẵn trong thư mục data/fuel_data.csv.")
