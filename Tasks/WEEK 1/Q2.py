'''
2) Write a Python program to find all the valid identifiers in a given string.
    Assume that identifiers are separated by spaces.

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

def find_valid_identifiers(s):

    valid_identifiers = []
    for i in s.split():
        if is_valid_identifier(i):
            valid_identifiers.append(i)
    return valid_identifiers


s = input("Enter a string\t")
print(find_valid_identifiers(s))