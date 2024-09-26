#Write a function that capitalizes the first and fourth letters of a name


def capitalize(name):
    result=""
    result=name[0].upper()+name[1:3]+name[3].upper()+name[4:]
    print(f"The resultant string is  ",result)

name=input("Enter a Name\t")
capitalize(name)
