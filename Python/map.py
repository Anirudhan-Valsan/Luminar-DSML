#cube of all numbers using map
#filter odd numbers using filter
#product using reduce

from functools import reduce

def cube(x):

    return x**3

def is_odd(x):

    if x%2!= 0:

        return True
    else:

        False

def multiply(x,y):

    return x*y

numbers = [1,5,3,4,1,6,7,2,8,5,10]

num_cube = list(map(cube,numbers))              #=list(map(lambda,a:a**3,numbers))

odd_num = list(filter(is_odd,num_cube))         #=list(filter(lambda,a:a%2!=0,num_cube))

product_num = reduce(multiply,odd_num)          #=reduce((lambda,a,b:a*b),odd_num)

print(num_cube)

print(odd_num)

print(product_num)


