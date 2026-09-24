# Online Retail Sales Analysis

A compact SQL + Python + statistics project using transaction data from an online retailer.

## What it demonstrates
- Data cleaning
- SQL filtering and aggregation
- Calculated fields
- Descriptive statistics
- Monthly trend analysis
- Product and customer summaries
- Visualization

## Dataset
UCI Online Retail:
https://archive.ics.uci.edu/dataset/352/online+retail


## Analysis questions
1. What is total revenue after cleaning?
2. How many invoices are present?
3. What is average order value?
4. Which products generate the most revenue?
5. Which countries contribute the most revenue?
6. How does revenue vary by month?
7. Which transaction quantities occur most often?
8. What does the customer-level summary look like?

## SQL skills
Filtering, DISTINCT, GROUP BY, ORDER BY, LIMIT, aggregate functions, calculated fields, and customer-level summaries.

## Run
```bash
pip install -r requirements.txt
python src/analyze.py
```

## Cleaning rule
Rows missing essential fields and rows with non-positive quantity or unit price are excluded from the main revenue analysis. The rule is documented rather than hidden.

## Limitations
The data represents one retailer and a historical period, so results should not automatically be generalized to other retailers or periods.
