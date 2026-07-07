import streamlit as st
from utils.style import setup_page,hero,section
setup_page("Giới thiệu")
hero("ℹ️ Giới thiệu đề tài","Từ tiểu luận OLS đến hệ thống hỗ trợ ra quyết định logistics")
section("Tên hệ thống"); st.write("FuelInsight AI – Hệ thống phân tích, dự báo giá dầu DO 0,05S-II và hỗ trợ quản trị chi phí logistics.")
section("Ý nghĩa"); st.write("Hệ thống giúp chuyển hóa kết quả nghiên cứu định lượng thành công cụ thực hành. Người dùng có thể xem dữ liệu, chạy mô hình, dự báo, phân tích chi phí và xuất báo cáo.")
section("Hướng phát triển"); st.write("- Kết nối dữ liệu tự động từ nguồn công khai."); st.write("- Bổ sung XGBoost, LSTM khi dữ liệu đủ dài."); st.write("- Thêm tài khoản người dùng, phân quyền và lưu lịch sử trên database."); st.write("- Tích hợp dashboard cho doanh nghiệp vận tải/logistics.")
