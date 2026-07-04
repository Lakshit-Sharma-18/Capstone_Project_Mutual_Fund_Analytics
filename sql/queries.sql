
--!  Top 5 funds by AUM.
select sum(aum_lakh_crore) as total_aum, fund_house
from fact_aum
GROUP BY fund_house
ORDER BY sum(aum_lakh_crore) DESC
Limit 5;

--!  Average NAV per month.
SELECT
    strftime('%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;
-- Use SQLite's strftime() function to extract the year and month from the date column
-- so that the average NAV can be calculated on a monthly basis.


--! SIP YoY growth.
SELECT
    substr(month,1,4) AS year,
    round(AVG(yoy_growth_pct),2) AS average_growth
FROM fact_sip_inflows
GROUP BY substr(month,1,4)
ORDER BY year;

-- we used substring in this because the type of month is not date it is string thats why 

--! Transactions by state
select state , sum(amount_inr) as total
from fact_transactions
GROUP BY state
ORDER BY state ASC

--! Funds with expense ratio < 1%.


SELECT
    scheme_name,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;


--! Find the top 5 funds with the highest 5-year returns.

SELECT
    amfi_code,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;



--! Calculate the average expense ratio across all mutual funds.

SELECT
    AVG(expense_ratio_pct) AS average_expense_ratio
FROM fact_performance;



--! Find the total transaction amount grouped by payment mode.

SELECT
    payment_mode,
    SUM(amount_inr) AS total_transaction_amount
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_transaction_amount DESC;


--! Count the number of investors in each age group.

SELECT
    age_group,
    COUNT(investor_id) AS total_investors
FROM fact_transactions
GROUP BY age_group
ORDER BY total_investors DESC;



--! Find the average Sharpe Ratio for each risk grade.

SELECT
    risk_grade,
    AVG(sharpe_ratio) AS average_sharpe_ratio
FROM fact_performance
GROUP BY risk_grade
ORDER BY average_sharpe_ratio DESC;