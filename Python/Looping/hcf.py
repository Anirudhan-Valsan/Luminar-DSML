num1=int(input("enter the first number\n"))
num2=int(input("Enter the second number\n"))


if num1<num2:
    num1,num2=num2,num1

while(num2!=0):
    remainder=num1%num2
    num1=num2
    num2=remainder

print(f"The Hcf is {num1}")