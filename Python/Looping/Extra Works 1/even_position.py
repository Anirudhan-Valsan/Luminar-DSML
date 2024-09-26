#wap to print the characters of a string in even positions. >>>      name= "python"    o/p = y h n

'''string=input("Enter a string\t")

result=''
for i in string:
    if (string.index(i)+1)%2==0:
        result+=i
print(result)'''     

''' >>>>-----------------------------------------------OR-----------------------------------------<<<<'''

string=input("Enter a string\t")

print(string[1::2])
