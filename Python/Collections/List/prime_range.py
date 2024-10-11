def is_Prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True 

def print_prime(a,b):
    prime=[]
    for i in range(a,b+1):
        if is_Prime(i):
            prime.append(i)
    return prime


a=int(input("Enter the lower limit\t"))
b=int(input("enter the upper limit\t"))

print(print_prime(a,b))


