# perform inner joining
# salary above 2500,age,salary.dat.amount
# maximum age 1 empname ,age,salary,dat,amount
# latest date purchase name,age,dat,amount

import pandas as pd

data1 = pd.read_csv('C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/custom.txt',header=None)
data2 = pd.read_csv('C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/order.txt',header=None)

df1 = pd.DataFrame(data1)
df1.columns=['cid','age','name','loc','salary']
df2 = pd.DataFrame(data2)
df2.columns=['oid','dat','cid','amount']

print(df1)
print("="*100)
print(df2)
print("="*100)


new_df = pd.merge(df1,df2,on='cid',how='inner')

print(new_df)
print("="*100)

print(new_df.loc[new_df['salary'] > 2500][['age','salary','dat','amount']])
print("="*100)

print(new_df.sort_values(by='age',ascending=False)[['name', 'age', 'salary', 'dat', 'amount']].head(1))

print("="*100)

new_df['dat'] = pd.to_datetime(new_df['dat'])

print(new_df.sort_values(by='dat',ascending=False)[['name','age','dat','amount']].head(1))





