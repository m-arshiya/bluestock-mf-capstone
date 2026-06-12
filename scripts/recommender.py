import pandas as pd

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

risk = input(
    "Enter Risk Appetite (Low / Moderate / High): "
).strip().lower()

filtered = performance[
    performance['risk_grade'].str.lower() == risk
]

recommendation = (
    filtered
    .sort_values(
        'sharpe_ratio',
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds\n")

print(
    recommendation[
        [
            'scheme_name',
            'fund_house',
            'sharpe_ratio'
        ]
    ]
)