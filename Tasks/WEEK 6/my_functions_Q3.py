def string_manipulation(s):
    vowels = "aeiouAEIOU"
    num = 0
    for i in vowels:
        if i in s:
            num+=1

    print(f"The number of vowels is {num}")
    print(f"The reversed string is {s[::-1]}")