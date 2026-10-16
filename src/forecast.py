import pandas as pd

def forecast_model(model, df):
    # getting last row
    last_row = df.iloc[-1]

    #loading cleaned dataset
    df = pd.read_csv("/Users/Tippie/Desktop/Computing Project/defra_air_quality/data/cleaned/bloomsbury_cleaned.csv")

    # extracting features
    X = df.drop(columns=["PM10 particulate matter (Hourly measured)", "datetime"])

    #predicting next hour PM10
    predicted_pm10 = model.predict([X.iloc[-1]])[0]

    #computing next timestamp
    next_timestamp = last_row["datetime"] + pd.Timedelta(hours=1)

    #Print message
    print("\n=== Forecast Summary ===")
    print(f"Last timestamp: {last_row["datetime"]}")
    print(f"Last actual PM10: {last_row["PM10 particulate matter (Hourly measured)"]:.2f}")
    print(f"Next timestamp: {next_timestamp}")
    print(f"Predicted next-hour PM10: {predicted_pm10:.2f}")


    return predicted_pm10