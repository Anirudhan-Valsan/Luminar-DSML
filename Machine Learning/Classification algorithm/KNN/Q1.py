import pandas as pd
from click import clear
from sklearn.neighbors import KNeighborsClassifier



data = {"Points":['p1','p2','p3','p4'],'x1':[7,7,3,1],'y1':[7,4,4,4],'output':['good','good','bad','bad']}
df = pd.DataFrame(data)

x1  = df['x1']
y1 = df['y1']

feature = list(zip(x1,y1))

target = ['good','good','bad','bad']

Knn =  KNeighborsClassifier(n_neighbors=3)

model = Knn.fit(feature,target)

x =3
y =7
test = list(zip([x],[y]))

result = model.predict(test)

print(result)














