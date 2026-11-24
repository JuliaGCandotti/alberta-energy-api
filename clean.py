import pandas as pd

df = pd.read_excel("data/ST37_SH.xlsx")

# 1. Removes spaces and standardizes the status text
df["Licence_Status"] = df["Licence_Status"].str.strip().str.lower()

# 2. Converts the data columns to type data
for col in ["Licence_Status_Date", "Spud_Date", "Most_Recent_Final_Drill_Date"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# 3. Counts empty values per column
print(df.isna().sum())

# 4. Saves in CSV (reads it faster than Excel)
df.to_csv("data/wells_clean.csv", index=False)
print(df["Licence_Status"].value_counts())
print("Saved:", df.shape)