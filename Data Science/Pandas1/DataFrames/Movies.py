import pandas as pd


df = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/movies.csv",header=None)

df.columns = ['ID','NAME','YEAR','RATING','DURATION(mins)']

df['DURATION(mins)'] = df["DURATION(mins)"]//60

print(df.head())
print("*"*100)
print(df.shape)
print("*"*100)
print(df.describe())