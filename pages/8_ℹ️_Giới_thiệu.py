import streamlit as st
from utils.style import setup_page, hero, section
from utils.assets import show_banner, image_card

setup_page("Giới thiệu")
hero("ℹ️ Giới thiệu đề tài", "Từ tiểu luận OLS đến hệ thống hỗ trợ ra quyết định logistics", ["Research", "Smart Logistics", "Decision Support"])
show_banner("research_team.jpg")

section("Tên hệ thống")
st.write("FuelInsight AI – Hệ thống phân tích, dự báo giá dầu DO 0,05S-II và hỗ trợ quản trị chi phí logistics.")

section("Nền tảng nghiên cứu")
a, b, c = st.columns(3)
with a:
    image_card("oil_refinery.jpg", "Dầu DO 0,05S-II", "Nhiên liệu quan trọng cho vận tải, logistics và sản xuất.")
with b:
    image_card("brent_market.jpg", "Thị trường Brent", "Biến động giá dầu thế giới truyền dẫn vào thị trường nội địa.")
with c:
    image_card("currency_exchange.jpg", "Tỷ giá USD/VND", "Tỷ giá ảnh hưởng đến chi phí nhập khẩu nhiên liệu.")

section("Ý nghĩa")
st.write(
    '''
    Hệ thống giúp chuyển hóa kết quả nghiên cứu định lượng thành công cụ thực hành.
    Người dùng không cần thao tác Python vẫn có thể xem dữ liệu, chạy mô hình, dự báo,
    phân tích chi phí và xuất báo cáo.
    '''
)

section("Hướng phát triển")
st.write("- Kết nối dữ liệu tự động từ nguồn công khai.")
st.write("- Bổ sung XGBoost, LSTM khi dữ liệu đủ dài.")
st.write("- Thêm tài khoản người dùng, phân quyền và lưu lịch sử trên database.")
st.write("- Tích hợp dashboard cho doanh nghiệp vận tải/logistics.")
