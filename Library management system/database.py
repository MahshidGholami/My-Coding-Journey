import mysql.connector as msql

#اتصال به پایگاه داده
connection=msql.connect(
    host='localhost',
    user='root',
    passwd='mahshid'
)
cursor1=connection.cursor()

#ایجاد پایگاه داده
cursor1.execute('CREATE DATABASE IF NOT EXISTS Library_management')

#انتخاب پایگاه داده
cursor1.execute('USE Library_management')

#ایجاد جدول
cursor1.execute('CREATE TABLE IF NOT EXISTS Library(id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(200), auther VARCHAR(200), years INT)')

#نمایش موجود جدول ها
cursor1.execute('SHOW TABLES')
tables=cursor1.fetchall()
print(tables)

#بستن اتصال 
cursor1.close()
connection.close()
