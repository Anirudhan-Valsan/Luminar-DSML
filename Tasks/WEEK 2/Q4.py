# Q4) Accept the age, sex ('M', 'F'), number of days and display the wages accordingly


# Age : 18 <= age < 30   Wage: M = 700/Day  !  F = 750/Day
# Age : 30 <= age <= 40  Wage : M = 800/Day !  F = 850/Day

def wage(age,sex,days):


    if(18 <= age < 30):

        if sex == 'M':

            wage = 700*days
        
        elif sex == 'F':

            wage = 750*days
    
    if 30 <= age <= 40:

        if sex == 'M':

            wage = 800*days

        elif sex == 'F':

            wage = 850*days

    return wage
        

age = int(input("Enter your Age : \t"))
sex = input("Enter your sex (F/M) :  \t")
days = int(input("Enter the number of days worked : \t"))

print(f"Your wage is : {wage(age,sex,days)}")



