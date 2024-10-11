#o/p >>> {name:"hari","age":26,"place":"kochi"}

keys=["name","age","place"]
values=["hari",26,"chennai"]

person={}

for i in range(len(keys)):
    person.update({keys[i]:values[i]})
    

print(person)