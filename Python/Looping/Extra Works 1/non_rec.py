'''
Given a pattern
 Text=”ABABC”
 Write a program to print first non-recursive character output=c without using nested loop
'''

text=input("Enter a String\t")
result=""
for i in text:
    if text.count(i)==1:
        print(i)
        break




