# count the number of odd digits in a number

n=int(input("enter a number\n"))

count=0

for i in str(n):
    if int(i)% 2!=0:
        count+=1

print(f"The number of odd digits in the number {n} is {count}")