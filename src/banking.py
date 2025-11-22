import time

class Transaction:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount
        self.timestamp = time.time()

    def __repr__(self):
        return f"Transaction({self.type}, {self.amount}, {self.timestamp})"

class Account:
    MIN_BALANCE = 0

    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            self.transactions.append(Transaction("DEPOSIT", amount))
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance = self.balance - amount
            self.transactions.append(Transaction("WITHDRAWAL", amount))
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

class SavingsAccount(Account):
    def __init__(self, initial_balance=0, interest_rate=0.02):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        # deposit logs the transaction, but we might want a specific type
        # For simplicity, we'll let deposit handle it or update the last transaction type
        if self.transactions:
            self.transactions[-1].type = "INTEREST"

class CheckingAccount(Account):
    def __init__(self, initial_balance=0, overdraft_limit=100):
        super().__init__(initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and self.balance + self.overdraft_limit >= amount:
            self.balance = self.balance - amount
            self.transactions.append(Transaction("WITHDRAWAL", amount))
            return True
        return False

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_id, account):
        self.accounts[account_id] = account

    def get_account(self, account_id):
        return self.accounts.get(account_id)

    def transfer(self, from_id, to_id, amount):
        if from_id not in self.accounts or to_id not in self.accounts:
            return False
            
        from_acc = self.accounts[from_id]
        to_acc = self.accounts[to_id]

        # Integration logic: withdraw from one, deposit to another
        if from_acc.withdraw(amount):
            if to_acc.deposit(amount):
                # Update transaction types for clarity
                from_acc.transactions[-1].type = f"TRANSFER_OUT_TO_{to_id}"
                to_acc.transactions[-1].type = f"TRANSFER_IN_FROM_{from_id}"
                return True
            else:
                # Rollback if deposit fails
                from_acc.deposit(amount) 
                # Remove the rollback deposit and failed withdrawal from history to keep it clean?
                # Or keep them as failed attempts. Let's keep it simple.
                return False
        return False

    def get_total_deposits(self):
        total = 0
        for acc in self.accounts.values():
            total += acc.get_balance()
        return total
