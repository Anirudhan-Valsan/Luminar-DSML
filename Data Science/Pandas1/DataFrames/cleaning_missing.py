import pandas as pd

data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/missing_data.csv")

df = pd.DataFrame(data)

print(df.head())
print("="*100)

print(df.describe())
print("="*100)

print(df.count())
print("="*100)

print(df.isna().sum())
print("="*100)

cal_mean = df['Calories'].mean()
df.fillna({'Calories':cal_mean},inplace=True)

x = df['Date'].mode()[0]

df.fillna({'Date':x},inplace=True)

print(df.isna().sum())
print("="*100)

# #dropna
#
# df.dropna(inplace=True,ignore_index=True)
# df.dropna(subset=['Calories'],inplace=True,ignore_index=True)