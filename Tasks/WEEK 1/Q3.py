'''

3)Write a Python program that takes three numbers as input from the user and prints out the sum of those numbers.

'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

sum = lambda a, b, c: a + b + c
print("Sum of three numbers is: ", sum(a, b, c))