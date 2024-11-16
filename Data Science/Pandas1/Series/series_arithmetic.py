import pandas as pd

a = pd.Series([2,3,4,5,6])
b = pd.Series([1,3,9,8,7])

sum1 = a.add(b)
print(sum1)
print("*"*100)

diff = a.subtract(b)
print(diff)
print("*"*100)

prod = a.multiply(b)
print(prod)
print("*"*100)

div = a.divide(b)
print(div)
print("*"*100)

mod  = a.mod(b)
print(mod)
print("*"*100)

c = a._append(b,ignore_index=True)

print(c)