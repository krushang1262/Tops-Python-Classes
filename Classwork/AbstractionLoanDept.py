from abc import ABC, abstractmethod
class Loan:
    balance = 0
    
    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass
    
    def checkLoanRecoverAmt(self):
        print(f"Total {self.balance} amount is pending/ to pay")
    
class AccountDept(Loan):
    
    def deposit(self, amt):
        if amt>self.balance:
            print("u are amount is greater than loan amount")
        else:
            self.balance -= amt
            
    def withdraw(self, amt):
        self.balance += amt
        
ad = AccountDept()
ad.withdraw(100000)
ad.deposit(25000)
ad.withdraw(10000)
ad.deposit(85000)
ad.checkLoanRecoverAmt()