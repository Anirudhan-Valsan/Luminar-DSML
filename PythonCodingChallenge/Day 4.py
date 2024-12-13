def only_floats():
    a = input("Enter the first value: ")
    b = input("Enter the second value: ")
    count = 0
    try:
        if '.' in a:
            float(a)
            count += 1
    except ValueError:
        pass

    try:
        if '.' in b:
            float(b)
            count += 1
    except ValueError:
        pass

    return count


result = only_floats()
print(result)
