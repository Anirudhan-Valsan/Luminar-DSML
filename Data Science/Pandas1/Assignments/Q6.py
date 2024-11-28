#6. Full data

import pandas as pd

data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/Assignments/customer1.txt",header=None)

df = pd.DataFrame(data)

df.columns = ["ID","F_NAME","L_NAME","AGE","PROF","LOC"]

unique = df.groupby('LOC') ['LOC'].count()

print(unique.sort_values(ascending=False))
print("="*100)

print(df.loc[df['LOC'] == 'australia'])

