n1=int(input("Enter the limit\t"))
n2=int(input("Enter the limit\t"))

for i in range(n1,n2+1):

    temp=str(i)
    power=len(temp)
    p=power
    sum=0

    while(p>0):

        sum+=int(temp[p-1])**power
        i-=1

        