import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error



def train_models(df):
    #load cleaned dataset
    df = pd.read_csv("/Users/Tippie/Desktop/Computing Project/defra_air_quality/data/cleaned/bloomsbury_cleaned.csv")

    #defining target and features
    features = df.drop(columns=["PM10 particulate matter (Hourly measured)", "datetime"])
    target = df["PM10 particulate matter (Hourly measured)"]

    X = features
    y = target

    #train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    # Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr_preds = lr.predict(X_test)

    lr_r2 = r2_score(y_test, lr_preds)
    lr_rmse = np.sqrt(mean_squared_error(y_test, lr_preds))

    print("\n===Linear Regression Results ===")
    print(f"R2 Score: {lr_r2:.3f}")
    print(f"RMSE: {lr_rmse:.3f}")


    # Random Forest
    rf = RandomForestRegressor(
        n_estimators=300,
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42,
        n_jobs=-1
    )

    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test)
    
    rf_r2 = r2_score(y_test, rf_preds)
    rf_rmse = np.sqrt(mean_squared_error(y_test, rf_preds))

    print("\n=== Random Forest Results ===")
    print(f"R2 Score: {rf_r2:.3f}")
    print(f"RMSE: {rf_rmse:.3f}")

    #returning noth models and metrics
    return {
        "linear_model": lr,
        "random_forest": rf,
        "metrics": {
            "linear": {"r2":lr_r2, "rmse":lr_rmse},
            "random_forest": {"r2": rf_r2, "rmse": rf_rmse}
        }
    }