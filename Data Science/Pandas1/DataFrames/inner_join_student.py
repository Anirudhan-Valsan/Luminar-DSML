# passed student name,rolno,result

import pandas as pd

data1 = pd.read_csv('C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/student.unknown',header=None)
df1 = pd.DataFrame(data1)
df1.columns=['name','roll']

data2 = pd.read_csv('C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/DataFrames/results.unknown',header=None)
df2 = pd.DataFrame(data2)
df2.columns = ['roll','result']

new_df = pd.merge(df1,df2,on='roll',how='inner')

print(new_df.loc[new_df['result'] == 'pass'][['name','roll','result']])