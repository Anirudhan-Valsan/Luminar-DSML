import pandas as pd

a = pd.Series({"eid":111,"name":"Anirudhan","lname":"Valsan","age":25,"prof":"ML Engineer","Salary":100000},index = ["age","eid","prof","name","lname","Salary"])

print(a)
print("*"*100)
print(a.head())