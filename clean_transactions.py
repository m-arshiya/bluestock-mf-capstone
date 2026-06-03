import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

df = df[df["amount_inr"] > 0]

print("Transaction Types:")
print(df["transaction_type"].unique())

print("\nKYC Status:")
print(df["kyc_status"].unique())

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Saved Successfully")