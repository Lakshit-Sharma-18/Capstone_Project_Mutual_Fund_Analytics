import os
import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "db", "bluestock_mf.db")

conn = sqlite3.connect(DB_PATH)

fund_df = pd.read_sql("SELECT * FROM dim_fund", conn)
performance_df = pd.read_sql("SELECT * FROM fact_performance", conn)
nav_df = pd.read_sql("SELECT * FROM fact_nav", conn)
aum_df = pd.read_sql("SELECT * FROM fact_aum", conn)

st.title("📈 Mutual Fund Analytics Dashboard")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Funds", len(fund_df))

if "one_year_return_pct" in performance_df.columns:
    avg_return = round(performance_df["one_year_return_pct"].mean(), 2)
    col2.metric("Average Return (%)", avg_return)

if "sharpe_ratio" in performance_df.columns:
    avg_sharpe = round(performance_df["sharpe_ratio"].mean(), 2)
    col3.metric("Average Sharpe", avg_sharpe)

if "aum_cr" in aum_df.columns:
    total_aum = round(aum_df["aum_cr"].sum(), 2)
    col4.metric("Total AUM (Cr)", total_aum)

st.markdown("---")

st.header("Fund Selection")

funds = fund_df["scheme_name"].tolist()

selected_fund = st.selectbox(
    "Choose a Mutual Fund",
    funds
)

st.markdown("---")

selected_nav = nav_df.merge(
    fund_df[["amfi_code", "scheme_name"]],
    on="amfi_code"
)

selected_nav = selected_nav[
    selected_nav["scheme_name"] == selected_fund
]

selected_nav["date"] = pd.to_datetime(selected_nav["date"])

selected_nav = selected_nav.sort_values("date")

fig = px.line(
    selected_nav,
    x="date",
    y="nav",
    title="NAV History"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.header("Performance Table")

st.dataframe(performance_df)

st.markdown("---")

st.header("Fund Master")

st.dataframe(fund_df)

conn.close()