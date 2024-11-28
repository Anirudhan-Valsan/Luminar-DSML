#3. Age maximum 10 fname,lname,prof,loc

import pandas as pd

data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/Assignments/customer1.txt",header=None)

df = pd.DataFrame(data)

df.columns = ["ID","F_NAME","L_NAME","AGE","PROF","LOC"]

print(df.sort_values(by='AGE',ascending=False).head(10)[df.columns[1:]])