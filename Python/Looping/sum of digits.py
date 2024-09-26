#sum of digits of a number

n=int(input("enter the number\n"))
temp=n
sum=0

while (n>0):
    sum+=n%10
    n//=10

print(f"The sum of digits of the number {temp} is {sum}")