def length_list(words):

    length_list=[]
    for i in words:
        if "e" in i and len(i)>3:
            length_list.append(len(i))

    sq=[]
    ev_sq=[]
    for i in length_list:
            sq.append(i**2)
            if i%2==0:
                ev_sq.append(i**2)

    #print(length_list)
    #print(sq)
    print(ev_sq)
                
words=["apple","banana","cherry","date","elderberry","fig","grape"]
length_list(words)
