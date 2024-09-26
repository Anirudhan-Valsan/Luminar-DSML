#sum of first n numbers


n=int(input("Enter the number\n"))

sum=0

for i in range(n+1):
    sum+=i

print(f"The sum of first {n} numbers is {sum}")