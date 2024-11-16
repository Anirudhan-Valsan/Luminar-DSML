import numpy as np
"""
a = np.array([6,0,9,4,2,8,7,1,15,12,11])
b = np.array([1,2,3,4,5,6,7,8])
c = np.concat((a,b))
print(c)
"""

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
brr = np.array([[11,12,13],[14,15,16],[17,18,19]])

crr = np.concat((arr,brr),axis=1)

print(crr)
