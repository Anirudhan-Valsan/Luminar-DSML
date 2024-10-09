string = input("Enter the string\n")

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = '1234567890'

first_chars = alphabets + '_'
all_chars = alphabets + digits + '_'

if string[0] in first_chars:
    is_valid=True
    for i in string[1:]:
        if i not in all_chars:
            is_valid=False
            break
    if is_valid:

        print("The string is a valid identifier\n")
    else:
        print("The string is not a valid identifier")
        
else:

    print("The String is not a valid identifier\t")