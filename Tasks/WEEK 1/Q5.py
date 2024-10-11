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

print("The largest number in the list is ",max(num_list), "and the minimum number is ",min(num_list))