#to print the no of digits in the number enter by user

"""n=int(input("Enter the number\n"))
temp=n
count=0
while (n>0):
    
    digit= n % 10
    count+=1
    n=n//10

print(f"The number of digits in the number {temp} is {count}")"""

n=int(input("Enter the number\n"))          # taking input

num_string=f"{n}"       #convert to string

digits=len(num_string)          #taking length

print(f"The number of digits is {digits}")