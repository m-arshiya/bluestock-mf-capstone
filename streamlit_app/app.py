from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Bluestock Mutual Fund Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📊 Bluestock Mutual Fund Analytics Dashboard")

# -------------------------------------------------
# PATHS
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

performance = pd.read_csv(DATA_DIR / "07_scheme_performance.csv")
transactions = pd.read_csv(DATA_DIR / "08_investor_transactions.csv")
holdings = pd.read_csv(DATA_DIR / "09_portfolio_holdings.csv")
benchmark = pd.read_csv(DATA_DIR / "10_benchmark_indices.csv")
sip = pd.read_csv(DATA_DIR / "04_monthly_sip_inflows.csv")
category = pd.read_csv(DATA_DIR / "05_category_inflows.csv")
folios = pd.read_csv(DATA_DIR / "06_industry_folio_count.csv")
aum = pd.read_csv(DATA_DIR / "03_aum_by_fund_house.csv")

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Industry Overview",
        "Fund Performance",
        "Investor Analytics",
        "SIP Trends",
        "Advanced Analytics",
        "Fund Recommender"
    ]
)

# =================================================
# PAGE 1
# =================================================

if page == "Industry Overview":

    st.header("Industry Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total AUM", "₹81 Lakh Cr")
    c2.metric("Monthly SIP", "₹31K Cr")
    c3.metric("Folios", "26.12 Cr")
    c4.metric("Schemes", str(len(performance)))

    fig = px.line(
        aum,
        x="date",
        y="aum_lakh_crore",
        title="Industry AUM Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

# =================================================
# PAGE 2
# =================================================

elif page == "Fund Performance":

    st.header("Fund Performance")

    fig = px.scatter(
        performance,
        x="return_3yr_pct",
        y="std_dev_ann_pct",
        size="aum_crore",
        color="risk_grade",
        hover_name="scheme_name"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Fund Scorecard")

    st.dataframe(
        performance[
            [
                "scheme_name",
                "fund_house",
                "return_3yr_pct",
                "sharpe_ratio",
                "alpha",
                "beta"
            ]
        ]
    )

# =================================================
# PAGE 3
# =================================================

elif page == "Investor Analytics":

    st.header("Investor Analytics")

    fig = px.bar(
        transactions,
        x="state",
        y="amount_inr",
        title="State Wise Investment"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.pie(
        transactions,
        names="transaction_type",
        values="amount_inr",
        hole=0.5
    )

    st.plotly_chart(fig2, use_container_width=True)

# =================================================
# PAGE 4
# =================================================

elif page == "SIP Trends":

    st.header("SIP Trends")

    fig = px.line(
        sip,
        x="month",
        y="sip_inflow_crore",
        title="Monthly SIP Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

# =================================================
# PAGE 5
# =================================================

elif page == "Advanced Analytics":

    st.header("Advanced Analytics")

    top_sharpe = performance.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(10)

    st.subheader("Top Funds by Sharpe Ratio")

    st.dataframe(top_sharpe)

    top_alpha = performance.sort_values(
        "alpha",
        ascending=False
    ).head(10)

    st.subheader("Top Funds by Alpha")

    st.dataframe(top_alpha)

# =================================================
# PAGE 6
# =================================================

elif page == "Fund Recommender":

    st.header("Fund Recommender")

    risk = st.selectbox(
        "Risk Appetite",
        ["Low", "Moderate", "High"]
    )

    filtered = performance[
        performance["risk_grade"].str.lower() ==
        risk.lower()
    ]

    recommendations = filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)

    st.subheader("Top 3 Recommended Funds")

    st.dataframe(
        recommendations[
            [
                "scheme_name",
                "fund_house",
                "sharpe_ratio"
            ]
        ]
    )