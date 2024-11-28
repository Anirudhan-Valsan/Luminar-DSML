"""
Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list. For example,
if you pass '23569' as an argument,
your function should return 9. Use list comprehension..

"""

def biggest_odd(nums):
    odd = []

    for i in nums:
        if int(i) %2 !=0:
            odd.append(int(i))
    sort_odd = sorted(odd)

    return sort_odd[-1]


nums = '23569'

print(biggest_odd(nums))
