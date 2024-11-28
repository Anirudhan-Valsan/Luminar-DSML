#7. Each age group count [age desc order]

import pandas as pd

data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/Assignments/customer1.txt",header=None)

df = pd.DataFrame(data)

df.columns = ["ID","F_NAME","L_NAME","AGE","PROF","LOC"]


age_count = df.groupby('AGE') ['AGE'].count()

print(age_count.sort_values(ascending=False))


