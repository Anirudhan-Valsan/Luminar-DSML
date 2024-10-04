#print sum of key and value if key is even in list comprehension

dict={2:8,4:6,6:8,1:4,3:5}


sum_list=[i+dict[i] for i in dict.keys() if i%2==0]


print(sum_list)