
import os
import sqlite3
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

current_dir = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(
    current_dir,
    "..",
    "data",
    "db",
    "bluestock_mf.db"
)

conn = sqlite3.connect(db_path)

nav_df = pd.read_sql(
    """
    SELECT
        amfi_code,
        date,
        nav
    FROM fact_nav
    """,
    conn
)

fund_master = pd.read_sql(
    """
    SELECT
        amfi_code,
        scheme_name
    FROM dim_fund
    """,
    conn
)

conn.close()

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)

nav_df = nav_df.merge(
    fund_master,
    on="amfi_code"
)

nav_matrix = nav_df.pivot_table(
    index="date",
    columns="scheme_name",
    values="nav"
)

returns = nav_matrix.pct_change().dropna()

print("\n===============================")
print("BONUS 4")
print("Portfolio Optimizer")
print("===============================\n")

available_funds = list(returns.columns)

for i, fund in enumerate(available_funds):

    print(f"{i+1}. {fund}")

print("\nChoose ANY 5 Funds")

selected_funds = []

while len(selected_funds) < 5:

    choice = int(
        input(
            f"Enter Fund Number {len(selected_funds)+1}: "
        )
    )

    fund_name = available_funds[
        choice-1
    ]

    if fund_name not in selected_funds:

        selected_funds.append(
            fund_name
        )

selected_returns = returns[
    selected_funds
]

mean_returns = (
    selected_returns.mean() * 252
)

cov_matrix = (
    selected_returns.cov() * 252
)

print("\nSelected Funds\n")

for fund in selected_funds:

    print("-", fund)    
    

num_portfolios = 1000

portfolio_returns = []
portfolio_risks = []
portfolio_sharpes = []
portfolio_weights = []

risk_free_rate = 0.06

for _ in range(num_portfolios):

    weights = np.random.random(len(selected_funds))

    weights = weights / np.sum(weights)

    portfolio_return = np.sum(
        mean_returns * weights
    )

    portfolio_risk = np.sqrt(
        np.dot(
            weights.T,
            np.dot(
                cov_matrix,
                weights
            )
        )
    )

    sharpe_ratio = (
        portfolio_return - risk_free_rate
    ) / portfolio_risk

    portfolio_returns.append(
        portfolio_return
    )

    portfolio_risks.append(
        portfolio_risk
    )

    portfolio_sharpes.append(
        sharpe_ratio
    )

    portfolio_weights.append(
        weights
    )

portfolio_df = pd.DataFrame({

    "Return": portfolio_returns,

    "Risk": portfolio_risks,

    "Sharpe": portfolio_sharpes

})

best_index = portfolio_df[
    "Sharpe"
].idxmax()

best_return = portfolio_returns[
    best_index
]

best_risk = portfolio_risks[
    best_index
]

best_sharpe = portfolio_sharpes[
    best_index
]

best_weights = portfolio_weights[
    best_index
]

print("\n===================================")
print("OPTIMAL PORTFOLIO")
print("===================================\n")

print(
    f"Expected Return : {best_return:.2%}"
)

print(
    f"Portfolio Risk  : {best_risk:.2%}"
)

print(
    f"Sharpe Ratio    : {best_sharpe:.2f}"
)

print("\nOptimal Allocation\n")

allocation_df = pd.DataFrame({

    "Fund": selected_funds,

    "Weight (%)": np.round(
        best_weights * 100,
        2
    )

})

print(
    allocation_df
)

import plotly.express as px
import plotly.graph_objects as go

fig = px.scatter(

    portfolio_df,

    x="Risk",

    y="Return",

    color="Sharpe",

    color_continuous_scale="Viridis",

    title="Efficient Frontier",

    labels={
        "Risk": "Portfolio Risk",
        "Return": "Expected Return",
        "Sharpe": "Sharpe Ratio"
    }

)

fig.add_trace(

    go.Scatter(

        x=[best_risk],

        y=[best_return],

        mode="markers",

        marker=dict(

            color="red",

            size=15,

            symbol="star"

        ),

        name="Optimal Portfolio"

    )

)

fig.update_layout(

    template="plotly_dark",

    height=700,

    title_x=0.5,

    xaxis_title="Portfolio Risk",

    yaxis_title="Expected Return"

)

fig.show()

print("\n===================================")
print("TOP PORTFOLIO ALLOCATION")
print("===================================\n")

allocation_df = allocation_df.sort_values(

    by="Weight (%)",

    ascending=False

)

print(allocation_df)

print("\n===================================")
print("SUMMARY")
print("===================================\n")

print(f"Funds Selected        : {len(selected_funds)}")
print(f"Simulated Portfolios  : {num_portfolios}")
print(f"Best Sharpe Ratio     : {best_sharpe:.2f}")
print(f"Expected Return       : {best_return:.2%}")
print(f"Portfolio Risk        : {best_risk:.2%}")

allocation_df.to_csv(

    os.path.join(

        current_dir,

        "..",

        "reports",

        "optimal_portfolio.csv"

    ),

    index=False

)

print("\nOptimal Portfolio saved to reports/optimal_portfolio.csv")