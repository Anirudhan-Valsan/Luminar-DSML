# Q10) Take values of length and breadth of a rectangle from user and check if it is square or not.

def is_square(a,b):

    return 'Is Square' if a == b else 'Not square'

l = int(input("enter the length of the rectangle\t")) 
b = int(input("enter the breadth of the rectangle\t"))

print(is_square(l,b))