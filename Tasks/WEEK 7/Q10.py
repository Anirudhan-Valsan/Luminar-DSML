# Given a string, find the longest substring without repeating characters

def find_string(s):

    longest = ""

    current = ""

    for i in s:

        if i not in current:

            current += i

        else:
            if len(current) > len(longest):

                longest = current

            current = i

    if len(current) > len(longest):

        longest = current

    return longest

string = input("Enter a string \t")

print(f"The longest substring without repeating characters is  {find_string(string)}")

