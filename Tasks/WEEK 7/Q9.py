# Implement a function to check if a list is a palindrome

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        print('Is palindrome')
    else:
        print("Not a palindrome")


n = int(input("Enter a number\t"))
is_palindrome(n)