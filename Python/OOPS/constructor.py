

class Employee:

    name  : str

    place : str

    role  : str


    def __init__(self,name,place,role):         #constructor
        
        self.name  = name
        self.place = place
        self.role  = role

    def show_name(self):

        return self.name


person1 = Employee('Anirudhan','Ayroor','ML Engineer')

print(person1.show_name())