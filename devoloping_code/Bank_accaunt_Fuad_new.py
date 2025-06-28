class BankAccount:
    """Represents a bank account with an owner and a balance.

    Attributes:
        owner_name (str): The name of the account owner.
        balance (int): The current balance in the account.
    """

    def __init__(self, owner_name: str, balance: int = 0):
        """Initializes a bank account with an owner and a starting balance.

        Args:
            owner_name (str): The name of the account owner.
            balance (int, optional): The initial balance (default is 0).
        """
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: int):
        """Adds money to the account and updates the balance.

        Args:
            amount (int): The amount to deposit.
        """
        self.balance += amount
        print(f"{self.owner_name} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount: int):
        """Withdraws money from the account if there are enough funds.

        Args:
            amount (int): The amount to withdraw.

        If the balance is not enough, an error message is printed.
        """
        if amount > self.balance:
            print(f"Mr or Ms {self.owner_name}, insufficient funds! Available balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"{self.owner_name} withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        """Displays the current balance of the account."""
        print(f"Mr or Ms {self.owner_name}, your current balance: {self.balance}")


# Create two bank accounts
account1 = BankAccount("Elon Musk", 1000)
account2 = BankAccount("Jeff Bezos", 2000)

# Display initial balances
account1.get_balance()
account2.get_balance()

# Perform transactions
account1.deposit(500)    # Elon deposits 500
account2.withdraw(200)   # Jeff withdraws 200
account1.get_balance()   # Check Elon's balance
account2.withdraw(2000)  # Jeff tries to withdraw more than available
