def thousand_separator(numbers):
    newlst = []
    for i in numbers:
        newlst.append(f"{i:,}")
    return newlst

numbers = [1000000, 2356989, 2354672, 9878098]

print(thousand_separator(numbers))