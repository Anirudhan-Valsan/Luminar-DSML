import pandas as pd

data = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/missing_data.csv")

df = pd.DataFrame(data)

df.loc[7,'Duration'] = df['Duration'].mode()[0]

x = df['Calories'].mean()

for i in df.index:
    if df.loc[i,'Calories'] > 400:
        df.loc[i,'Calories'] = x        #to drop  df.drop(i,inplace = True,ignore_index = True)

print(df)

