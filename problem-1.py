# create account class with 2 attribute - balance and account no, create methods for debit and credit and printing the balance  

class Account:
    def __init__(self,bal,acct):
        self.balance = bal
        self.acct_no = acct
   #debit method-------
    def debit(self,amount):
        self.balance -= amount
        print("Rs..",amount,"was debited")
        print("total balance =",self.get_balance())
   #credit method----------
    def credit(self,amount):
        self.balance += amount
        print("Rs..",amount,"amount has been creddited")
        print("total balance =",self.get_balance())
   # to get balance 
    def get_balance(self):
        return self.balance
    
user1 = Account(10000,12345)
user1.credit(2000)
user1.debit(2000)