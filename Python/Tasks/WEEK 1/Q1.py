string = input("Enter the string\n")

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

if string[0] in alphabets or (string[0] == "_"):

    print("The string is a valid identifier\n")

else:

    print("The String is not a valid identifier\t")