"""
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
"""
p=6
for i in range(1,6):
    for j in range(p):
        print(j,end=" ")
    p-=1
    print()
