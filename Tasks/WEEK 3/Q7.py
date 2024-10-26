'''
7)Write a program to accept a number and check whether its a perfect number or not. 
Perfect number is a number which is equal to sum of its divisors. For ex: 6, its divisors are 1,2,3.
 So sum of divisors 1+2+3 is also 6

'''

def is_perfect(number):
    if number<=0:
        return False
    sum_div = sum(div for div in range(1,number) if number%div==0)

    if sum_div == number:
        print(f"{number} is a perfect number")
    else:
        print("Not perfect")

number = int(input("Enter the number\t"))
is_perfect(number)