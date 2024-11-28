#2. Remove duplicates rows and find total row count

import pandas as pd

data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/Assignments/customer1.txt",header=None)

df = pd.DataFrame(data)

df.columns = ["ID","F_NAME","L_NAME","AGE","PROF","LOC"]

print(df.shape[0])
print("="*100)

df1 = df.drop_duplicates()

print(df1.shape[0])





