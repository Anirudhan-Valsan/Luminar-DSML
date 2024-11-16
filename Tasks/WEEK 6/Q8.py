def consecutive(nums):
    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] > 1:
            for j in range(1, nums[i+1] - nums[i]):
                print(nums[i] + j)


nums = [1, 2, 3, 5, 6, 7]
consecutive(nums)
