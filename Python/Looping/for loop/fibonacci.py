n=int(input("Enter the limit\t"))

prev=0
current=1
print(prev,current,end=" ")
for i in range(n):

    next=prev+current
    print(next,end=' ')
    prev=current
    current=next
    
    


