'''
8) Create a Python program that prompts the user to enter their age 
and checks if they are eligible to vote.
Use logical operators to check if the age is greater than
or equal to 18 and less than or equal to 120.
Print a message indicating whether the person can vote or not.

'''

def check_eligible():

    age = int(input("Enter Your Age\t"))

    print("\nYou're eligible to Vote ") if (18<=age<=120) else print("\nYou are Not Eligible to Vote")


check_eligible()




