import os
import pandas as pd

PATH = "data/dataset.csv"
if not os.path.exists(PATH):
    print("No dataset found at", PATH, "- mount ./data to /app/data")
    raise SystemExit(0)

rows = 0
total = 0.0
by_state = {}
by_company = {}

for chunk in pd.read_csv(PATH, chunksize=500_000):
    rows += len(chunk)
    total += chunk["Amount_USD"].sum()
    for k, v in chunk.groupby("State")["Amount_USD"].sum().items():
        by_state[k] = by_state.get(k, 0) + v
    for k, v in chunk.groupby("Company")["Amount_USD"].sum().items():
        by_company[k] = by_company.get(k, 0) + v

print("Rows:", rows)
print("Total amount (USD): {:,.2f}".format(total))
print("Top 5 states:")
print(pd.Series(by_state).nlargest(5))
print("Top 5 companies:")
print(pd.Series(by_company).nlargest(5))