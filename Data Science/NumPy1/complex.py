import numpy as np


a = np.array([[1,2,3,8],[3,4,5,4],[3,4,5,6]],dtype=complex)
print(a)
print()
b = a.reshape([4,3])
print(b)