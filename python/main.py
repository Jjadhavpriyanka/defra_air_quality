import pandas as pd 

from src.load_data import load_data
from src.preprocess import preprocess
from src.train_model import train_models
from src.forecast import forecast_model



def main():
    print("\nLoading data...\n\n")
    df = load_data("data/combined/bloomsbury_2019_2023.csv")
    df.info()

    print("\nPreprocessing...\n\n")
    df = preprocess(df)

    print("PM10 missing values:", df["PM10 particulate matter (Hourly measured)"].isna().sum())
    print("PM10 unique values:", df["PM10 particulate matter (Hourly measured)"].unique()[:10])

    print("\nTraining model...\n\n")
    results = train_models(df)

    #chose which model to forecast with
    model = results["random_forest"]

    print("\nMaking forecast...\n\n")
    next_pm10 = forecast_model(model, df)
    print("Next predicted PM10:", next_pm10)

if __name__ == "__main__":
    main()