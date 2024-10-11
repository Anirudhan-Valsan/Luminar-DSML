# largest among 3 nums

n1 = int(input("Enter first number\n"))
n2 = int(input("Enter second number\n"))
n3 = int(input("Enter third number\n"))

if n1>n2 and n1>n3:
    print(f"{n1} is greatest")

elif n2>n1 and n2>n3:
    print(f"{n2} is greatest")
    
else:
    print(f"{n3} is greatest")