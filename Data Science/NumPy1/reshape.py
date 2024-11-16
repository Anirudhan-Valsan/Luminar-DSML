import numpy as np


a = np.array([[3,2,1,5,2],[1,2,3,4,5],[6,3,7,8,4],[2,6,3,8,9]],dtype=int)
print(a)

print()

b = a.reshape([5,4])
print(b)
print()

c = a.reshape([2,10])
print(c)
print()

d = a.reshape([10,2])
print(d)