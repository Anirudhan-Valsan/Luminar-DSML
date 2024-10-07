string=input("Enter a string\t")

identifiers = string.split()

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("The valid identifiers in the given string are \n")

for i in identifiers:

    if i[0] in alphabets or i[0] == "_":

        print(i)






