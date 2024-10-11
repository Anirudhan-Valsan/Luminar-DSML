#O/p {'name': 'hari', 'age': '24', 'job': 'Team Lead', 'place': 'Kakkanad'}

d1={"name":"hari","age":"24","job":"trainer","place":"kochi"}

d2={"job":"Team Lead","place":"Kakkanad","Salary":"10000"}



for i in d1.keys():
    if i in d2.keys():
        d1[i]=d2[i]

print(d1)