class Bank:
    def __init__(self):
        self.balance=0
        self.accountno=int(input("Enter account number:"))
        self.name=input("Enter name:")
        self.accounttype=input("Enter account type:")

    def display(self):
        print("Name:",self.name)
        print("AccountNumber",self.accountno)
        print("Account type:",self.accounttype)

    def deposit(self):
        amount=int(input("Enter the amount to deposite:"))
        self.balance+=amount
        print("Your balance is",self.balance)

    def withdraw(self):
        amount=int(input("Enter the amount to withdraw:"))
        if(amount>self.balance):
            print("Insufficient balance!")
        else:
            self.balance-=amount
            print("Your remaining balance is:",self.balance)

account=Bank()
account.display()
account.deposit()
account.withdraw()          