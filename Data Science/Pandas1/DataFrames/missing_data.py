import pandas as pd

df = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/missing_data.csv")

print(df.head())

print("-"*100)

print(df.columns)

print("-"*100)

print(df.isna().sum())
print("-"*100)
df1 = df.fillna(250)

print(df1.isna().sum())
print("-"*100)


