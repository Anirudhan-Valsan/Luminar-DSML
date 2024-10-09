'''
7) Create a Python program that prompts the user to enter two numbers.
Compare the numbers using comparison operators (>, <, ==, !=, >=, <=) 
and print out the result of each comparison.

'''

def compare():

    x = int(input("Enter the first number\t"))
    y = int(input("Enter the second number\t"))

    print(f"{x} > {y} = {x>y}")
    print(f"{x} < {y} = {x<y}")
    print(f"{x} == {y} = {x==y}")
    print(f"{x} != {y} = {x!=y}")
    print(f"{x} >= {y} = {x>=y}")
    print(f"{x} <= {y} = {x<=y}")


compare()