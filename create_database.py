from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

print("Database Created")