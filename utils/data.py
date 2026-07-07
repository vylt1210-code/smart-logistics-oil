from pathlib import Path
import pandas as pd
import numpy as np
from utils.constants import REQUIRED_COLS, DEFAULT_CONST, DEFAULT_BETA_CPI, DEFAULT_BETA_USD, DEFAULT_BETA_BRENT

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "fuel_data.csv"
HISTORY_PATH = ROOT / "data" / "prediction_history.csv"

def ensure_sample_data():
    if DATA_PATH.exists():
        return
    np.random.seed(14)
    months = pd.date_range("2020-01-01", periods=72, freq="MS")
    brent = np.linspace(45, 85, 72) + np.random.normal(0, 8, 72)
    usd = np.linspace(23200, 25300, 72) + np.random.normal(0, 250, 72)
    cpi = np.random.normal(0.035, 0.012, 72)
    do = DEFAULT_CONST + DEFAULT_BETA_CPI*cpi + DEFAULT_BETA_USD*usd + DEFAULT_BETA_BRENT*brent + np.random.normal(0, 850, 72)
    df = pd.DataFrame({
        "Thang": months.strftime("%Y-%m"),
        "CPI": cpi.round(4),
        "USD_VND": usd.round(0).astype(int),
        "Brent": brent.round(2),
        "Gia_DO": do.round(0).astype(int),
    })
    DATA_PATH.parent.mkdir(exist_ok=True)
    df.to_csv(DATA_PATH, index=False, encoding="utf-8-sig")

def normalize_columns(df):
    rename_map = {}
    for col in df.columns:
        key = str(col).strip().lower()
        if key in ["thang", "tháng", "month", "date", "ngay", "ngày"]:
            rename_map[col] = "Thang"
        elif key == "cpi":
            rename_map[col] = "CPI"
        elif key in ["usd_vnd", "usd/vnd", "ty_gia", "tỷ giá", "ty gia", "exchange"]:
            rename_map[col] = "USD_VND"
        elif key in ["brent", "gia_brent", "giá brent", "gia dau brent"]:
            rename_map[col] = "Brent"
        elif key in ["gia_do", "gia dầu do", "giá do", "gia do", "gia_do_005s_ii", "do"]:
            rename_map[col] = "Gia_DO"
    return df.rename(columns=rename_map)

def load_default_data():
    ensure_sample_data()
    return pd.read_csv(DATA_PATH)

def load_uploaded_data(uploaded):
    if uploaded is None:
        return load_default_data()
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)
    return normalize_columns(df)

def validate_data(df):
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    return len(missing) == 0, missing

def add_date_parts(df):
    out = df.copy()
    if "Thang" in out.columns:
        out["Date"] = pd.to_datetime(out["Thang"], errors="coerce")
        out["Nam"] = out["Date"].dt.year
        out["Thang_so"] = out["Date"].dt.month
    return out

def read_history():
    if HISTORY_PATH.exists():
        return pd.read_csv(HISTORY_PATH)
    return pd.DataFrame(columns=["created_at","CPI","USD_VND","Brent","OLS_Prediction","Risk_Level","Note"])

def save_history(df):
    HISTORY_PATH.parent.mkdir(exist_ok=True)
    df.to_csv(HISTORY_PATH, index=False, encoding="utf-8-sig")
