import streamlit as st
import pandas as pd
from utils.style import setup_page,hero,section
from models.ols import predict_default_ols
from utils.charts import bar_chart
setup_page("Chi phí logistics")
hero("🚛 Ước tính chi phí logistics","Tính chi phí nhiên liệu và mô phỏng kịch bản tăng giá dầu")
c1,c2,c3=st.columns(3)
with c1: cpi=st.number_input("CPI dự báo",value=0.0340,step=0.001,format="%.4f")
with c2: usd=st.number_input("USD/VND dự báo",value=25300,step=100)
with c3: brent=st.number_input("Brent dự báo",value=82.0,step=1.0)
price=predict_default_ols(cpi,usd,brent)
v1,v2,v3,v4=st.columns(4)
with v1: vehicles=st.number_input("Số xe",min_value=1,value=10)
with v2: km_day=st.number_input("Km/xe/ngày",min_value=1,value=180)
with v3: liter_per_km=st.number_input("Lít/km",min_value=0.01,value=0.28,step=0.01)
with v4: days=st.number_input("Ngày vận hành/tháng",min_value=1,value=26)
monthly_liters=vehicles*km_day*liter_per_km*days; monthly_cost=monthly_liters*price
m1,m2,m3=st.columns(3); m1.metric("Giá dầu dự báo",f"{price:,.0f} VNĐ/lít"); m2.metric("Nhiên liệu/tháng",f"{monthly_liters:,.0f} lít"); m3.metric("Chi phí/tháng",f"{monthly_cost:,.0f} VNĐ")
scenario=pd.DataFrame({"Kịch bản":["Hiện tại","Tăng 5%","Tăng 10%","Tăng 15%","Tăng 20%"],"Giá dầu":[price,price*1.05,price*1.10,price*1.15,price*1.20]})
scenario["Chi phí tháng"]=scenario["Giá dầu"]*monthly_liters; scenario["Chi phí tăng thêm"]=scenario["Chi phí tháng"]-monthly_cost
section("Kịch bản biến động chi phí"); st.dataframe(scenario.round(0),use_container_width=True,hide_index=True); st.plotly_chart(bar_chart(scenario,"Kịch bản","Chi phí tháng","Chi phí nhiên liệu theo kịch bản"),use_container_width=True)
