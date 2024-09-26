#9) sum of odd and even indexed digits in a number


def sum_digit(num):
    odd=str(num)[0::2]
    even=str(num)[1::2]

    odd_sum=0
    even_sum=0

    for i in range(len(odd)):
        odd_sum+=int(odd[i])
    for i in range(len(even)):
        even_sum+=int(even[i])

    print(f"Sum of odd index digits is {odd_sum} \n\t\tand\n even indexed digits is {even_sum}")





n=int(input("enter a number\t"))
sum_digit(n)