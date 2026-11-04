import pandas as pd

SRC = r"D:\OP_DTL_GNRL_PGYR2025_P06302026_06032026.csv"
OUT = r"C:\tp04\data\dataset.csv"

cols = ["Covered_Recipient_Type", "Recipient_State", "Recipient_Country",
        "Covered_Recipient_Specialty_1",
        "Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name",
        "Total_Amount_of_Payment_USDollars", "Date_of_Payment",
        "Number_of_Payments_Included_in_Total_Amount",
        "Form_of_Payment_or_Transfer_of_Value",
        "Nature_of_Payment_or_Transfer_of_Value", "Record_ID"]

parts = []
for chunk in pd.read_csv(SRC, usecols=cols, dtype=str,
                         encoding="latin-1", chunksize=500_000):
    d = pd.to_datetime(chunk["Date_of_Payment"], format="%m/%d/%Y", errors="coerce")
    chunk["Date_of_Payment"] = d
    chunk = chunk[(d >= "2025-01-01") & (d <= "2025-03-31")]
    parts.append(chunk)
    print("rows kept so far:", sum(len(p) for p in parts))

df = pd.concat(parts, ignore_index=True)
df = df.drop_duplicates(subset="Record_ID")

df["Total_Amount_of_Payment_USDollars"] = pd.to_numeric(
    df["Total_Amount_of_Payment_USDollars"], errors="coerce")
df["Number_of_Payments_Included_in_Total_Amount"] = pd.to_numeric(
    df["Number_of_Payments_Included_in_Total_Amount"], errors="coerce")

spec = df["Covered_Recipient_Specialty_1"].fillna("").str.strip()
split = spec.str.split("|", expand=True).reindex(columns=[0, 1])
df["Provider_Category"] = split[0]
df["Specialty"] = split[1]
df = df.drop(columns=["Covered_Recipient_Specialty_1", "Record_ID"])

df = df.rename(columns={
    "Covered_Recipient_Type": "Recipient_Type",
    "Recipient_State": "State",
    "Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name": "Company",
    "Total_Amount_of_Payment_USDollars": "Amount_USD",
    "Number_of_Payments_Included_in_Total_Amount": "Payment_Count",
    "Date_of_Payment": "Payment_Date",
    "Form_of_Payment_or_Transfer_of_Value": "Payment_Form",
    "Nature_of_Payment_or_Transfer_of_Value": "Payment_Nature"})

df = df[df["Specialty"].notna() & (df["Specialty"] != "")]

df.to_csv(OUT, index=False, encoding="utf-8")
print("DONE. Final rows:", len(df))