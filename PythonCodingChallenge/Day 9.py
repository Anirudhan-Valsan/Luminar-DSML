"""
Day 9: Biggest Odd Number
Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list.
For example, if you pass '23569' as an argument, your function should return 9. Use list comprehension.
"""

def biggest_odd(num):

    return max([int(x) for x in num if int(x)%2!=0])

print(biggest_odd(input("Enter a string of numbers\t")))