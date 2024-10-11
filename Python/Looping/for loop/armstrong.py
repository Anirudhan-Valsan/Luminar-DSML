num=int(input("enter a number\t"))

temp=str(num)
power=len(temp)
i=power
sum=0

while(i>0):

    sum+=int(temp[i-1])**power
    i-=1

if num==sum:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")