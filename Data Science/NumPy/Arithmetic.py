import numpy as np

a = np.array([[3,4,5],[1,2,3],[6,5,4]])
b = np.array([[4,5,6],[4,1,2],[4,7,8]])

add = np.add(a,b)
mult = np.multiply(a,b)
sub = np.subtract(a,b)
div = np.divide(a,b)
sqr = np.square(a)
sqrt = np.sqrt(a)
dot = np.dot(a,b)

print(add)
print("*"*100)
print(sub)
print("*"*100)
print(mult)
print("*"*100)
print(div)
print("*"*100)
print(sqr)
print("*"*100)
print(sqrt)
print("*"*100)
print(dot)