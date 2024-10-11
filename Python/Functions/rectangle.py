'''
Write a Python function area(length, width) that calculates the area of a rectangle. 
If only the length is provided, the function should return the area of a square (assuming length = width).
 If both length and width are provided, it should return the area of the rectangle
'''
'''
def area():
    length=float(input("enter the length\t"))
    width_in=input("Enter the width  \t")

    if width_in=="":
        width=length
    
    else:
        width=float(width_in)

    return(length*width)



print("The area is ",area())

'''


def area(length,width=None):
    if width==None:
        width=length
    return length*width

l=float(input("Enter the length\t"))
w=float(input("Enter the width\t"))
print("area is ",area(l,w))