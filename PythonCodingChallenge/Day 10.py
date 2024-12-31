def hide_password():
    passwd = input('Enter password\t')
    return f"The password {'*'*len(passwd)} is {len(passwd)} characters long"

print(hide_password())