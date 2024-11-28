# Given a list of numbers. write a program to turn every item of a list into its square.s
# Given:
# numbers = [1, 2, 3, 4, 5, 6, 71]
# Output:
# [1, 4, 9, 16, 25, 36, 49]

numbers = [1, 2, 3, 4, 5, 6, 7]

print(list(map(lambda x: x**2,numbers)))