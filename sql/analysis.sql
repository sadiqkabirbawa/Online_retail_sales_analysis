-- 1. Total revenue
SELECT ROUND(SUM(Revenue),2) AS total_revenue FROM retail;

-- 2. Unique invoices
SELECT COUNT(DISTINCT InvoiceNo) AS unique_invoices FROM retail;

-- 3. Revenue by country
SELECT Country, ROUND(SUM(Revenue),2) AS total_revenue
FROM retail GROUP BY Country ORDER BY total_revenue DESC LIMIT 10;

-- 4. Top products by revenue
SELECT Description, ROUND(SUM(Revenue),2) AS total_revenue
FROM retail WHERE Description IS NOT NULL
GROUP BY Description ORDER BY total_revenue DESC LIMIT 10;

-- 5. Top products by quantity
SELECT Description, SUM(Quantity) AS total_quantity
FROM retail WHERE Description IS NOT NULL
GROUP BY Description ORDER BY total_quantity DESC LIMIT 10;

-- 6. Monthly revenue
SELECT strftime('%Y-%m',InvoiceDate) AS month, ROUND(SUM(Revenue),2) AS revenue
FROM retail GROUP BY month ORDER BY month;

-- 7. Average order value
SELECT ROUND(SUM(Revenue)/COUNT(DISTINCT InvoiceNo),2) AS average_order_value
FROM retail;

-- 8. Top customers by revenue
SELECT CustomerID, COUNT(DISTINCT InvoiceNo) AS invoice_count,
       SUM(Quantity) AS total_quantity, ROUND(SUM(Revenue),2) AS total_revenue
FROM retail WHERE CustomerID IS NOT NULL
GROUP BY CustomerID ORDER BY total_revenue DESC LIMIT 20;

-- 9. Common transaction quantities
SELECT Quantity, COUNT(*) AS transaction_count
FROM retail GROUP BY Quantity ORDER BY transaction_count DESC LIMIT 10;

-- 10. Revenue concentration among top 10 countries
SELECT ROUND(
  100.0*SUM(revenue)/(SELECT SUM(Revenue) FROM retail),2
) AS top_10_country_share
FROM (
  SELECT Country, SUM(Revenue) AS revenue
  FROM retail GROUP BY Country ORDER BY revenue DESC LIMIT 10
);
