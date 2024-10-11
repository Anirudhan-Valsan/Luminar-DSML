'''
1) Write a Python program to check if a given string is a valid identifier or not.
An identifier is valid if it starts with a letter (a-z, A-Z) or an underscore (_) followed by zero or more letters,
underscores, or digits (0-9).
'''

def is_valid_identifier(string):

    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'

    first_chars = alphabets + '_'
    all_chars = alphabets + digits + '_'

    if string[0] not in first_chars:
        return False
    for char in string[1:]:
        if char not in all_chars:
            return False
    return True 

string = input("Enter a string to check whether its valid identifier or not : ")
print(is_valid_identifier(string))
    

