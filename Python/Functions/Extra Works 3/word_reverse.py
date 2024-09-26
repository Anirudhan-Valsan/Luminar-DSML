# 1 reverse order of words in a string


def reverse(sentence):
    reverse=''
    p=0
    for i in sentence:
        p+=1
        if i==" ":
            c=p
            break
    reverse=sentence[c:]+" "+sentence[:c]
    

    print(reverse)


sentence=input("enter a sentence \t")

reverse(sentence)
