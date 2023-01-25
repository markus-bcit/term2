from customer import Customer
from account import *


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

        
    def create_account(self, category, owner, interest_rate=0):
        new_account = None
        if category not in ("account", "credit", "savings"):
            return AttributeError
        if category == 'account':
            new_account = Account(owner)
        if category == 'credit':
            new_account = CreditAccount(owner, interest_rate)
        if category == 'savings':
            new_account = SavingsAccount(owner)
        self.accounts.append(new_account)
        return new_account
 
    def find_accounts_by_ssn(self, ssn):
        a = []
        for acc in self.accounts:
            if acc.owner.ssn == ssn:
                a.append(acc)
        return a
        
    def find_accounts_by_name(self, name):
        a = []
        for acc in self.accounts:
            if acc.owner.name == name:
                a.append(acc)
        return a
    
    @property
    def balance(self):
        total = 0 
        for account in self.accounts:
            total += account.amount
        return total