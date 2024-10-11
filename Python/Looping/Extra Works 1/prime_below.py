#wap to find the prime numbers below n where n is entered by user
def isPrime(n):
    if n<=1:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True

def findPrime(num):
    for i in range(2,num):
        if isPrime(i):
            print(i,end=" ")
    

num=int(input("Enter a number\t"))

findPrime(num)


