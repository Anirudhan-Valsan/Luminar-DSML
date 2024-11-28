"""

Bank domain:

Design a program for the bank domain where there are unlimited denominations of coins (e.g., 1, 2, 5, 10).
 The program takes an amount as input (e.g., 7) and calculates the minimum number of coins needed to sum up to that amount.
For instance, if the input is 7, the output should be 2, as the minimum number of coins to make 7 is 2 (using one 5-coin and one 2-coin).



"""



n = int(input("Enter a number\t"))

coins = [1, 2, 5, 10]
numbers = []
result = []

for i in range(len(coins)):
    if n == i:
        print(1)
    else:
        for j in range(i + 1):
            if i + j == n:
                numbers = [str(i) + str(j)]
    for j in numbers:
        nums = [len(j)]
        result = nums.sort()

print(result)






