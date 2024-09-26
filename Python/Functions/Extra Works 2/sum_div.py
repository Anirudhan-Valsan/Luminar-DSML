''' Write a function that finds the sum of proper divisors of a number. 
    Proper divisors of a number are those numbers by which the number is divisible, 
    except the number itself. For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18
'''

def sum_div(n):
    sum=0
    print(f"The perfect divisors of {n} are ",end=" ")
    for i in range(1,n+1):
        if (n%i==0) and (i!=n):
            sum+=i
            print(i,end=" ")
    print(f"\nThe sum of perfect divisors of {n} is {sum}")



num=int(input("Enter a number\t"))
sum_div(num)