'''
4)Write a Python program to generate all possible valid identifiers of length n,
where n is provided by the user. Also take n values from user.
Then create possible identifiers
'''

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

all_chars = alphabets + digits + '_'

def is_valid(string):

    if not string:

        return False
    
    if string[0] not in alphabets + '_':
        
        return False
    
    for i in string[1:]:

        if i not in (all_chars):

            return False
        
    return True
    
def generate_identifier(n):
    
    identifiers = []

    identifier = ''

    def combination(identifier,length):

        if length == n:
            if is_valid(identifier):
                identifiers.append(identifier)
            return           
        
        if length == 0:
            for i in alphabets+'_':
                combination(identifier+i,length + 1)
        else:

            for i in all_chars:
                combination(identifier+i,length + 1)

    combination(identifier,0)
    return identifiers

print("A Program to Generate possible valid identifiers\n-----------------------------------------\n")
n = int(input("Enter the desired length: "))

print(f"Possible valid identifier of length {n} is {generate_identifier(n)}")


    