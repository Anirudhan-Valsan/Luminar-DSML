alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

def is_valid_identifier(string):

    if string[0] in alphabets or digits or string[0] == "_":

        for i in string[1:]:

            if not (i in alphabets or digits or i == "_"):
                
                return False
            
            return True
        
        return False


def generate_identifier(n,limit):

    all_char = alphabets + digits + "_"
    first_chars = alphabets + '_'

    identifiers=[]

    