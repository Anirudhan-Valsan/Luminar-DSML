'''
4)Write a Python program to generate all possible valid identifiers of length n,
where n is provided by the user. Also take n values from user.
Then create possible identifiers
'''
#<--------------------------------------------------------------------------->

alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

first_chars = alphabets + '_'
all_chars = alphabets + digits + '_'

#<--------------------------------------------------------------------------->

def is_valid_identifier(string):

    if not string:
        return False

    if string[0] not in first_chars:
        return False
    for char in string[1:]:
        if char not in all_chars:
            return False
    return True 

#<--------------------------------------------------------------------------->

def generate_valid_identifiers(n,user_values):

    identifiers = []

    def combination(identifier,length):

        if length == n:

            if is_valid_identifier(identifier):
                identifiers.append(identifier)
            return
            
        
        if length == 0:
            for i in user_values:
                if i in first_chars:
                    combination(identifier+i,length+1)
        else:

            for i in user_values:
                if i in all_chars:
                    combination(identifier+i,length+1)

    combination('',0)
    return identifiers
    
#<--------------------------------------------------------------------------->

n = int(input("Enter the desired length of valid identifier: "))

user_values = []

for i in range(n):

    user_input = input(f"Enter  character {i+1}: ")
    if user_input in all_chars:
        user_values.append(user_input)
    else:
        print(f"character {i+1} is Not a valid character\n")

result = generate_valid_identifiers(n,user_values)

print(f"The possible valid identifiers of length {n} from the given characters are \n<------------------------------------------------------------------------->\n")

for i in result:

    print(i,end=", ")




