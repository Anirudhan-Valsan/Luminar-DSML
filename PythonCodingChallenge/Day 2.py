
def convert_add(string_list):
    if not string_list:
        return 0
    else:
        return int(string_list[0]) + convert_add(string_list[1:])

print('Sum = ',convert_add(input('Enter numbers\n').split(' ')))
