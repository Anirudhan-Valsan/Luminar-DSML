def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter a Number\t"))
fib = []
for i in range(n+1):
    fib.append(fibonacci(i))

print(f"The value at position {n} in a fibonacci series is {fib[n-1]}")