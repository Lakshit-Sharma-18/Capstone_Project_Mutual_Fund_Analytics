import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///../data/db/bluestock_mf.db")


funds_df = pd.read_csv("../data/raw/01_fund_master.csv")
facts_nav_df = pd.read_csv("../data/processed/nav_history_cleaned.csv")
funds_trans_df = pd.read_csv("../data/processed/investor_transaction.csv")
funds_perf_df = pd.read_csv("../data/processed/scheme_performance.csv")
funds_aum_df = pd.read_csv("../data/raw/03_aum_by_fund_house.csv")
fact_sip_df = pd.read_csv("../data/raw/04_monthly_sip_inflows.csv")


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

print("Data loaded successfully!")