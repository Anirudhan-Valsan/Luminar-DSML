#6)Python program to check the validity of password input by users.

def is_valid_password(password):
    if len(password) < 8:
        return False

    has_lower = has_upper = has_digit = has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in '@#$%^&+=':
            has_special = True
        if has_lower and has_upper and has_digit and has_special:
            return True

    return False


password = input("Enter a password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
