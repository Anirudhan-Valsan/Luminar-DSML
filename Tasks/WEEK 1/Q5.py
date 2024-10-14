'''
5) Write a Python program that takes a list of numbers as input from the user
and prints out the maximum and minimum numbers in the list.

'''


size=int(input("Enter the size of the list\t"))
print("Enter the list of numbers\n")

num_list = []

for i in range(size):

    num = int(input())
    num_list.append(num)

max = num_list[0]
min = num_list[0]

for num in num_list:
    if num > max:
        max = num
    if num < min:
        min = num

print(f"The largest number in the list is {max} and smallest is {min}")