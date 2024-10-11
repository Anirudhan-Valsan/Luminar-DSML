#8) print characters in even position


def even_char(string):
    for i in string[1::2]:
        print(i,end=" ")


string=input("Enter a string\t")
even_char(string)