# Create a BankAccaunt with  owner name and balance.

class BankAccaunt:
   
    def __init__(self, owner_name: str ,balance: int=0):
        self.owner_name=owner_name
        self.balance=balance
# This method adds money to the account and prints a confirmation message.
    def deposit(self,amount):
        self.balance=self.balance+amount

        print(f"{self.owner_name} deposited {amount}. New balance: {self.balance}")
# This method deducts money from the account if sufficient balance is available; otherwise, prints an error message.
    def withdraw(self,amount):
        if amount > self.balance:

            print(f"Mr or Ms {self.owner_name} insufficient funds! Available balance: {self.balance}")
            
        else:
            self.balance=self.balance-amount  

            print(f"{self.owner_name} withdrawn {amount}. New balance: {self.balance}")
# This method returns and prints the current balance.
    def get_balance(self):

        print(f"Mr or Ms {self.owner_name} your current balance: {self.balance}")

        
        
        
account1 = BankAccaunt("Elon Musk",1000)
account2 = BankAccaunt("Jeff Bezos",2000)

account1.get_balance()
account2.get_balance()

account1.deposit(500)

account2.withdraw(200)

account1.get_balance()

account2.withdraw(2000)


