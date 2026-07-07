import streamlit as st
from utils.style import setup_page,hero,section
from models.ols import predict_default_ols
from utils.risk import classify_risk
setup_page("Cảnh báo rủi ro")
hero("⚠️ Cảnh báo rủi ro","Đánh giá mức rủi ro khi giá dầu, Brent hoặc tỷ giá biến động")
cpi=st.slider("CPI",0.000,0.080,0.034,0.001); usd=st.slider("USD/VND",22000,28000,25300,50); brent=st.slider("Brent USD/thùng",40,130,82,1)
price=predict_default_ols(cpi,usd,brent); level,color,advice=classify_risk(price,brent,usd)
st.metric("Giá dầu DO dự báo",f"{price:,.0f} VNĐ/lít")
if color=="red": st.error(f"{level}: {advice}")
elif color=="yellow": st.warning(f"{level}: {advice}")
else: st.success(f"{level}: {advice}")
section("Gợi ý quản trị")
st.write("- Thiết lập phụ phí nhiên liệu theo ngưỡng giá."); st.write("- Mô phỏng chi phí theo kịch bản Brent và USD/VND."); st.write("- Cập nhật dữ liệu sau mỗi kỳ điều hành giá."); st.write("- Khi rủi ro cao, rà soát hợp đồng vận tải dài hạn.")
