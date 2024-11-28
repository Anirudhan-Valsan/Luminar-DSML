# Remove empty strings from the list of strings
# Given:
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Output:
# ["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

print([i for i in list1 if len(i)!=0 ])