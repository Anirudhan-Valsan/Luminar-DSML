"""

1: implement a function to encode a given string by the following manner
car - ect
c -3 becomes  e-5 .
+2 for each alphabet
"""
def encode(s):
    new_word = ''
    alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in s:
        if i.upper() in alphabets:
            new_word += alphabets[alphabets.index(i.upper())+2]
    if s.upper == new_word:
        print(new_word)
    else:
        print(new_word.lower())

s = input("Enter a word\t")
encode(s)

