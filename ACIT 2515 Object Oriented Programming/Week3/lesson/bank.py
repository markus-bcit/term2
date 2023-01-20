class BankAccount:
    def __init__(self):
        self._amount = 0
    
    def deposit(self, value):
        self._account += value

    
    def withdraw(self, value):
        self.deposit(-value)
        
    @property
    def amount(self):
        return self.amount
    
    @amount.setter
    def set_amount(self, value):
        if value > 0:
            raise ValueError
        
        self._amount = value