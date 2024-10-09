"""
10)Write a function to calculate the factorial of a number recursively
"""

def factorial(n):

    if (n == 0):

        return 1
    
    return n * factorial(n-1)


n = int(input("Enter a number\t"))

print(f"The factorial of {n} is {factorial(n)}")

