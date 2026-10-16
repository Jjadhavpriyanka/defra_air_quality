import pandas as pd


def load_data(path="../data/combined/bloomsbury_2019_2023.csv"):
    df = pd.read_csv(path)
    print("\n\nLoading data...\n\n")
    return df