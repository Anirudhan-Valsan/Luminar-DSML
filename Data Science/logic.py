lst = [1,3,5,4,3,5,6,7,9,7,5,4,8,9,10,7,5,4]

#op = [1,5,3,9,4,10]
op = []
for i in range(len(lst)):
    if  lst[i] < lst[i+1]:
        op.append(lst[i])

print(op)