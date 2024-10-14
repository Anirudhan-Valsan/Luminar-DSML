# Q2)  Write a program to check whether given year is leap year or not

def is_leap(x):

    print(f"{x} Is a Leap Year") if (x % 4 == 0 and x % 100 != 0 ) or (x % 400 == 0) else print(f"{x} is not a leap year")

year = int(input("Enter the year to check \t"))
is_leap(year)