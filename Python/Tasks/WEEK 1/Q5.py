size=int(input("Enter the size of the list\t"))
print("Enter the list of numbers\n")

num_list = []

for i in range(size):

    num = int(input())
    num_list.append(num)

print("The largest number in the list is ",max(num_list), "and the minimum number is ",min(num_list))