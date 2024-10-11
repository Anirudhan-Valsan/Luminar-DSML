
a=int(input("Enter a number\t"))

result=lambda a:a**2 if a%2==0 else a**3

print("The result is ",result(a))