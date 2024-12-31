def odd_even(numbers):
    return max([num for num in numbers if num % 2 == 0]) - min([num for num in numbers if num % 2 != 0])

print(odd_even(list(map(int, input('Enter a list of numbers separated by spaces: ').split()))))




