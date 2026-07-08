# 📈 Mutual Fund Analytics Capstone Project

> An end-to-end Mutual Fund Analytics platform built during the **Bluestock Fintech Internship**. The project automates mutual fund data collection, performs ETL operations, stores data in SQLite, computes financial performance metrics, and visualizes insights through an interactive Streamlit dashboard.

---

## 🚀 Project Overview

The objective of this project is to build a complete data analytics pipeline for mutual funds, starting from raw data collection to interactive visualization and portfolio optimization.

The project demonstrates industry-standard practices in:

- Data Engineering
- ETL Pipelines
- Database Design
- Financial Analytics
- Interactive Dashboard Development
- Cloud Deployment
- Portfolio Optimization

---

# ✨ Features

## 📥 Data Collection

- Fetches live NAV data using MFAPI
- Supports multiple mutual funds
- Error handling for failed API requests
- Automated CSV generation

---

## ⚙️ ETL Pipeline

- Data Extraction
- Data Cleaning
- Data Transformation
- Data Validation
- Data Loading

---

## 🗄 Database

SQLite database containing:

- `dim_fund`
- `fact_nav`
- `fact_performance`
- `fact_aum`

---

## 📊 Financial Metrics

The project computes several important financial indicators:

- CAGR
- 1-Year Return
- 3-Year Return
- 5-Year Return
- Alpha
- Beta
- Sharpe Ratio
- Sortino Ratio
- Volatility
- Maximum Drawdown
- Expense Ratio
- AUM

---

## 📈 Interactive Dashboard

Built using **Streamlit** and **Plotly**.

Features include:

- KPI Cards
- Fund Selection
- NAV History Chart
- Performance Table
- Fund Master Information
- Interactive Visualizations

---

# 🎯 Bonus Features

## ✅ Bonus 1 — Automated ETL Scheduling

Implemented automated NAV fetching using **Windows Task Scheduler**.

The ETL pipeline runs automatically every weekday at the scheduled time without manual intervention.

---

## ✅ Bonus 2 — Cloud Deployment

Successfully deployed the dashboard using **Streamlit Community Cloud**.

This allows users to access the dashboard directly from any browser.

---

## ✅ Bonus 3 — Fund Recommendation System

A recommendation engine that suggests mutual funds based on:

- Risk Appetite
- Sharpe Ratio
- Composite Score
- Maximum Drawdown

---

## ✅ Bonus 4 — Portfolio Optimizer

Implemented **Markowitz Portfolio Optimization**.

Features:

- Random Portfolio Simulation
- Efficient Frontier
- Maximum Sharpe Portfolio
- Optimal Asset Allocation
- Portfolio Risk Analysis
- Portfolio Return Analysis

---

# 📂 Project Structure

```text
Capstone_Project_Mutual_Fund_Analytics/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│
├── reports/
│
├── scripts/
│   ├── live_nav_fetch.py
│   ├── etl_pipeline.py
│   ├── sqlite_loading.py
│   ├── compute_metrics.py
│   ├── recommender.py
│   └── portfolio_optimizer.py
│
├── sql/
│
├── streamlit_app/
│   └── app.py
│
├── requirements.txt
│
└── README.md
```

---

# 🛠 Technology Stack

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Requests
- Plotly
- Streamlit

### Database

- SQLite

### Deployment

- Streamlit Community Cloud

### Version Control

- Git
- GitHub

---

# 🗃 Database Schema

## dim_fund

Stores fund master information.

Contains:

- AMFI Code
- Scheme Name
- Fund House
- Category
- Launch Date
- Benchmark
- Expense Ratio

---

## fact_nav

Stores historical NAV values.

Contains:

- Date
- NAV
- AMFI Code

---

## fact_performance

Stores calculated financial metrics.

Contains:

- Returns
- Alpha
- Beta
- Sharpe Ratio
- Sortino Ratio
- Volatility
- Drawdown
- Expense Ratio

---

## fact_aum

Stores Assets Under Management information.

---

# 📊 Dashboard Preview

The dashboard provides:

- 📈 Total Funds
- 📈 Average Return
- 📈 Average Sharpe Ratio
- 📈 Total AUM

Interactive Components:

- Fund Selector
- NAV Trend
- Performance Table
- Fund Master Table

---

# ⚡ Installation

Clone the repository

```bash
git clone <repository-url>
```

Go inside the project

```bash
cd Capstone_Project_Mutual_Fund_Analytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run ETL Pipeline

```bash
python scripts/live_nav_fetch.py

python scripts/etl_pipeline.py

python scripts/sqlite_loading.py

python scripts/compute_metrics.py
```

---

# ▶️ Run Dashboard

```bash
streamlit run streamlit_app/app.py
```

---

# ☁️ Deployment

The dashboard is deployed using **Streamlit Community Cloud**, allowing users to access it directly from a web browser.

---

# 📚 Learning Outcomes

Through this project I gained practical experience in:

- ETL Pipeline Development
- Data Engineering
- Financial Data Analytics
- SQL Database Design
- Streamlit Dashboard Development
- Interactive Data Visualization
- Cloud Deployment
- Portfolio Optimization
- Software Project Structuring

---

# 🚀 Future Enhancements

Some planned improvements include:

- Real-Time Market Data
- User Authentication
- Portfolio Tracking
- Email Reporting
- Monte Carlo Simulation
- Machine Learning Recommendations
- Power BI Integration
- REST API Support

---

# 👨‍💻 Author

**Lakshit Sharma**

Bluestock Fintech Internship

Mutual Fund Analytics Capstone Project

---

# 📄 License

This project was developed as part of the **Bluestock Fintech Internship Program** and is intended for educational and demonstration purposes.