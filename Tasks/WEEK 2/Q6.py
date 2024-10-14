"""
Q6. Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
    Note:
        An equilateral triangle is a triangle in which all three sides are equal.
        A scalene triangle is a triangle that has three unequal sides.
        An isosceles triangle is a triangle with (at least) two equal sides.
"""

def check_triangle(a,b,c):

    if a == b and b == c and a == c:

        print("Equilateral")

    elif a != b and a!=c and b!=c:

        print("Scalene")

    elif a == b or b == c or a == c:

        print("Isosceles")


a = int(input("enter the first side\t"))
b = int(input("enter the second side\t"))
c = int(input("enter the third side\t"))

check_triangle(a,b,c)