from datetime import datetime
from typing import List, Dict, Optional

class Transaction:
    def __init__(self, tx_type: str, amount: float, balance_after: float):
        self.tx_type = tx_type
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = datetime.now()

class Account:
    def __init__(self, account_id: str, owner: str, initial_deposit: float = 0.0):
        self.account_id = account_id
        self.owner = owner
        self.balance = initial_deposit
        self.history: List[Transaction] = []
        if initial_deposit > 0:
            self.history.append(Transaction("INITIAL_DEPOSIT", initial_deposit, self.balance))

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False
        self.balance += amount
        self.history.append(Transaction("DEPOSIT", amount, self.balance))
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        self.history.append(Transaction("WITHDRAW", amount, self.balance))
        return True

class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts: Dict[str, Account] = {}

    def create_account(self, account_id: str, owner: str, initial_deposit: float = 0.0) -> Account:
        if account_id in self.accounts:
            raise ValueError(f"Account {account_id} already exists.")
        acc = Account(account_id, owner, initial_deposit)
        self.accounts[account_id] = acc
        return acc

    def transfer(self, from_id: str, to_id: str, amount: float) -> bool:
        if from_id not in self.accounts or to_id not in self.accounts or amount <= 0:
            return False
        acc_from = self.accounts[from_id]
        acc_to = self.accounts[to_id]
        if acc_from.withdraw(amount):
            acc_to.deposit(amount)
            return True
        return False
