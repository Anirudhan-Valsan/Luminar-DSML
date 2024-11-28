import pandas as pd
# total num of missing values
# each count of target column
# separate x and y
# Fill the missing values using proper method
# trestbps column value >= 180 is assumed as wrong data and to be filled with mean

data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/heart.csv")

df = pd.DataFrame(data)
print(df.head())
print("="*100)

print("Total Number of missing values")
print(df.isna().sum())
print("="*100)

print(df.groupby('target')['target'].count())
print("="*100)

x = df['restecg'].mode()[0]
df['restecg'].fillna(x,inplace=True)

df['trestbps'].fillna(df['trestbps'].mean(),inplace=True)
df['thalach'].fillna(df['thalach'].mean(),inplace=True)
df['ca'].fillna(df['ca'].mode()[0],inplace=True)
df['thal'].fillna(df['thal'].mode()[0],inplace=True)

print(df.isna().sum())
print("="*100)

x = df.iloc[:,:-1]
y = df.iloc[:,-1]



print(x)
print("="*100)
print(y)
print("="*100)
for i in df.index:
    if df.loc[i,'trestbps'] > 180:
        df.loc[i,'trestbps'] = df['trestbps'].mean()

print(df)



