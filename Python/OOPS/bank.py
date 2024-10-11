#name,place,account type,balance,bank name

#methods : show details, deposit, withdrawal,balance


class Bank:

    name         : str
    place        : str
    account_type : str
    balance      : float
    bank_name    = 'SBI'

    def __init__(self,name,place,account_type,balance,bank_name):
        
        self.name = name
        self.place = place
        self.account_type = account_type
        self.balance = balance
        self.bank_name = bank_name
        


    def show_details(self):

        print("\n--------------------------------Account Details--------------------------------")
        print(f"Name         :  {self.name}")
        print(f"Place        :   {self.place}")
        print(f"Account Type :  {self.account_type}")
        print(f"Balance      : {self.balance}")
        print(f"Bank Name    : {self.bank_name}")
        print("\n<----------------------------------------------------------->\n")

    def deposit(self):

        dep = float(input ("Enter The amount to deposit\t"))

        self.balance += dep

    def withdraw(self):

        wdraw = float(input("Enter the amount to withdraw\t"))
        self.balance -= wdraw


    def balance_acc(self):

        print(f"Balance : {self.balance}")






obj1 = Bank('Anirudhan','Kochi','Savings',150000,bank_name='SBI')

obj1.show_details()

obj1.deposit()

obj1.balance_acc()

obj1.withdraw()

obj1.balance_acc()

