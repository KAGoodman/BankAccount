class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
        
    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all(acnt):
        for account in acnt.accounts:
            account.display_account_info()

savings = BankAccount(.06, 500)
checking = BankAccount(.02, 2150)

savings.deposit(10).deposit(20).deposit(50).withdraw(500).yield_interest().display_account_info()
checking.deposit(300).deposit(100).withdraw(20).withdraw(50).withdraw(15).withdraw(50).yield_interest().display_account_info()

BankAccount.print_all()


