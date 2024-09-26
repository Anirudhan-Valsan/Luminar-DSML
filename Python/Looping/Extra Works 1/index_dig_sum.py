#wap to print sum of even and odd indexed digits in a given number

num=int(input("Enter a number\t"))

odd=str(num)[0::2]
even=str(num)[1::2]

odd_sum=0
ev_sum=0

for i in range(len(odd)):
    odd_sum+=int(odd[i])
for i in range(len(even)):
    ev_sum+=int(even[i])

print(f"sum of odd indexed digits is {odd_sum}\nsum of even indexed digits is {ev_sum}")