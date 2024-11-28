"""
9. India work
    A. Row count
    B. Each profession count [count desc order]
    C. Age mxm 3 employees fname,lname,age,prof
    D. Age minimum 3 employees fname,lname,age,prof
    E. age above 40 full data
    F. age range 30 to 40 [profession count]
"""
import pandas as pd

data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/Assignments/customer1.txt",header=None)
df = pd.DataFrame(data)
df.columns = ["ID","F_NAME","L_NAME","AGE","PROF","LOC"]
df_india = df.loc[df['LOC'] == 'india']
print("Row Count = ",len(df_india))
print("="*100)
prof_count = df_india.groupby('PROF') ['PROF'].count().sort_values(ascending=False)
print("Profession count\n",prof_count)
print("="*100)
print("Age mxm 3 employees fname,lname,age,prof\n",df_india.sort_values('AGE',ascending=False)[df.columns[1:5]].head(3))
print("="*100)
print("Age minim 3 employees fname,lname,age,prof\n",df_india.sort_values('AGE')[df.columns[1:5]].head(3))
print("="*100)
print("Age Above 40",df.loc[df['AGE'] > 40][df.columns[1:]])
print("="*100)
print("age range 30 to 40 [profession count]")
print(df.loc[(df['AGE']<=40)&(df['AGE']>=30)].groupby('PROF')['PROF'].count())
print("="*100)









