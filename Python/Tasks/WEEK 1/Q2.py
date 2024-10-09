

def is_valid(string):

    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = '1234567890'

    first_chars = alphabets + '_'
    all_chars = alphabets + digits + '_'

    if string[0] in first_chars:
        if_valid=True
        for i in string[1:]:
            if i not in all_chars:
                if_valid=False
                break
        if if_valid:

            return True
        else:
            return False
    
    return False


def find_valid(s):

    list_identifier = s.split()

    valid_identifiers = []

    for i in list_identifier:
        if is_valid(i):
            valid_identifiers.append(i)

    return valid_identifiers



s = input("Enter a string \n")

print(f"The valid identifiers in the given string are \n {find_valid(s)}")











