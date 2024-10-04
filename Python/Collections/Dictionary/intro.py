#dictionary

items={}

list1=[1,2,3,4]
list2=["a","b","c","d"]

for i in range(4):
    items[list1[i]]=list2[i]
print(items)

print(items.items())

print(items.get(3))

print(items.keys())

print(items.values())

items.update({5:"e",6:"f"})
print(items)



