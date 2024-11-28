# Q1. Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list,
# then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
# Given:
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Output
# ['My', 'name', 'is', 'Kelly']

list1 = ['M','na','i','Ke']
list2 = ['y','me','s','lly']
op = []
if len(list1) == len(list2):
    for i in range(len(list1)):
        op.append(list1[i]+list2[i])
else:
    if len(list1) > len(list2):
        diff = len(list1) - len(list2)
        for x in range(diff):
            list2.append('')
    else:
        diff = len(list2) - len(list1)
        for y in range(diff):
            list1.append('')

    for i in range(len(list1)):
        op.append(list1[i]+list2[i])

print(op)