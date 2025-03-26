import mysql.connector as msql

# اتصال به پایگاه داده
connection = msql.connect(
    host='localhost',
    user='root',
    passwd='mahshid'
)

cursor1 = connection.cursor()

# ایجاد پایگاه داده 
cursor1.execute('CREATE DATABASE IF NOT EXISTS customer_management')

# انتخاب پایگاه داده
cursor1.execute('USE customer_management')

# ایجاد جدول 
cursor1.execute('CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), phone VARCHAR(12), email VARCHAR(250))')

# نمایش جداول موجود در پایگاه داده
cursor1.execute('SHOW TABLES')
tables = cursor1.fetchall()

# نمایش نام جداول
print(tables)

# بستن اتصال
cursor1.close()
connection.close()
