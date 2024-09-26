#Given an integer n, return True if n is within 10 of either 100 or 200

def check_within(n):
    print("True") if (90<=n<=110) or (190<=n<=210) else print("False")
        

num=int(input("Enter a number\t"))
check_within(num)