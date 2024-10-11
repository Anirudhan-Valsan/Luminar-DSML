def sum(*args):                    
    sum=0
    for i in args:
        sum+=i
    return(sum)


print(sum(1,2,3))    


 #**kwargs for keyword arguments

def details(**kwargs):
   print(kwargs)


details(name='Anirudhan',Age='24')