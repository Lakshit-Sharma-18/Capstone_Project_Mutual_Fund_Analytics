import os
import requests
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA = os.path.join(BASE_DIR, "data", "raw")
DB_FOLDER = os.path.join(BASE_DIR, "data", "db")

os.makedirs(RAW_DATA, exist_ok=True)
os.makedirs(DB_FOLDER, exist_ok=True)

DB_PATH = os.path.join(DB_FOLDER, "bluestock_mf.db")

engine = create_engine(f"sqlite:///{DB_PATH}")

funds = {
    "hdfc_top_100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

total_records = 0

for fund_name, scheme_code in funds.items():

    print(f"\nFetching NAV data for {fund_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        if "data" not in data:
            print(f"No NAV data found for {fund_name}")
            continue

        df = pd.DataFrame(data["data"])

        df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

        df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

        df = df.drop_duplicates()

        df = df.dropna(subset=["nav"])

        df = df.sort_values("date")

        df.reset_index(drop=True, inplace=True)

        df["fund_name"] = fund_name
        df["scheme_code"] = scheme_code

        csv_file = os.path.join(RAW_DATA, f"{fund_name}.csv")

        df.to_csv(csv_file, index=False)

        df.to_sql(
            "live_nav_history",
            engine,
            if_exists="append",
            index=False
        )

        total_records += len(df)

        print(f"CSV Updated      : {fund_name}.csv")
        print(f"Database Updated : live_nav_history")
        print(f"Records Imported : {len(df)}")

    except Exception as e:

        print(f"Error fetching {fund_name}: {e}")

print("\n" + "=" * 60)
print("MFAPI ETL PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)
print(f"Funds Processed : {len(funds)}")
print(f"Records Loaded  : {total_records}")
print(f"Database        : {DB_PATH}")
print(f"CSV Folder      : {RAW_DATA}")