from account import Account, CreditAccount, SavingsAccount



class Bank:
    """bank account"""
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, category, owner, interest_rate=0):
        """Create a new account"""

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

    def find_accounts_by_ssn(self, ssn: list) -> list:
        """searches for accounts and returns a list of 
        if they match the ssn

        Args:
            ssn (list): ssn as a string

        Returns:
            list: returns a list of accounts
        """
        account_list = []
        for acc in self.accounts:
            if acc.owner.ssn == ssn:
                account_list.append(acc)
        return account_list

    def find_accounts_by_name(self, name:str) -> list:
        """Searches for accounts by name

        Args:
            name (str): name 

        Returns:
            list: list of accounts that have the name
        """
        account_list = []
        for acc in self.accounts:
            if acc.owner.name == name:
                account_list.append(acc)
        return account_list

    @property
    def balance(self) -> int:
        """adds all accounts.amounts
        for a bank balance total

        Returns:
            int: bank balance
        """
        total = 0
        for account in self.accounts:
            total += account.amount
        return total
