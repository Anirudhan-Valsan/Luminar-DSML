import pandas as pd

data =pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/ASSIGNMENT 2/txn.csv")
df = pd.DataFrame(data)
df.columns = ['oid','dat','cid','amount','category','product','city','state','method']
print('='*100)

#1. Find Row count
print('Find Row count')
print(len(df))
print('='*100)

#2. jan month oid,cusno,category,product,state
    #A. Row count
print('#2.')
print(df[df['dat'].str.split('-').str[1] == '01'][['oid', 'cid', 'category', 'product', 'state']])
print('='*100)

#3. July Month oid,cusno,category,product,state
 #B. Row count
print('#3. July Month ')
print(df[df['dat'].str.split('-').str[1] == '07'][['oid', 'cid', 'category', 'product', 'state']])
print('='*100)

#4. Each category [count desc sort]
print('#4. Each category [count desc sort]')
print(df.groupby('category')['category'].count().sort_values(ascending=False))
print('='*100)

#5. Category full deatils
print('#5. Category full deatils')
print(df.loc[df['category'] == 'Outdoor Recreation'])
print('='*100)

#6. Each paymethod count
print('#6. Each paymethod count')
print(df.groupby('method')['method'].count())
print('='*100)

#7. jan-july month purchase count [include]
print('#7. jan-july month purchase count [include]')
df['month']=df['dat'].str.split('-').str[1].astype(int)
jan_to_jul = df[(df['month']>= 1 )& (df['month'] <= 7)]
print(len(jan_to_jul))
print('='*100)

#8. Each category total amount
print('#8. Each category total amount')
print(df.groupby('category')['amount'].sum())
print('='*100)

#9. Each category maximum amount
print('#9. Each category maximum amount')
print(df.groupby('category')['amount'].max())
print('='*100)

#10. Each category avg amount
print('#10. Each category avg amount')
print(df.groupby('category')['amount'].mean())
print('='*100)

#11.total amount by cash and credit card
print('11.total amount by cash and credit card')
print(df.groupby('method')['amount'].sum())
print('='*100)

#12. Indoor games ,total amount
print('#12. Indoor games ,total amount')
print(df.loc[df['category'] == 'Indoor Games'][['amount']].sum())
print('='*100)

#13. Each state count
print('13. Each state count')
print(df.groupby('state')['state'].count().sort_values(ascending=False))