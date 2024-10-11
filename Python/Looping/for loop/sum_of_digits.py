#sum of digits of a number


number = int(input("Enter a number\n"))
sum=0
for i in str(number):
    sum = sum + int(i)

print(sum)