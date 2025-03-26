import mysql.connector as msql

# اتصال به دیتابیس
def connect_to_db():
    Continue=msql.connect(
        host='localhost',
        user='root',
        passwd='mahshid',
        database='customer_management'
    )
    return Continue
#افزودن مشتری به دیتابیس
def add_customer(name,phone,email):
    Continue=connect_to_db()
    Cursor=Continue.cursor()
    query='INSERT INTO customers(name,phone,email)VALUES(%s,%s,%s)' 
    Cursor.execute(query,(name,phone,email))
    Continue.commit()
    print('با موفقیت انجام شد')
    Cursor.close()
    Continue.close()


#نمایش همه ی مشتری ها
def displaye_customer():
    Continue=connect_to_db()
    Cursor=Continue.cursor()
    query='SELECT * FROM customers'
    Cursor.execute(query)
    customers=Cursor.fetchall()
    for customer in customers:
        print(customer)
    Cursor.close()
    Continue.close()

#جستجوی کابر با نام
def search_customer_by_name(name):
    Continue=connect_to_db()
    Cursor=Continue.cursor()
    query='SELECT * FROM customers WHERE name LIKE %s'
    Cursor.execute(query,(f'%{name}%',))
    customers=Cursor.fetchall()
    if customers:
        for customer in customers:
            print(f'ID: {customers[0]}, NAME: {customers[1]}, PHONE: {customers[2]}, EMAIL: {customers[3]}')
    else:
        print('پیدا نشد')
    Cursor.close()
    Continue.close()

#اپدیت کردن اطلاعات
def update_customer(id,name=None, phone=None , email=None):
    Contionue=connect_to_db()
    Cursor=Contionue.cursor()
    query='UPDATE customers SET name = %s, phone = %s, email = %s, address = %s WHERE id = %s'
    Cursor.execute(query,(f'%{name}%',))
    Cursor.execute(query, (name, phone, email, id))
    Contionue.commit()
    print(f"مشتری با ID {id} ویرایش شد.")
    Cursor.close()
    Contionue.close()

#حذف کاربر
def delete_customer(id):
   Contionue=connect_to_db()
   Cursor=Contionue.cursor()
   query='DELETE FROM customers WHERE id=%s' 
   Cursor.execute(query,(id))
   Contionue.commit()
   print("با موفقیت انجام شد")
   Cursor.close()
   Contionue.close()