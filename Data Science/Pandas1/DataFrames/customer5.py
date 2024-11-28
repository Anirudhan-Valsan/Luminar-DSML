import pandas as pd



#each prof count descending
#each prof max salary desc
#each prof min salary asc
#each country work total salary
#each prof avg age
#each loc min age
data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/customer5.txt",sep=',',header=None)

df = pd.DataFrame(data)
df.columns = ['ID','F_NAME','L_NAME','AGE','PROFESSION','COUNTRY','SALARY']

print("="*100)

print(df.groupby('PROFESSION')['PROFESSION'].count().sort_values(ascending=False))
print("="*100)
print(df.groupby('PROFESSION')['SALARY'].max().sort_values(ascending=False))
print("="*100)
print(df.groupby('PROFESSION')['SALARY'].min().sort_values())
print("="*100)
print(df.groupby('COUNTRY')['SALARY'].sum())
print("="*100)
print(df.groupby('PROFESSION')['AGE'].mean())
print("="*100)
print(df.groupby('COUNTRY')['AGE'].min())