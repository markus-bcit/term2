
from customer import Customer

class Account:
    """management for account,
    must be a customer instance
    """
    def __init__(self, owner):
        if not isinstance(owner, Customer):
            raise AttributeError
        else:
            self.owner = owner
            self.amount = 0
            
    def deposit(self, amount):
        """adds the amount deposited to the customers account

        Args:
            amount (int): amount to deposit

        Raises:
            AttributeError: if amount is < 0.
        """
        if amount < 0:
            raise AttributeError("Invalid amount")
        else:
            self.amount += amount
    
    def withdraw(self, amount):
        """subtracts the amount withdrawn from the customers account

        Args:
            amount (int): amount to withdraw

        Raises:
            AttributeError: if amount is < 0.
        """
        if amount < 0:
            raise AttributeError("Invalid amount")
        
        self.amount -= amount
        
    def transfer(self, account : object, amount:int):
        """subtracts the amount transferred from the self.account
        and adds the amount to account

        Args:
            account (class): Account
            amount (int): _description_

        Raises:
            TypeError: if account is not instance of Account
        """
        if not isinstance(account, Account):
            raise TypeError
        
        account.amount += amount
        self.amount -= amount
        
class CreditAccount(Account):
    """adds interest to account if negative balance

    Args:
        Account (object): account instance
    """
    def __init__(self, customer, interest):
        super().__init__(customer)
        self.interest = interest

    def compute_interest(self):
        """if account is below 0, add interest to account and $10 fee
        """
        if self.amount < 0:
            self.amount = self.amount * (100 + self.interest) / 100
            self.amount -= 10

class SavingsAccount(Account):
    """parent class account 

    Args:
        Account (ogject): parent of savings account
    """
    def __init__(self, customer):
        super().__init__(customer)
        
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise UserWarning
        self._amount = value
