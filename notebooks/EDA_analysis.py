import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load datasets

nav = pd.read_csv("data/raw/02_nav_history.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
category = pd.read_csv("data/raw/05_category_inflows.csv")
folio = pd.read_csv("data/raw/06_industry_folio_count.csv")
portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")

print("Datasets Loaded Successfully")
nav['date'] = pd.to_datetime(nav['date'])

fig = px.line(
    nav,
    x='date',
    y='nav',
    color='amfi_code',
    title='Daily NAV Trend 2022-2026'
)

fig.write_html("reports/charts/nav_trend.html")

print("NAV Trend Created")
aum['year'] = pd.to_datetime(aum['date']).dt.year

plt.figure(figsize=(12,6))

sns.barplot(
    data=aum,
    x='year',
    y='aum_crore',
    hue='fund_house'
)

plt.title("AUM Growth by Fund House")

plt.tight_layout()

plt.savefig("reports/charts/aum_growth.png")

plt.close()

print("AUM Chart Saved")
sip['month'] = pd.to_datetime(sip['month'])

fig = px.line(
    sip,
    x='month',
    y='sip_inflow_crore',
    title='Monthly SIP Inflow Trend'
)

fig.write_html("reports/charts/sip_trend.html")

print("SIP Trend Saved")
pivot = category.pivot(
    index='category',
    columns='month',
    values='net_inflow_crore'
)

plt.figure(figsize=(14,8))

sns.heatmap(
    pivot,
    cmap='YlGnBu'
)

plt.title("Category Inflow Heatmap")

plt.tight_layout()

plt.savefig("reports/charts/category_heatmap.png")

plt.close()

print("Heatmap Saved")
folio['month'] = pd.to_datetime(folio['month'])

plt.figure(figsize=(12,6))

plt.plot(
    folio['month'],
    folio['total_folios_crore']
)

plt.title("Folio Growth")

plt.tight_layout()

plt.savefig("reports/charts/folio_growth.png")

plt.close()

print("Folio Growth Saved")
sector = portfolio.groupby(
    'sector'
)['weight_pct'].sum()

plt.figure(figsize=(8,8))

plt.pie(
    sector,
    labels=sector.index
)

centre = plt.Circle((0,0),0.6)

plt.gca().add_artist(centre)

plt.title("Sector Allocation")

plt.savefig(
    "reports/charts/sector_donut.png"
)

plt.close()

print("Sector Chart Saved")
plt.figure(figsize=(8,8))

transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

transactions["age_group"].value_counts().plot.pie(
    autopct="%1.1f%%"
)

plt.title("Investor Age Group Distribution")

plt.savefig(
    "reports/charts/age_group_pie.png"
)

plt.close()

print("Age Group Chart Saved")
plt.figure(figsize=(10,6))

sns.boxplot(
    data=transactions,
    x="age_group",
    y="amount_inr"
)

plt.title(
    "Investment Amount by Age Group"
)

plt.savefig(
    "reports/charts/age_group_boxplot.png"
)

plt.close()

print("Age Boxplot Saved")
plt.figure(figsize=(8,8))

transactions["gender"].value_counts().plot.pie(
    autopct="%1.1f%%"
)

plt.title("Gender Distribution")

plt.savefig(
    "reports/charts/gender_split.png"
)

plt.close()

print("Gender Chart Saved")
state_data = (
    transactions.groupby("state")
    ["amount_inr"]
    .sum()
    .sort_values()
)

plt.figure(figsize=(12,8))

state_data.plot.barh()

plt.title(
    "State-wise SIP Amount"
)

plt.savefig(
    "reports/charts/state_distribution.png"
)

plt.close()

print("State Chart Saved")
plt.figure(figsize=(8,8))

transactions["city_tier"].value_counts().plot.pie(
    autopct="%1.1f%%"
)

plt.title(
    "T30 vs B30 Distribution"
)

plt.savefig(
    "reports/charts/t30_b30.png"
)

plt.close()

print("City Tier Chart Saved")
sector_data = (
    portfolio.groupby("sector")
    ["weight_pct"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

sector_data.plot.bar()

plt.title(
    "Top 10 Sectors by Weight"
)

plt.savefig(
    "reports/charts/top_sectors.png"
)

plt.close()

print("Top Sectors Chart Saved")
stock_data = (
    portfolio.groupby("stock_name")
    ["weight_pct"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

stock_data.plot.bar()

plt.title(
    "Top 10 Stock Holdings"
)

plt.savefig(
    "reports/charts/top_stocks.png"
)

plt.close()

print("Top Stocks Chart Saved")
pivot_nav = nav.pivot_table(
    index="date",
    columns="amfi_code",
    values="nav"
)

returns = pivot_nav.pct_change()

corr = returns.corr()

plt.figure(figsize=(12,10))

sns.heatmap(
    corr,
    cmap="coolwarm"
)

plt.title(
    "NAV Return Correlation Matrix"
)

plt.savefig(
    "reports/charts/correlation_matrix.png"
)

plt.close()

print("Correlation Matrix Saved")
plt.figure(figsize=(12,6))

plt.plot(
    sip["month"],
    sip["yoy_growth_pct"]
)

plt.title(
    "SIP YoY Growth Percentage"
)

plt.savefig(
    "reports/charts/sip_growth.png"
)

plt.close()

print("SIP Growth Chart Saved")
