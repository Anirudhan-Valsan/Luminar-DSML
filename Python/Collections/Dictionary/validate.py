credential={"anirudhan":123}

user=input("enter the username\t")
password=int(input("Enter the pin\t"))

if user in credential.keys() and credential[user]==password:
    print("Welcome Anirudhan")
else:
    print("\ninvalid credentials")