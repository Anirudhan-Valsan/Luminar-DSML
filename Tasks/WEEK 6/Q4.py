import calculator_Q4 as cal

def calc(choice):
    if choice == "+":
        a = int(input("Enter the first number\t"))
        print("---------------------------------------------------------------")
        b = int(input("Enter the second number\t"))
        result = cal.add(a,b)
        print("---------------------------------------------------------------")
        print(f"Result = {result}")



    elif choice == "*":
        a = int(input("Enter the first number\t"))
        print("---------------------------------------------------------------")
        b = int(input("Enter the second number\t"))
        result = cal.mul(a,b)
        print("---------------------------------------------------------------")
        print(f"Result = {result}")



    elif choice == "-":
        a = int(input("Enter the first number\t"))
        print("---------------------------------------------------------------")
        b = int(input("Enter the second number\t"))
        result = cal.sub(a,b)
        print("---------------------------------------------------------------")
        print(f"Result = {result}")



    elif choice == "/":
        a = int(input("Enter the first number\t"))
        print("---------------------------------------------------------------")
        b = int(input("Enter the second number\t"))
        result = cal.div(a,b)
        print("---------------------------------------------------------------")
        print(f"Result = {result}")




print("\n<----------------------CALCULATOR-------------------------------->\n")

start = input("Start Calculator ? \t y/n\t")

while start == 'y':
    print("---------------------------------------------------------------")
    print("Select the operation to perform\t + , * , - , /")
    choice = input()
    calc(choice)
    print("----------------------------------------------------------------")
    start = input("Do you want to use the calculator again? \t y/n\t")

print("---------------------------------------------------------------")
print("Thank You For Using")

