'''
A number is called perfect if the sum of proper divisors of that number is equal to the number. 
For example 28 is perfect number, since 1+2+4+7+14=28.
Write a program to print all the perfect numbers in a given range 
'''
def sum_div(n):
    sum=0
    for i in range(1,n+1):
        if (n%i==0) and (i!=n):
            sum+=i
    return(sum)

def perfect(lower,upper):
    print(f"The series of perfect numbers between {lower} and {upper} are \t")
    for i in range(lower,upper+1):
        if sum_div(i)==i:
            print(i,end=" ")



lim1=int(input("Enter the lower limit\t"))
lim2=int(input("Enter the upper limit\t"))
perfect(lim1,lim2)