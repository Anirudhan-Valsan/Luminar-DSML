import pandas as pd

data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/customer1.txt",header=None)

df = pd.DataFrame(data=data)

df.columns=columns=['ID','F_NAME','L_NAME','AGE','PROFESSION','COUNTRY']

print(df.head())

print("="*100)

#Q1 missing value

print(df.isna().sum())
print("="*100)

#Q2 fill missing value

df = df.fillna('india')
print(df.isna().sum())
print("="*100)

#Q3 Seperate x and y

x = df[['F_NAME','L_NAME','AGE','PROFESSION']]
print(x)
y = df[['COUNTRY']]
print(y)
print("="*100)

#Q4

print(df[['F_NAME','L_NAME','AGE','PROFESSION']])
print("="*100)

#Q5

print(df.loc[df['AGE'] > 50][df.columns[1:5]])
print("="*100)

#Q6
print(df.loc[(df['AGE'] <=50)&(df['AGE']>=25)][df.columns[1:4]])
print("="*100)

#Q7

print(df.sort_values(by='AGE',ascending=False)[df.columns[1:5]].head())
print("="*100)

#Q8
print(df.sort_values(by='AGE',)[df.columns[1:]].head(3))
print("="*100)

#Q9

print( df.loc[df["COUNTRY"] == 'india'][df.columns[1:5]] )
print("="*100)

#Q10

print( df.loc[(df["COUNTRY"] == 'india') & (df['PROFESSION'] == 'Doctor')][df.columns[1:4]] )
print("="*100)

#Q11
print(df.sort_values(by='AGE').loc[df['COUNTRY'] == 'us'][df.columns[1:5]].head(3))
print("="*100)

#Q12
print( df.loc[(df['PROFESSION'] == 'Actor')&(df['AGE']>50)][df.columns[1:4]] )
print("="*100)

#Q13
print( df.loc[df['PROFESSION'] == 'Pilot'][df.columns[1:]].sort_values(by='AGE').head(2) )
print("="*100)

#Q14
print( df.loc[df['PROFESSION'] == 'Pilot'][df.columns[1:5]].sort_values(by='AGE',ascending=False).head(1) )
print("="*100)

#Q15
print( df.loc[(df['COUNTRY']=='india')& (df['AGE'] <= 40)&(df['AGE']>=25)][df.columns[1:5]])





