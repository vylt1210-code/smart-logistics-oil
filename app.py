import streamlit as st
from utils.style import setup_page,hero,metric_card,section,soft_card
from utils.constants import SUBTITLE,MODEL_R2_REFERENCE
setup_page("FuelInsight AI v1.0")
hero("⛽ FuelInsight AI v1.0",SUBTITLE)
c1,c2,c3,c4=st.columns(4)
with c1: metric_card("Mô hình lõi","OLS","📐")
with c2: metric_card("Biến đầu vào","3","📊")
with c3: metric_card("R² tham chiếu",f"{MODEL_R2_REFERENCE:.3f}","✅")
with c4: metric_card("Ứng dụng","Logistics","🚛")
section("🎯 Mục tiêu hệ thống")
st.write("FuelInsight AI v1.0 chuyển hóa bài nghiên cứu hồi quy giá dầu DO 0,05S-II thành website phân tích dữ liệu và hỗ trợ ra quyết định cho doanh nghiệp logistics.")
section("🧩 Module chức năng")
col1,col2,col3=st.columns(3)
with col1:
    soft_card("<b>📈 Phân tích dữ liệu</b><br>Biểu đồ xu hướng, thống kê mô tả, tương quan.")
    soft_card("<b>🔮 Dự báo giá dầu</b><br>Dự báo bằng OLS và lưu lịch sử dự báo.")
with col2:
    soft_card("<b>🤖 Machine Learning</b><br>So sánh Random Forest và Gradient Boosting.")
    soft_card("<b>🚛 Chi phí logistics</b><br>Mô phỏng chi phí nhiên liệu theo kịch bản.")
with col3:
    soft_card("<b>⚠️ Cảnh báo rủi ro</b><br>Phân loại rủi ro theo giá dầu, Brent, tỷ giá.")
    soft_card("<b>📊 Báo cáo</b><br>Xuất Excel/PDF phục vụ quản trị.")
section("🚀 Hướng dẫn")
st.info("Dùng thanh menu bên trái để mở từng trang. Dataset mẫu đã có sẵn trong thư mục data/fuel_data.csv.")
