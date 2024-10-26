#4)Python program to check if a given number is an Armstrong number

is_armstrong =  lambda num: num == sum(int(digit)**len(str(num)) for digit in str(num))

n = int(input("Enter a number\t"))

print(f"is {n} an armstrong number ? : {is_armstrong(n)}")

