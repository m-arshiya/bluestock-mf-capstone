import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

files = [
    "nav_history_clean.csv",
    "investor_transactions_clean.csv",
    "scheme_performance_clean.csv"
]

for file in files:

    df = pd.read_csv(
        f"data/processed/{file}"
    )

    table_name = file.replace(
        ".csv",
        ""
    )

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table_name} loaded"
    )

print("Database Loading Complete")