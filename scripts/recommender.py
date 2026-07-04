import pandas as pd
import os

current_dir = os.path.dirname(__file__)

csv_path = os.path.join(
    current_dir,
    '..',
    'reports',
    'fund_scorecard.csv'
)

fund_df = pd.read_csv(csv_path)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
).strip().title()

if risk not in ['Low', 'Moderate', 'High']:
    print("Invalid Risk Appetite! Please enter Low, Moderate, or High.")

else:

    if risk == 'Low':
        top_funds = (
            fund_df
            .sort_values(by='Max_Drawdown', ascending=True)
            .head(3)
        )

    elif risk == 'Moderate':
        top_funds = (
            fund_df
            .sort_values(by='Composite_Score', ascending=False)
            .head(3)
        )

    else:  # High Risk
        top_funds = (
            fund_df
            .sort_values(by='Sharpe_Ratio', ascending=False)
            .head(3)
        )

    print("\nTop 3 Recommended Funds:\n")

    print(
        top_funds[
            [
                'amfi_code',
                'Sharpe_Ratio',
                'Max_Drawdown',
                'Composite_Score'
            ]
        ]
    )