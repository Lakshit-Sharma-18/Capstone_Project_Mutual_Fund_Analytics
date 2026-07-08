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
st.markdown("Interactive dashboard for analyzing mutual fund performance and NAV trends.")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Funds", len(fund_df))

if "return_1yr_pct" in performance_df.columns:
    col2.metric(
        "Average Return",
        f"{performance_df['return_1yr_pct'].mean():.2f}%"
    )

if "sharpe_ratio" in performance_df.columns:
    col3.metric(
        "Average Sharpe",
        f"{performance_df['sharpe_ratio'].mean():.2f}"
    )

if "aum_crore" in performance_df.columns:
    col4.metric(
        "Total AUM",
        f"{performance_df['aum_crore'].sum():,.0f} Cr"
    )

st.markdown("---")

left, right = st.columns(2)

selected_house = left.selectbox(
    "Select Fund House",
    sorted(fund_df["fund_house"].unique())
)

fund_list = sorted(
    fund_df[
        fund_df["fund_house"] == selected_house
    ]["scheme_name"]
)

selected_fund = right.selectbox(
    "Select Mutual Fund",
    fund_list
)

selected_nav = nav_df.merge(
    fund_df[["amfi_code", "scheme_name"]],
    on="amfi_code"
)

selected_nav = selected_nav[
    selected_nav["scheme_name"] == selected_fund
].copy()

selected_nav["date"] = pd.to_datetime(selected_nav["date"])
selected_nav = selected_nav.sort_values("date")

fig = px.line(
    selected_nav,
    x="date",
    y="nav",
    title=f"NAV Trend - {selected_fund}",
    labels={
        "date": "Date",
        "nav": "NAV (₹)"
    }
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.subheader("Performance Metrics")

selected_perf = performance_df[
    performance_df["scheme_name"] == selected_fund
]

st.dataframe(
    selected_perf,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

st.subheader("Fund Information")

selected_info = fund_df[
    fund_df["scheme_name"] == selected_fund
]

st.dataframe(
    selected_info,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

st.caption(
    "Developed by Lakshit Sharma | Bluestock Fintech Internship | Mutual Fund Analytics Dashboard"
)

conn.close()