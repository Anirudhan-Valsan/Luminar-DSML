def string_range(n):
    return '0' if n == 1  else  string_range(n-1) + '.' + str(n-1)

print(string_range(int(input("Enter the range\t"))))


