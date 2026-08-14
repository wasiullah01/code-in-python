class BankAccount:
    def __init__(self,owner_name,BalanceDeposit,account_number):
        self.owner = owner_name
        self.balance = BalanceDeposit
        self.account_number = account_number
        self.statment = []

    def deposit(self,deposited):    
        self.balance += deposited
        print(f"PKR: {deposited} Deposited Successfully")
        self.statment.append(f"Deposited Balance: {deposited} ")

    def Withdraw(self,withdrawal):
        if withdrawal <= self.balance:
            print("Successfull withdraw")
            self.balance = self.balance - withdrawal
            self.statment.append(f"Withdraw: {withdrawal} ")
        else: 
            print(f"Your total amount is PKR: {self.balance}")

    def get_info(self):
        print(f"Account Holder Name: {self.owner}")
        print(f"Account Number {self.account_number}")
        print(f"Total Balance is {self.balance}")
        print(f"Statments: {self.statment}")
    

class child_1(BankAccount):
    def __init__(self, owner_name, BalanceDeposit, account_number):
        self.monthlyFee = 100
        self.limit = 5000

        super().__init__(owner_name, BalanceDeposit, account_number)

    def monthly_fee(self):

        self.balance = self.balance - self.monthlyFee
        self.statment.append(f"Monthly Fee Child1: {self.monthlyFee}")

    def withrawal_limit(self,withdraw):

        if withdraw <= self.limit:
            if self.balance >= withdraw:
               self.balance -= withdraw
               print(f"Amount {withdraw} Withraw successfull")
               self.statment.append(f"Child1 Withdraw {withdraw}")
            else:
                print(f"Your Parent Account balance is {self.balance}")

        else: 
            print(f"you have total amount {self.limit}")

    def child1_info(self):
        print(f"Total limit reamain {self.limit}")
        print(f"Monthly deduction {self.monthlyFee}")




print("===Child 1===")
child1 = child_1("Wasi",20000,145808)

child1.monthly_fee()
child1.withrawal_limit(3000)
child1.child1_info()
child1.get_info()
