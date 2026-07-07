import pandas as pd
import statsmodels.api as sm
from utils.constants import DEFAULT_CONST,DEFAULT_BETA_CPI,DEFAULT_BETA_USD,DEFAULT_BETA_BRENT
def predict_default_ols(cpi,usd,brent): return DEFAULT_CONST+DEFAULT_BETA_CPI*cpi+DEFAULT_BETA_USD*usd+DEFAULT_BETA_BRENT*brent
def fit_ols(df): return sm.OLS(df["Gia_DO"],sm.add_constant(df[["CPI","USD_VND","Brent"]])).fit()
def ols_summary_table(model):
    rows=[]
    for name in model.params.index:
        rows.append({"Biến":name,"Hệ số":model.params[name],"t-stat":model.tvalues[name],"p-value":model.pvalues[name],"Kết luận":"Có ý nghĩa" if model.pvalues[name]<0.05 else "Chưa có ý nghĩa"})
    return pd.DataFrame(rows)
