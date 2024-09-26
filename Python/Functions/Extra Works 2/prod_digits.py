#Write a function  that inputs a number and returns the product of digits of that number.


def prod_digit(n):
    product=1
    for i in range(len(str(n))):
        product*=int(str(n)[i])
    print(f"The product of digits of {n} is {product}")



num=int(input("Enter a nuber\t"))
prod_digit(num)
