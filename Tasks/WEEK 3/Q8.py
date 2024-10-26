'''
8)Write a python program to print all permutations using those three variables Original Collection: [1, 2, 3] Collection of Permutation.
 [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1. 2]. [1. 3. 2]. [1, 2, 3]]
'''
def generate_permutations(nums,perm=[]):
    
    if not nums:
        permutations.append(perm)
    else:
        for i in range(len(nums)):
            generate_permutations(nums[:i]+nums[i+1:],perm+[nums[i]])



permutations = []

original_collection = [1,2,3]

generate_permutations(original_collection)

print(permutations)