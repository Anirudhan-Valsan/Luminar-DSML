#A function to reverse a number


def reverse(num):
    print(f"The reverse of {num} is :-",int(str(num)[::-1]))


n=int(input("Enter a number\t"))
reverse(n)