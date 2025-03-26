import mysql.connector as msql


#اتصال به پایگاه داده
def connect_to_db():
    connection=msql.connect(
        host='localhost',
        user='root',
        passwd='mahshid',
        database='Library_management'
    )
    return connection

#اضافه کردن کتاب 
def add_book(title, author, year):
    connection=connect_to_db()
    cursor=connection.cursor()
    query='INSERT INTO Library(title, author, year)VALUES(%s,%s,%s)'
    values=(title, author, year)
    cursor.execute(query, values)
    connection.commit()
    print(f'با موفقیت اضافه شد')
    cursor.close()
    connection.close()


#نمایش کتاب ها
def displaye_book():
    connection=connect_to_db()
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM Library')
    books=cursor.fetchall()
    if books:
        print("\n لیست کتاب‌ها:")
        for book in books:
            print(book)
    else:
        print(" هیچ کتابی در کتابخانه وجود ندارد.")

    cursor.close()
    connection.close()

#جستجوی کتاب
def search_book(keyword):
    connection=connect_to_db()
    cursor=connection.cursor()
    query='SELECT * FROM Library WHERE title LINK %s OR author LINK %s '
    cursor.execute(query, (f'%{keyword}%',f'%{keyword}%'))
    books=cursor.fetchall()
    if books:
        print("\n نتیجه جستجو:")
        for book in books:
            print(f'{book[1]} - {book[2]} ({book[3]})')
    else:
        print(" کتابی یافت نشد.")
    cursor.close()
    connection.close()


#حذف کتاب
def del_book(book_id):
    connection=connect_to_db()
    cursor=connection.cursor()
    query='DELETE FROM Library WHERE id=%s'
    cursor.execute(query,(book_id,))
    
    if cursor.rowcount > 0:
        print(f' کتاب با شناسه {book_id} حذف شد.')
    else:
        print("کتابی با این شناسه یافت نشد.")

    
    connection.commit()
    cursor.close()
    connection.close()