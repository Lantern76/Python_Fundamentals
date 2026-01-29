import pandas as pd

df = pd.read_csv("cleaning_practice.csv")


df["Amount"] = df["Amount"].str.replace("$", "")
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
df["Age"] = df["Age"].replace(300, 30)
df["City"] = df["City"].str.title()

median_amount = df["Amount"].median()
df["Amount"] = df["Amount"].fillna(median_amount)

df = df.dropna()
df = df.sort_values(by="City")
df = df.drop_duplicates()
df = df.groupby("City")["Amount"].sum()

print(df)


df.plot(kind="bar")
