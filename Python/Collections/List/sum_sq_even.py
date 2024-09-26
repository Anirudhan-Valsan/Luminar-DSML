'''nums=[1,2,9,65,4,3,7,6]

for i in nums:
    sum=0
    if i%2==0:
        sum+=i**2

print(f"The sum of squares of even numbers in list is {sum}")        
'''

nums=[1,2,9,65,4,3,7,6]

for i in range(3):
    last=nums.pop()
    nums.insert(0,last)

print(nums)