'''
9)Write a program that takes inputs from user and prints the multiplication
table of that number

'''

def multi_table(n,i=1):

    if i>10:

        return 
    
    print(f"{n} * {i} = {n*i}")

    multi_table(n,i+1)


n = int(input("Enter a number\t"))
multi_table(n)