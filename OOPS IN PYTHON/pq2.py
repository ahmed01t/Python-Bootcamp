class bank:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
    #debit method
    def debit(self,amount):
        self.balance-=amount
        print(f"{amount} is debited from your account")
        print(f"total balance is ",self.final_balance())
    # credit method
    def credit(self,amount):
        self.balance+=amount
        print(f"{amount} is credited ")
        print(f"total balance is ",self.final_balance())

    def final_balance(self):
        return self.balance
customer=bank(25000,1234)
customer.debit(1000)
customer.credit(5000)