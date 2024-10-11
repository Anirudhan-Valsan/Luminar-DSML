#nums divisible by 3 and 5 from 10 to 100

print("The number divisible by bot 3 and 5 are\n------------------------------------------")

for i in range(10,101):

    if i%3==0 and i%5==0:

        print(i,end=" ")