"""
* * * *
* * *
* *
*
* *
* * *
* * * *

"""
n = 4
p = n
for i in range(1,5):
    while p >= 1:
        for j in range(p):
            print("*",end=" ")
        p-=1
        print("\n")
    else:
        for j in range(i):
            print("*",end=" ")
        print("\n")
