"""
             1
           1 2 1
         1 2 3 2 1
       1 2 3 4 3 2 1
"""
n = 5

p = n

for i in range(5):
    for j in range(p):
        print(" ",end=" ")
    p-=1
    for s in range(1,i+1):
        print(s,end=" ")
    for q in range(i-1,0,-1):
        print(q,end=" ")
    print()


