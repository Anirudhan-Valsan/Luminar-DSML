
class Students():

    def register(self,name,rollno,course):
        self.name = name
        self.rollno = rollno
        self.course = course

    def display(self):
        print(f"Name      :   {self.name}")
        print(f"Roll No   :   {self.rollno}")
        print(f"Course:   :   {self.course}")
        

print("Enter the students details\n---------------------------------------\n")

ch=''

i = 1

student_list = []

while(ch != 'n'):

    name   = input("Enter the name        : ")
    rollno = input("Enter the rollno      : ")
    course = input("Enter the course      : ")

    obj_name = 'student'+'i'

    obj_name = Students()
    obj_name.register(name,rollno,course)

    student_list.append(obj_name)
    
    i = i+1
   
    ch = input("\nDo you want to continue (y/n) : ")

    print("\n---------------------------------------\n")



print("\n---------------------------------------\n")
print("List of students\n---------------------------------------\n")
count=1

for i in student_list:
    print("\n---------------------------------------\n")
    print(f"Student no. {count}")
    print("---------------------------------------")
    i.display()
    count+=1
    print("---------------------------------------\n")