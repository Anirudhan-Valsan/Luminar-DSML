#1)Print numbers divisible by 3 or 5 from 1 to 20 using a for loop

x = [i for i in range(1,21) if i%3==0 or i%5==0]

print(x)