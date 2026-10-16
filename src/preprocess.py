import pandas as pd
import numpy as np

# preprocess function
def preprocess(df):

    # Remove HTML tags
    df.columns= (
        df.columns.str.strip()
        .str.replace("<sub>", "", regex=False)
        .str.replace("</sub>", "", regex=False)
        )
    
    # create datetime column
    df["datetime"] = pd.to_datetime(df["Date"] + " " + df["time"], dayfirst=True, errors="coerce")
    df = df.drop(columns = ["Date", "time"])

    #convert pollutants to numeric
    for col in df.columns:
        if col not in ["datetime", "year"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    #dropping empty columns
    df = df.dropna(axis=1, how="all")

    #sorting by datetime
    df = df.sort_values("datetime").reset_index(drop=True)

    #dropping specific PM10/Pm2.5 columns(non-volatile and volatile)
    cols_to_drop = [
        "Non-volatile PM10 (Hourly measured)",
        "Volatile PM10 (Hourly measured)",
        "Non-volatile PM2.5 (Hourly measured)",
        "Volatile PM2.5 (Hourly measured)"
    ]
    df = df.drop(columns=cols_to_drop)

    #Filling missing pollutant values with forward fill
    pollutant_cols = ["PM10 particulate matter (Hourly measured)", "PM2.5 particulate matter (Hourly measured)", "Nitrogen dioxide", "Ozone", "Sulphur dioxide"]
    for col in pollutant_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    #dropping rows where PM10 is still missing
    df = df.dropna(subset=["PM10 particulate matter (Hourly measured)"])

    #dropping missing datetime
    df = df.dropna(subset=["datetime"])

    #interpolate pollutants
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.set_index("datetime")
    df = df.interpolate(method="time")

    # forward-fill missing pollutant values
    df = df.fillna(method="ffill")
    
    #resetting index
    df = df.reset_index()

    #feature engineering
    lag_cols = [
        "PM2.5 particulate matter (Hourly measured)",
        "Nitrogen dioxide",
        "Ozone"
    ]

    #lag features
    for col in lag_cols:
        df[col + "_lag1"] = df[col].shift(1)

    #rolling averages
    for col in lag_cols:
        df[col + "_roll3"] = df[col].rolling(window=3).mean()

    #temporal features
    df["month"] = df["datetime"].dt.month
    df["day_of_week"] = df["datetime"].dt.dayofweek

    #drop NaNs created by lag/rolling
    df = df.dropna()

    # saving cleaned dataset
    df.to_csv("/Users/Tippie/Desktop/Computing Project/defra_air_quality/data/cleaned/bloomsbury_cleaned.csv", index=False)
    print("file saved!")
    
    return df
