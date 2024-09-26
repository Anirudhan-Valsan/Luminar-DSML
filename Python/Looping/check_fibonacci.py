num=int(input("Enter the number \t"))

prev=0
current=1
print(prev,current,end=" ")
for i in range(num**2):

    next=prev+current
    print(next,end=" ")
    if num==next:
        print(f"\n{num} is present in fibonacci series\n")
        break
    prev=current
    current=next
else:
    print(f"{num} Not present in the series")
    