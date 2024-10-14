'''
Q8)
A school has following rules for grading system:
a. Below 25-F
b. 25 to 45-E
c. 45 to 50-D
d. 50 to 60-C
e. 60 to 80- B
f. Above 80-A
Ask user to enter marks and print the corresponding grade

'''

def grades(mark):

    grades = {
              range(0,25)  : 'F',
              range(25,45) : 'E',
              range(45,50) : 'D',
              range(50,60) : 'C',
              range(60,80) : 'B',
              range(80,101): 'A'
            }
    for i in grades:
        if mark in i:
            return grades[i]
    return 'Invalid marks'

mark = int(input("enter the percentage\t"))
print(f"The grade is {grades(mark)}")