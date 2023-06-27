# class BankAccount

class BankAccount:
    def __init__(self, account: int):
        self.account = account

    def __str__(self):
        return f'\nyour current account: {self.account}'

    def refill(self, refill_amount: int):
        self.account += refill_amount
        return self.__str__()

    def withdraw(self, withdraw_amount: int):
        if withdraw_amount <= self.account:
            self.account -= withdraw_amount
        else:
            return '\nunsupported amount'
        return self.__str__()

