
head=[1,4,6,7,8,9]

length=len(head)

i=1


while(i<length):
    head.insert(i,head.pop(-1))
    i+=2



print(head)
