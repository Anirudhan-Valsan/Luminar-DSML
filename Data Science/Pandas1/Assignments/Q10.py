"""
10. us work
    A. Row count
    B. Each age group count
    C. Each profession count [count desc]
    D. Civil engineer dept and age above 30

"""
import pandas as pd
data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/Assignments/customer1.txt",header=None)
df = pd.DataFrame(data)
df.columns = ["ID","F_NAME","L_NAME","AGE","PROF","LOC"]
df_us = df.loc[df['LOC'] == 'us']
print(len(df_us))
print("="*100)

print(df_us.groupby('AGE')['AGE'].count())
print("="*100)

print(df_us.groupby('PROF') ['PROF'].count().sort_values(ascending=False))
print("="*100)

print(df_us.loc[(df['PROF'] == 'Civil engineer')&(df['AGE'] > 30)])