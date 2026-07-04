import requests
import pandas as pd

funds = {
    'hdfc_top_100': 125497,
    'sbi_bluechip': 119551,
    'icici_bluechip': 120503,
    'nippon_large_cap': 118632,
    'axis_bluechip': 119092,
    'kotak_bluechip': 120841
}

for fund_name, scheme_code in funds.items():

    print(f"\nFetching data for {fund_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data['data'])

    df.to_csv(f"data/raw/{fund_name}.csv", index=False)

    print("CSV saved successfully")