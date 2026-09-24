import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA = Path("data/Online Retail.xlsx")
DB = Path("retail.db")
OUT = Path("visualizations")
OUT.mkdir(exist_ok=True)

if not DATA.exists():
    raise FileNotFoundError("Download data/Online Retail.xlsx from the official UCI dataset page.")

df = pd.read_excel(DATA)
df.columns = [c.strip() for c in df.columns]
df = df.dropna(subset=["InvoiceNo","StockCode","Quantity","UnitPrice","InvoiceDate"]).copy()
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)].copy()
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("Rows after cleaning:", len(df))
print("Total revenue:", round(df["Revenue"].sum(),2))
print("Unique invoices:", df["InvoiceNo"].nunique())
print("Average order value:", round(df["Revenue"].sum()/df["InvoiceNo"].nunique(),2))
print("\nRevenue statistics:\n", df["Revenue"].describe().round(2))

monthly = df.assign(month=df["InvoiceDate"].dt.to_period("M").astype(str)).groupby("month")["Revenue"].sum()
top_products = df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10)
top_countries = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10)
customers = df[df["CustomerID"].notna()].groupby("CustomerID").agg(
    invoice_count=("InvoiceNo","nunique"),
    total_quantity=("Quantity","sum"),
    total_revenue=("Revenue","sum")
).sort_values("total_revenue", ascending=False)

print("\nTop five customers by revenue:\n", customers.head().round(2))

monthly.plot(figsize=(9,5), title="Monthly Revenue")
plt.ylabel("Revenue"); plt.tight_layout(); plt.savefig(OUT/"monthly_revenue.png",dpi=150); plt.close()

top_products.sort_values().plot(kind="barh", figsize=(9,5), title="Top 10 Products by Revenue")
plt.xlabel("Revenue"); plt.tight_layout(); plt.savefig(OUT/"top_products_by_revenue.png",dpi=150); plt.close()

top_countries.sort_values().plot(kind="barh", figsize=(9,5), title="Top 10 Countries by Revenue")
plt.xlabel("Revenue"); plt.tight_layout(); plt.savefig(OUT/"top_countries_by_revenue.png",dpi=150); plt.close()

customers["total_revenue"].head(10).sort_values().plot(kind="barh", figsize=(8,5), title="Top 10 Customers by Revenue")
plt.xlabel("Revenue"); plt.tight_layout(); plt.savefig(OUT/"top_customers_by_revenue.png",dpi=150); plt.close()

with sqlite3.connect(DB) as conn:
    df.to_sql("retail", conn, if_exists="replace", index=False)

print("\nDone. SQLite database and charts created.")
