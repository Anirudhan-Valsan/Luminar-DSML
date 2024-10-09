

class Students:

    name : str
    age  : int
    course : str

    def register(self,name,age,course):

        self.name = name
        self.age = age
        self.course = course

    def display(self):

        print(f"Name    :  {self.name}")
        print(f"Age     :  {self.age}")
        print(f"Course  :  {self.course}")


print("        Enter The students details       ")
print("-------------------------------------------")


ch = ''
i = 1
student_list = []

while(ch!='n'):

    name = input("Enter the name             \t")
    age  = input("Enter The age              \t")
    course = input("Enter the course name    \t")

    i += 1
    obj_name = "student" + str(i)

    obj_name = Students()

    obj_name.register(name,age,course)

    student_list.append(obj_name)

    ch = input("\nDo you want enter another student? if yes type 'y' or to stop enter 'n'   \t")



count=1

print("\n>>>>>>>   STUDENT DETAILS   <<<<<<")

for i in student_list:

    print(f"\nStudent No. {count}  ")
    print("------------------------")

    i.display()

    count+=1
















    









