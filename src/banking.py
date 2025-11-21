class Account:
    MIN_BALANCE = 0

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance = self.balance - amount
            return True
        return False

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_id, account):
        self.accounts[account_id] = account

    def transfer(self, from_id, to_id, amount):
        if from_id not in self.accounts or to_id not in self.accounts:
            return False
            
        from_acc = self.accounts[from_id]
        to_acc = self.accounts[to_id]

        # Integration logic: withdraw from one, deposit to another
        if from_acc.withdraw(amount):
            if to_acc.deposit(amount):
                return True
            else:
                # Rollback if deposit fails
                from_acc.deposit(amount) 
                return False
        return False
