import pandas as pd

df = pd.read_excel("data/ST37_SH.xlsx")
print(df.shape)
print(df.columns.tolist())
print(df.head())

print(df["Licence_Status"].value_counts())