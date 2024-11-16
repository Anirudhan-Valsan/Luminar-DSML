from mypackageQ2 import module1 as m1
from mypackageQ2 import module2 as m2

a = int(input("Enter the first number\t"))
b = int(input("Enter the second number\t"))

s = m1.sum_of(a,b)
d = m2.diff(a,b)

print(f"The Sum is {s} and the difference is {d}")