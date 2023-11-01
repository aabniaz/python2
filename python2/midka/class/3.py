class BankAccount:
    def __init__(self, accnumber, balance=0):
        self.accnumber = accnumber
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into Account {self.accnumber}. Current balance is {self.balance}.")
        else:
            print("Please enter a valid amount to deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from Account {self.accnumber}. Current balance is {self.balance}.")
        else:
            print("Insufficient funds or invalid amount to withdraw.")

    def check_balance(self):
        print(f"Account {self.accnumber} balance: {self.balance}")


account1 = BankAccount("12345", 500)  
account1.check_balance()  
account1.deposit(100)  
account1.check_balance()  
account1.withdraw(50)  
account1.check_balance()  
account1.withdraw(600)  
