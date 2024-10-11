def evn_oddsum(lower,upper):
    evsum=0
    oddsum=0
    for i in range(lower,upper+1):
        if(i%2==0):
            evsum+=i
        else:
            oddsum+=i
    print(f"Sum of even numbers between {lower} and {upper} are {evsum}")
    print(f"Sum of odd numbers between {lower} and {upper} are {oddsum}")




a=int(input("Enter the first limit\t"))
b=int(input("Enter the second limit\t"))
evn_oddsum(a,b)