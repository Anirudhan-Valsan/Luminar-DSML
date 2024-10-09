

n1=int(input("Enter a number\t"))
n2=int(input("Enter second number\t"))
n3=int(input("Enter third number\t"))

sum = lambda a,b,c : a+b+c

print(f"The sum of the three numbers {n1}, {n2}, {n3} is ",sum(n1,n2,n3))