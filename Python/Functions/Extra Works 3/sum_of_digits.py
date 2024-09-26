# 2) sum of digits of a positive integer entered

def sum_d(n):
    sum=0
    for i in str(n):
        sum+=int(i)

    print(f"The sum of the digits of {n} is {sum}")


num=int(input("Enter a Positive integer\t"))
if num>0:
    sum_d(num)
else:
    print("Please enter a positive integer ")
