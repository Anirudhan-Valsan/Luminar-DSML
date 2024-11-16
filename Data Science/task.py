
import numpy as np

f = open("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/customer1.txt", "r")
data = []
for line in f:
    data.append(line.strip('\n').split(','))

f.close()


for i in data:
    if i[4] == "Actor" and int(i[3])>50:
        print(i[1:5])