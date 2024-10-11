'''
Given a pattern text=”ABEABAIACB”
   Write a program to print most recursive consonant from above text 
   Output=B

'''
text=input("Enter a string\t")

vowels="aeiouAEIOU"

str_count=""
rec_str=''


for i in text:
    if i not in vowels and text.count(i)>1 and i not in rec_str:
        str_count+=str(text.count(i))
        rec_str+=i

max_count=0
most_recurring=''

for i in range(len(rec_str)):
    if int(str_count[i])>max_count:
        max_count=int(str_count[i])
        most_recurring=rec_str[i]

print("The most recurring consonant is ",most_recurring,"  with  ",max_count, " occurences") if most_recurring else print("No consonant is present with more than one occurence")
