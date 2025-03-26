from Bank_Account.Bank_Account import *
from Bank_Account.Account import *
import mysql.connector as msql

con1 = msql.connect(
    host='localhost',
    user='root',
    passwd='mahshid'
)
cursor1 = con1.cursor()

cursor1.execute("CREATE DATABASE IF NOT EXISTS users")

con1.close()  
con1 = msql.connect(
    host='localhost',
    user='root',
    passwd='mahshid',
    database='users'
)
cursor1 = con1.cursor()


query1 = '''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    balance INT,  
    national_code VARCHAR(10)
)
'''
cursor1.execute(query1)


try:
    values = (fatemeh.name, fatemeh.balance, fatemeh.national_code)
except NameError:
    print("خطا: متغیر 'zahra' تعریف نشده است.")
    con1.close()
    exit()


query2 = "INSERT INTO users(name, balance, national_code) VALUES (%s, %s, %s)"
cursor1.execute(query2, values)
con1.commit()

cursor1.execute("SELECT * FROM users")
for row in cursor1.fetchall():
    print(row)


con1.close()
