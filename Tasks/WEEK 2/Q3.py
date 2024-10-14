# Q3) Write a program to find greatest number among three numbers

def greatest(nums):
    
    greatest = nums[0]

    for i in nums:
        if i > greatest:
            greatest = i

    return greatest

print("Enter three numbers to check greatest\n")
nums = []
for i in range(3):
    num = int(input())
    nums.append(num)

print(f"The greatest of {nums} is :\t {greatest(nums)}")

