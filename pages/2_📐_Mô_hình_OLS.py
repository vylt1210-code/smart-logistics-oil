import streamlit as st
from utils.style import setup_page,hero,section,metric_card
from utils.sidebar import data_sidebar
from models.ols import fit_ols,ols_summary_table,predict_default_ols
from utils.charts import residual_chart
setup_page("Mô hình OLS")
hero("📐 Mô hình OLS","Ước lượng hồi quy tuyến tính đa biến và kiểm định mô hình")
df,ok=data_sidebar()
if not ok: st.stop()
model=fit_ols(df); summary=ols_summary_table(model)
c1,c2,c3,c4=st.columns(4)
with c1: metric_card("R²",f"{model.rsquared:.3f}","✅")
with c2: metric_card("Adjusted R²",f"{model.rsquared_adj:.3f}","📌")
with c3: metric_card("F p-value",f"{model.f_pvalue:.4f}","🧪")
with c4: metric_card("Quan sát",f"{int(model.nobs)}","📊")
section("Bảng hệ số hồi quy"); st.dataframe(summary.round(4),use_container_width=True,hide_index=True)
report=df.copy(); report["OLS_Du_Bao"]=predict_default_ols(report["CPI"],report["USD_VND"],report["Brent"]); report["Sai_Lech"]=report["Gia_DO"]-report["OLS_Du_Bao"]
section("Residual Plot"); st.plotly_chart(residual_chart(report),use_container_width=True)
with st.expander("Xem tóm tắt kỹ thuật từ statsmodels"): st.text(model.summary())
