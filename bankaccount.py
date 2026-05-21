from datetime import datetime

class BankAccount:
    def __init__(self, username, pin):
        self.__username = username
        self.__pin = pin
        self.__balance = 0
        self.__transactions = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, value):
        if value <= 0:
            print("Ingrese un monto válido.")
            raise ValueError("Ingrese un monto válido.")
        self.__balance += value
        transaction = Transaction("deposit", value, self.__balance)
        self.__transactions.append(transaction)

    def withdraw(self, value):
        if value <= 0:
            print("Ingrese un monto válido.")
            raise ValueError("Ingrese un monto válido.")
        if value > self.__balance:
            print("Fondos insuficientes.")
            raise ValueError("Fondos insuficientes.")
        self.__balance -= value
        transaction = Transaction("withdraw", value, self.__balance)
        self.__transactions.append(transaction)

    def get_transactions(self):
        return self.__transactions.copy()
    
class Transaction:
    def __init__(self, type, amount, balance_after):
        self.type = type
        self.amount = amount
        self.date = datetime.now()
        self.balance_after = balance_after

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.type} | {self.amount} | Saldo: {self.balance_after}"
