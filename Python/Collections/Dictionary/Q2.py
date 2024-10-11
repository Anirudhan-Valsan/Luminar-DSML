#op result=[10,10,16,3]


items={2:8,4:6,7:9,1:2}
sum_list=[]

for i in items.keys():
        sum=i+items[i]
        sum_list.append(sum)


print(sum_list)


