

def print_list(list):
    for i in list:
        if i<0:
            break
        print(i)


list = [1,2,3,-2,4,5]
print_list(list)