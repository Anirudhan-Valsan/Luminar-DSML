import pandas as pd

data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/temperature.unknown",header=None,sep=' ')

df = pd.DataFrame(data)
print(df.head())
df.columns = ['year','temperature']
print(df.head())
print("="*100)
print(df.groupby('year') ['temperature'].max().sort_values(ascending=False))
print("="*100)
print(df.groupby('year')['temperature'].min())
print("="*100)
print(df.groupby('year')['temperature'].sum())
print("="*100)
print(df.groupby('year')['temperature'].mean())
print("="*100)
print(df.groupby('year')['temperature'].median())