class  Account():
    
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if (self.balance > 0 and amount < self.balance):
            self.balance -= amount
        else:
            print("Not sufficient balance")
        
    def __str__(self):
        return f"Account owner is {self.owner} and the balance is: {self.balance}"
        
account = Account('Denise', 1000)

account.deposit(300)
print(account)
account.withdraw(5000)
print("After withdraw")
print(account)