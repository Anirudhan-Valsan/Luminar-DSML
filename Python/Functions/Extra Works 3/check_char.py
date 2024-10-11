#6) check vowel or consonant

def check_char(string):
    vowels="aeiouAEIOU"
    
    print("vowel") if string in vowels else print("consonant")


string=input("Enter a character\t")
check_char(string)