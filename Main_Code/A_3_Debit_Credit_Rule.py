class Asset_Expense_Rule:
    def __init__(self):
        self.opening_balance = 0
        
        
    def credit_transaction(self,credit_amount):
        self.credit_balance = abs(self.opening_balance - credit_amount )
        return self.credit_balance 
       

    def debit_transaction(self,debit_amount):
        self.debit_balance = debit_amount + self.opening_balance 
        return self.debit_balance 
    
    def get_balance(self):
        return self.opening_balance, self.debit_balance, self.credit_balance, 


class Liability_Capital_Revenue_Rule:
    def __init__(self):
        self.opening_balance = 0

        
    def credit_transaction(self,credit_amount):
        self.credit_balance = credit_amount + self.opening_balance
        return self.credit_balance 
       

    def debit_transaction(self,debit_amount):
        self.debit_balance =abs(debit_amount - self.opening_balance ) 
        return self.debit_balance 
    
    def get_balance(self):
        return self.opening_balance, self.debit_balance, self.credit_balance, 

