import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
def train_ml_models(df):
    X=df[["CPI","USD_VND","Brent"]]; y=df["Gia_DO"]
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=14)
    models={"Random Forest":RandomForestRegressor(n_estimators=250,random_state=14),"Gradient Boosting":GradientBoostingRegressor(random_state=14)}
    rows=[]; trained={}
    for name,m in models.items():
        m.fit(Xtr,ytr); p=m.predict(Xte); trained[name]=m
        rows.append({"Mô hình":name,"R²":r2_score(yte,p),"MAE":mean_absolute_error(yte,p),"RMSE":mean_squared_error(yte,p)**0.5})
    return trained,pd.DataFrame(rows)
