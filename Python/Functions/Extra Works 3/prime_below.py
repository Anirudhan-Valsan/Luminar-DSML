#7) prime numbers below n


def is_Prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True
        
def print_prime(num):
    for i in range(2,num):
        if is_Prime(i):
            print(i,end=" ")


n=int(input("enter a number\t"))
print_prime(n)
    