from pathlib import Path
import pandas as pd
from utils.constants import REQUIRED_COLS
DATA_PATH=Path(__file__).resolve().parents[1]/"data"/"fuel_data.csv"
HISTORY_PATH=Path(__file__).resolve().parents[1]/"data"/"prediction_history.csv"
def normalize_columns(df):
    m={}
    for col in df.columns:
        k=str(col).strip().lower()
        if k in ["thang","tháng","month","date","ngay","ngày"]:m[col]="Thang"
        elif k=="cpi":m[col]="CPI"
        elif k in ["usd_vnd","usd/vnd","ty_gia","tỷ giá","ty gia"]:m[col]="USD_VND"
        elif k in ["brent","gia_brent","giá brent","gia dau brent"]:m[col]="Brent"
        elif k in ["gia_do","giá do","gia do","gia_do_005s_ii","do"]:m[col]="Gia_DO"
    return df.rename(columns=m)
def load_default_data(): return pd.read_csv(DATA_PATH)
def load_uploaded_data(uploaded):
    if uploaded is None:return load_default_data()
    df=pd.read_csv(uploaded) if uploaded.name.endswith('.csv') else pd.read_excel(uploaded)
    return normalize_columns(df)
def validate_data(df):
    missing=[c for c in REQUIRED_COLS if c not in df.columns]
    return len(missing)==0,missing
def add_date_parts(df):
    out=df.copy(); out['Date']=pd.to_datetime(out.get('Thang'),errors='coerce'); out['Nam']=out['Date'].dt.year; out['Thang_so']=out['Date'].dt.month; return out
def read_history(): return pd.read_csv(HISTORY_PATH) if HISTORY_PATH.exists() else pd.DataFrame(columns=['created_at','CPI','USD_VND','Brent','OLS_Prediction','Risk_Level','Note'])
def save_history(df): df.to_csv(HISTORY_PATH,index=False,encoding='utf-8-sig')
