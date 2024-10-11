#sum of squares of even digits in a number

num=int(input("Enter a number\n"))

sum=0

for i in str(num):
    if int(i)%2==0:
        sum=sum+(int(i)**2)


print(sum)