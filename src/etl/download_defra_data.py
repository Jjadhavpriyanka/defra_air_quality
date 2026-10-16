import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
import pandas as pd
import io
import os

# ensuring folder exists
os.makedirs("data/combined", exist_ok=True)

def download_year(year):
    url = f"https://uk-air.defra.gov.uk/datastore/data_files/site_data/CLL2_{year}.csv?v=1"
    print("\nDownload starting.....\n")
    print(f"Downloading {year} from {url}\n")

    response = requests.get(url, verify=False)
    lines = response.text.splitlines()

    # finding row the header starts
    header_index = None
    for i, line in enumerate(lines):
        if line.startswith("Date"):
            header_index = i
            break
    
    if header_index is None:
        raise ValueError(f"Could not find header row for year {year}")
    
    df = pd.read_csv(io.StringIO("\n".join(lines[header_index:])))
    df["year"] = year
    return df

def main():
    years = range(2019, 2024)
    dfs = []

    for y in years:
        df = download_year(y)
        dfs.append(df)

    combined = pd.concat(dfs, ignore_index=True)
    combined.to_csv("data/combined/bloomsbury_2019_2023.csv", index=False)
    print("Download completed!\n")
    print("Saved: data/combined/bloomsbury_2019_2023.csv")


if __name__  == "__main__":
    main()