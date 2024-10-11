def isPrime(n):
    
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True


num=int(input("enter a number\t"))
res=isPrime(num)
if res:
    print("Prime")
else:
    print("not prime")