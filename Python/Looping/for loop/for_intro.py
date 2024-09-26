#range returns a sequence of numbers
#range(start,stop,step)
'''seq = range(1,15)

for i in seq:
    print(i,end=" ")'''

name=input("enter the name\n")
vowels="aeiou"

for i in name.lower():
    if i in vowels:
        print(i,end=" ")
    else:
        break
    
print("none")