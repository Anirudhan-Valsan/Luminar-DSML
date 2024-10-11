print("1)Create a new file\n2)Display the file\n3)Add a new item to the file\nMake a selection 1,2 or 3\n")

choice=int(input())

if(choice == 1):

    subject = input("Enter a subject name\t")
    file = open("subject.txt",mode="w")
    file.write(subject)
    file.close()

elif(choice == 2):

    file = open("subject.txt",mode="r")
    print(file.read())

elif(choice == 3):

    new_sub=input("ENter a new subject\t")
    file = open("subject.txt",mode="a")
    file.write(new_sub)
    file.close()

    display = open("subject.txt",mode="r")
    print(display.read())
    display.close()

else:

    print("Invalid choice")