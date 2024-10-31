"""
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5

"""
p = 5
for i in range(6):
    for j in range(p):
        print("5",end=" ")
    p-=1
    print()