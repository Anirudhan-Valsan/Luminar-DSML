# both dataframe has a common field, when such dataframes are joined the data which matches with the common field are shown
import pandas as pd

dic1 = {'id':[1,2,3,4,5],
        'fname':['Anirudhan','Aswin','Amal','Sreerag','shubham'],
        'lname':['Valsan','Krishna','Das','Das','Vijay'],
        'age':[25,22,26,33,22]}

dic2 = {'prof':['ML Engineer','Data analyst','Vfx','signal engineer','Data scientisgt'],
        'Salary':[150000,80000,60000,120000,90000],'id':[4,5,6,7,8],
        'location':['london','kochi','bengaluru','hyderabad','pune']}

df1 = pd.DataFrame(dic1)
df2 = pd.DataFrame(dic2)

print(df1)
print("="*100)
print(df2)
print("="*100)
new_df = pd.merge(df1,df2,on='id',how='inner')[['fname','lname','age','prof','Salary']]

print(new_df)