n=int(input("Enter a number "))

if n%3 and n%7:
    print(f"{n} is divisible by both 3 and 7")
elif n%3 or n%7:
    print(f"{n} is divisible by either 3 or 7")
else:
    print("get out")


