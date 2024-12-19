import pandas as pd



df = pd.read_csv('C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Machine Learning/DataSets/mushroom_cleaned.csv')

print(df.head())

print(df.tail())

print(df.isna().sum())


print(df.dtypes)


x = df.drop('class',axis=1)
y = df['class']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30,random_state=42)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

sc.fit(x_train)

x_train = sc.transform(x_train)

x_test = sc.transform(x_test)

from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
gb = GaussianNB()

knn = KNeighborsClassifier(n_neighbors=5)
sv = SVC()
models = [gb,knn,sv]

from sklearn.metrics import accuracy_score as ac,confusion_matrix as cm,classification_report as cr
predictions = {}
performance = {}
for model in models:
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    predictions[model] = y_pred
    performance[model] = {'accuracy' : ac(y_test,predictions[model]),'confusion matrix':cm(y_test,y_pred) ,'classification report':cr(y_test,y_pred)}

for i in performance:
    print(i,'\n',performance[i],'\n')



