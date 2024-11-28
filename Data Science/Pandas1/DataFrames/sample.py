# age>22 print(fname,lname)
# age == 24 fname,lname,loc
#chennai work data's
# age above 23 and loc chennai, fname,lname,age,phno

import pandas as pd

df = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/sample4.txt",header=None)

new_df = pd.DataFrame(df)
new_df.columns=["id","fname","lname",'age',"phno","loc"]
"""
print(new_df.loc[new_df['age'] > 22][new_df.columns[1:3]])

print("="*100)

print(new_df.loc[new_df['age'] == 24][['fname','lname','loc']])

print("="*100)
print(new_df.loc[new_df['loc'] == 'Chennai'])

print("="*100)

print(new_df.loc[(new_df['age'] > 23) & (new_df['loc'] == 'Chennai')] 
            [['fname','lname','age','phno']])

 #  is used to extend the query to the next line
"""


print(new_df.sort_values(by='age',ascending=False)[new_df.columns[1:5]].head(2))
print("><"*100)

print(new_df.sort_values(by='age')[new_df.columns[1:4]].head(1))
print("><"*100)

df1 = new_df.loc[new_df['loc'] == 'Chennai'][new_df.columns[1:4]] \
            .sort_values(by='age',ascending=False).head(1)
print(df1)
print("><"*100)

