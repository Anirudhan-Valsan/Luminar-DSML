#create a class named employee with methods

#method 1 {name,role,salary,place}
#method 2 {name,place}
#method 3 {name,role,salary}
#method 4 {role,salary}


class employee:

    def method1(self,name,role,salary,place):
        
        self.name   = name
        self.role   = role
        self.salary = salary
        self.place  = place
        print(f"Employee {self.name} works as a {self.role} at {self.place} with a salary of {self.salary}.")


    def method2(self, name, place):

        self.name = name
        self.place = place
        print(f"Employee {self.name} works at {self.place}.")

    def method3(self, name, role, salary):

        self.name = name
        self.role = role
        self.salary = salary
        print(f"Employee {self.name} works as a {self.role} with a salary of {self.salary}.")

    def method4(self, role, salary):

        self.role = role
        self.salary = salary
        print(f"Employee's role is {self.role} with a salary of {self.salary}.")


name = input("Enter the name\t")
role = input("Enter the role\t")
salary = int(input("Enter the salary\t"))
place = input("Enter the place\t")


emp1 = employee()

emp1.method1(name,role,salary,place)

emp1.method2(name,place)

emp1.method3(name,role,salary)

emp1.method4(role,salary)