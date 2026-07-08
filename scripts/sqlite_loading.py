import os
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA = os.path.join(BASE_DIR, "data", "processed")
DB_FOLDER = os.path.join(BASE_DIR, "data", "db")

os.makedirs(DB_FOLDER, exist_ok=True)

DB_PATH = os.path.join(DB_FOLDER, "bluestock_mf.db")

engine = create_engine(f"sqlite:///{DB_PATH}")

funds_df = pd.read_csv(os.path.join(RAW_DATA, "01_fund_master.csv"))
facts_nav_df = pd.read_csv(os.path.join(PROCESSED_DATA, "nav_history_cleaned.csv"))
funds_trans_df = pd.read_csv(os.path.join(PROCESSED_DATA, "investor_transaction.csv"))
funds_perf_df = pd.read_csv(os.path.join(PROCESSED_DATA, "scheme_performance.csv"))
funds_aum_df = pd.read_csv(os.path.join(RAW_DATA, "03_aum_by_fund_house.csv"))
fact_sip_df = pd.read_csv(os.path.join(RAW_DATA, "04_monthly_sip_inflows.csv"))

date_df = pd.DataFrame()

date_df["date"] = pd.to_datetime(facts_nav_df["date"].unique())
date_df["year"] = date_df["date"].dt.year
date_df["month"] = date_df["date"].dt.month
date_df["day"] = date_df["date"].dt.day
date_df["quarter"] = date_df["date"].dt.quarter
date_df["day_name"] = date_df["date"].dt.day_name()

funds_df.to_sql("dim_fund", engine, if_exists="replace", index=False)
facts_nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)
funds_trans_df.to_sql("fact_transactions", engine, if_exists="replace", index=False)
funds_perf_df.to_sql("fact_performance", engine, if_exists="replace", index=False)
funds_aum_df.to_sql("fact_aum", engine, if_exists="replace", index=False)
date_df.to_sql("dim_date", engine, if_exists="replace", index=False)
fact_sip_df.to_sql("fact_sip_inflows", engine, if_exists="replace", index=False)

print(f"Rows in dim_fund CSV file: {len(funds_df)}")
print(f"Rows in dim_date CSV file: {len(date_df)}")
print(f"Rows in fact_nav CSV file: {len(facts_nav_df)}")
print(f"Rows in fact_transactions CSV file: {len(funds_trans_df)}")
print(f"Rows in fact_performance CSV file: {len(funds_perf_df)}")
print(f"Rows in fact_aum CSV file: {len(funds_aum_df)}")
print(f"Rows in fact_sip_inflows CSV file: {len(fact_sip_df)}")

print(pd.read_sql("SELECT COUNT(*) AS dim_fund FROM dim_fund", engine))
print(pd.read_sql("SELECT COUNT(*) AS dim_date FROM dim_date", engine))
print(pd.read_sql("SELECT COUNT(*) AS fact_nav FROM fact_nav", engine))
print(pd.read_sql("SELECT COUNT(*) AS fact_transactions FROM fact_transactions", engine))
print(pd.read_sql("SELECT COUNT(*) AS fact_performance FROM fact_performance", engine))
print(pd.read_sql("SELECT COUNT(*) AS fact_aum FROM fact_aum", engine))
print(pd.read_sql("SELECT COUNT(*) AS fact_sip_inflows FROM fact_sip_inflows", engine))

print(DB_PATH)