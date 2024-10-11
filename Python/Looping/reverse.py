n=int(input("enter the number\n"))
reverse=""
while(n>0):
    digit=n%10
    reverse+=f"{digit}"
    n=n//10

print(reverse)