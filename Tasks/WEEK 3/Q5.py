#5)Python program to display all numbers within a range except the prime numbers.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def display_non_primes(start, end):
    non_primes = [num for num in range(start, end + 1) if not is_prime(num)]
    return non_primes

start = int(input("Enter the lower range\t"))
end = int(input("Enter the upper range\t"))

print(display_non_primes(start,end))

