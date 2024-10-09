'''

6)Write a Python program that takes two numbers as input from the user 
and performs arithmetic operations 
(addition, subtraction, multiplication, division, and modulus) 
on them. Display the results of each operation

'''

def arithmetic():

    x = int(input("Enter the first number\t"))
    y = int(input("Enter the second number\t"))

    print(f"{x} + {y} = {x+y}")
    print(f"{x} - {y} = {x-y}")
    print(f"{x} * {y} = {x*y}")
    print(f"{x} / {y} = {x/y}")
    print(f"{x} % {y} = {x%y}")




arithmetic()