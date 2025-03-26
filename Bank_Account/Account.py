from Bank_Account.Bank_Account import *

fatemeh=BankAccount(name='fatemeh',balance= 50000, national_code='0250175509')
fatemeh.getBalance()
fatemeh.deposit(8000)
fatemeh.withdraw(3000)
zahra=BankAccount('zahra', 10000, '0250185637')
zahra.getBalance()
zahra.deposit(5000)
zahra.withdraw(2000)
zahra.transfer(1000, fatemeh)



