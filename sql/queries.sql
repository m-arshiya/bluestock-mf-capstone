-- Top 5 Funds by AUM
SELECT * FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Transactions Count
SELECT COUNT(*)
FROM fact_transactions;

-- Funds
SELECT * FROM dim_fund;

-- Category Wise Funds
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;

-- Fund House Count
SELECT fund_house, COUNT(*)
FROM dim_fund
GROUP BY fund_house;

-- Maximum NAV
SELECT MAX(nav)
FROM fact_nav;

-- Minimum NAV
SELECT MIN(nav)
FROM fact_nav;

-- Average AUM
SELECT AVG(aum)
FROM fact_aum;

-- Performance Count
SELECT COUNT(*)
FROM fact_performance;