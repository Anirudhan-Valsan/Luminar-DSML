'''
Q7. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
Like:
Enter First Number: 7
Enter Second Number: 9
Enter operator : +
Your Answer is: 16

'''

def mathematical(a,b,op):

    result = a+b if op =='+' else (a-b if op == '-' else (a*b if op == '*' else(a/b if op == '/' else (a%b if op == '%' else "Not a valid operator"))))
    return result

a = int(input("enter the first number\t"))
b = int(input("enter the second number\t"))
op = input("Enter the operator ( + , - ,  * ,  / , %)\t")

print(f"{a} {op} {b} = {mathematical(a,b,op)}")