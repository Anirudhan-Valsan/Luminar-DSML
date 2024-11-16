num_list = [1,2,3,-2,4]
sum = 0
for i in num_list:
    if i<0:
        continue
    sum+=i

print(sum)