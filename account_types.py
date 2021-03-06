from random import randint
import bank
import account

class SavingsAccount(account.Account, bank.Bank):
    def __init__(self, code, bank_code, salary, doc, tel, cep):
        super().__init__(code, bank_code, doc, tel, cep)
        self.salary = salary

    def interest_rate(self):
        self._balance *= 1.01
        return self._balance
    
    def mounth_turn(self):
        self.interest_rate()
        self._balance -= self.administration_fee(self._bank_code)
        self.salary += self.salary

class CheckingAccount(account.Account, bank.Bank):
    def __init__(self, code, bank_code, salary, doc, tel, cep):
        super().__init__(code, bank_code, doc, tel, cep)
        self.salary = salary

    def mounth_turn(self):
        self._balance += self.salary
        self._balance -= self.administration_fee(self._bank_code)
