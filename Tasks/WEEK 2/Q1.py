#  Q1)  Write program to check a number is even or odd


def even_odd(x):

    print(f"{x} is Even ") if x%2 == 0 else print(f"{x} is Odd") 

num = int(input("Enter a number \t"))
even_odd(num)