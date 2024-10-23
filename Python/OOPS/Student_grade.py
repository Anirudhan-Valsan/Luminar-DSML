#write a class student with attributes name and marks (dic of subjname and marks)

#add_marks(subject,marks)
#get_marks(subject)
#average_marks()

class Student:

    def __init__(self,name):

        self.name = name
        self.result = {}

    def add_marks(self,subject,mark):
        self.subject = subject
        self.marks = mark
        self.result[subject] = mark

    def get_marks(self,subject):

        print(f"The mark for {subject} is {self.result[subject]}")

    def average_marks(self):
        
        average = sum(self.result.values())/len(self.result)
    

        print(f"The average marks is {average}")


student1 = Student("Anirudhan")
student1.add_marks("Maths",50)
student1.add_marks("Computer",80)
student1.add_marks("English",80)

student1.get_marks("Computer")

student1.average_marks()
