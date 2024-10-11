num=int(input("Enter a number\t"))

temp=str(num)

print(f"{num} is a palindrome ") if num==int(temp[::-1]) else print(f"{num} is not a palindrome")



