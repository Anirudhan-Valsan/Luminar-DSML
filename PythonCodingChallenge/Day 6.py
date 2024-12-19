
def user_name():
    try:
        email = input("Enter Your Email :   ")
        if '@' not in email:
            raise ValueError('Not a valid email')
        return f'Username : {email.split('@')[0]}'
    except ValueError as e:
        return e

print(user_name())




