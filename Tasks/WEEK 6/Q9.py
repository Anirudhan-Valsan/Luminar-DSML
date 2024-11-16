def no_rep(s):

    for i in s:
        if s.count(i) ==1:
            index = s.index(i)
            break
    return index

s = input("Enter a string\t")

print(no_rep(s))