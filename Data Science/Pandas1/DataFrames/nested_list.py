#nested list  : id,fname,lname,age,prof,salary

import pandas as pd

employee = [[111,"Anirudhan","Valsan",25,"ML Engineer",150000],
            [112,"Aswin","Krishna",22,"Data Scientist",70000],
            [113,"Shubham,","Vijay",22,"Data Analyst",50000],
            [114,"Athul","Krishna",23,"Data Engineer",40000],
            [115,"Amal","Das",26,"VFX artist",60000],
            [116,"Sreerag","Das",33,"Signal engineer",120000],
            [117,"Nanadalal","S",26,"Logistics Operations",125000]]

columns = ["E_ID","F_NAME","L_NAME","AGE","PROFESSION","SALARY"]

df =pd.DataFrame(employee,columns=columns )
#df['Gender'] = ['Male','Male','Male','Male','Male','Male','Male']
"""print(df)
print("-"*100)
print()
print(df[columns[1:5]])"""
#print(df[df.columns[1:5]].head(2))

print(df.loc[df['AGE']>25])
print('\n',"="*100,'\n')

#python prof

print(df.loc[df['PROFESSION'] == 'ML Engineer'][df.columns[1:4]])
