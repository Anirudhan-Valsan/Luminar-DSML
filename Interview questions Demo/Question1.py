"""
Encryption question:

Create a program that takes a number as input (e.g., 2) and an alphabet letter (either uppercase or lowercase).
The output should be the letter that is the given number of positions ahead of the input letter in the alphabet.
For example, if the input is 2 and the letter is 'A', the output should be 'C'. Similarly, for lowercase letters,
 if the input is 2 and the letter is 'a', the output should be 'c'.


"""

alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

n = int(input("Enter a number\t"))

s = input("Enter the alphabet\t")

if s.upper() in alphabets:

    result = alphabets[alphabets.index(s.upper())+n]
    if s == s.upper():
        print(result)
    else:
        print(result.lower())

