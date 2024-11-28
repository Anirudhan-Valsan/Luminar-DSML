
import pandas as pd

df = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/customer1.txt",sep=',',header=None)

df.columns = ['ID','F_NAME','L_NAME','AGE','PROFESSION','COUNTRY']


"""
#num of missing values
print((df.isna().sum()))
print("-"*100)

print(df.head())
print("-"*100)

print(df.describe())
print("-"*100)

#Filling missing values
df1 = df.fillna('UNKNOWN')


#print(df[df.columns[1:5]].head())

print(df[df.columns[1:4]].head(25))
print('\n',"="*100,'\n')

print(df[df.columns[1:5]].tail(10))
print('\n',"="*100,'\n')

print(df.iloc[10:21])
print('\n',"="*100,'\n')

print(df.iloc[3:31,1:5])
print('\n',"="*100,'\n')

print(df.iloc[1::5,:4])
print('\n',"="*100,'\n')

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

print(x)
print('\n',"="*100,'\n')
print(y)
print(df.groupby('PROFESSION')['PROFESSION'].count().sort_values(ascending=False))
print("="*100)

print(df.groupby('COUNTRY')['COUNTRY'].count().sort_values(ascending=False))
"""
#print(df.groupby('PROFESSION') ['AGE'].max())
print(df.groupby('COUNTRY') ['AGE'].max().sort_values(ascending=False))