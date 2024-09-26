


num1=int(input("Enter a number\n"))
num2=int(input("Enter another number\n"))

total=0

total=num1+num2

choice="y"

while(choice=="y"):

    num3=int(input("Enter another number\n"))

    choice=input("do you want to add another number?: y/n \n")

    total+=num3

print(f"The total is {total}")
