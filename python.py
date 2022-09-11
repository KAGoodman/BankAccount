class user:

    def __init__(self, name="0", starting_balance=0, interest_rate=0.03):
        self.name = name
        self.account = BankAccount(starting_balance, interest_rate)

    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

class BankAccount:
    bankname = "the dojo trust"
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
    def all_balances(acnt):
        sum = 0
        for account in acnt.all_accounts:
            sum += account.balance
        return sum

    @classmethod
    def print_all(acnt):
        for account in acnt.accounts:
            account.display_account_info()

savings = BankAccount(.06, 500)
checking = BankAccount(.02, 2150)

savings.deposit(10).deposit(20).deposit(50).withdraw(500).yield_interest().display_account_info()
checking.deposit(300).deposit(100).withdraw(20).withdraw(50).withdraw(15).withdraw(50).yield_interest().display_account_info()

BankAccount.print_all()



ryan = user("ryan glookle")
ryan.display_user_balance().make_deposit(55).display_user_balance()
ryan.make_withdraw(22).display_user_balance()
ryan.yield_interest().display_user_balance()