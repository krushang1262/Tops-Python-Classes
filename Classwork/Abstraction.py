from abc import ABC, abstractmethod

class Account:
    balance = 0
    
    @abstractmethod
    def deposit(self,amt):
        pass
    
    @abstractmethod
    def withdraw(self,amt):
        pass
    
    def checkBalance(self):
        print(f"current balance is {self.balance}")
        
class SavingAccount(Account):
    
    def deposit(self, amt):
        self.balance += amt
        
    def withdraw(self, amt):
       if amt > self.balance:
           print("insuffcient balance")
       else:
           self.balance -= amt
           
s = SavingAccount()
s.checkBalance()
s.deposit(5000)
s.checkBalance()
s.withdraw(2000)
s.checkBalance()