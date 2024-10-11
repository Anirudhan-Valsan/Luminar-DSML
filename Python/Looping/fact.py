num=int(input("Enter the num to find fact\n"))

i=1
fact=1
while(i<num):
    fact*=i
    i+=1
print(f"The factorial is {fact}")