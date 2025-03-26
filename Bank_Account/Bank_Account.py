
class BankAccount:

    #create account
    def __init__(self, name:str, balance, national_code):
        self.name=name
        self.balance=balance
        self.national_code=national_code
        print(f'Account {self.name} created.\nBalance= {self.balance}') 
    
    #get balance
    def getBalance(self):
        print(f'Account {self.name} balance= {self.balance}') 
    
    #deposit
    def deposit (self, amount):
        self.balance+=amount
        print('successfully')
        BankAccount.getBalance(self)

    #withdraw
    def withdraw(self, amount):
        if self.balance < amount:
            print(f'Sorry account {self.name} only has balance of {self.balance}')
        elif self.balance > amount:
            self.balance-=amount
            print('successfully')
            BankAccount.getBalance(self)

    #transfer
    def transfer(self , amount, account_name):
        print('Transfer started\n*************')
        if self.balance < amount:
            print(f'Sorry account {self.name} only has balance of {self.balance}')
        else:
            self.balance-=amount
            print('successfully')
            BankAccount.getBalance(self) 
            BankAccount.deposit(account_name,amount) 
        print('*************\nTransfer comleted')

