def register_check(register):
    count = 0
    for i in register:
        if register[i] == 'yes':
            count+=1
    return count

register = {'Michael':'yes','John':'no',
'Peter':'yes', 'Mary':'yes'}

print(register_check(register))