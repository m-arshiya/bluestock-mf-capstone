import requests
import pandas as pd

codes = [119551, 120503, 118632, 119092, 120841]

for code in codes:
    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"{code}: HTTP Error {response.status_code}")
            continue

        if not response.text.strip():
            print(f"{code}: Empty response")
            continue

        data = response.json()

        if "data" not in data:
            print(f"{code}: No NAV data available")
            continue

        df = pd.DataFrame(data["data"])

        df.to_csv(f"data/raw/{code}.csv", index=False)

        print(f"{code}: Saved successfully")

    except Exception as e:
        print(f"{code}: {e}")