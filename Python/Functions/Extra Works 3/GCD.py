# 4) GCd

def gcd(num1,num2):
    temp1,temp2=num1,num2
    if num1<num2:
        num1,num2=num2,num1 
    
    while(num2!=0):
        remainder=num1%num2
        num1=num2
        num2=remainder
    print(f"The Greatest common divisor of {temp1} and {temp2} is {num1}")


num1=int(input("enter first number\t"))
num2=int(input("enter second number\t"))
gcd(num1,num2)