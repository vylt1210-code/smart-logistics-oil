import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def train_ml_models(df):
    X = df[["CPI", "USD_VND", "Brent"]]
    y = df["Gia_DO"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=14)

    models = {
        "Random Forest": RandomForestRegressor(n_estimators=250, random_state=14),
        "Gradient Boosting": GradientBoostingRegressor(random_state=14),
    }

    results = []
    trained = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        trained[name] = model
        results.append({
            "Mô hình": name,
            "R²": r2_score(y_test, pred),
            "MAE": mean_absolute_error(y_test, pred),
            "RMSE": mean_squared_error(y_test, pred) ** 0.5
        })

    return trained, pd.DataFrame(results)
