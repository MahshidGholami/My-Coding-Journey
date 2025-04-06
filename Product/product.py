from random import choice, choices

from django.contrib.admin.templatetags.admin_list import result_list

lst=[]

#خواندن از فایل و ریختن محتوا در یک متغیر
def read_file():
    with open(file='products.txt', mode='r')as file:
        lines=file.readlines()
    for line in lines:
        line=line.strip()
        parts=list(line.split(','))
        product=parts[0].split(':')[1].strip()
        price=int(parts[1].split(':')[1].strip())
        stock=int(parts[2].split(':')[1].strip())
        lst.append({'product':product , 'price':price , 'stock':stock})
    return lst

#افزودن محصول جدید
def add_product():
    print("****** Add product ******\n")
    input_product=input('enter a name product= ')
    input_price = int(input('enter product price: '))
    input_stock = int(input('enter product stock: '))
    with open('products.txt', 'a') as file:
        file.write(f'Product: {input_product}, Price: {input_price}, Stock: {input_stock}')
        print('Product added')
    reader=read_file()
    return reader

#حدف یک محصول
def del_product():
    reader=read_file()
    print("****** delete product ******\n")
    input_product=input('enter a name product= ')
    rewrite_lst = [line for line in reader if line['product'] != input_product]
    with open('products.txt', 'w') as file:
        for line in rewrite_lst:
            file.write(f"Product: {line['product']}, Price: {line['price']}, Stock: {line['stock']}\n")
    print("\nProduct deleted (if it existed).")

#سرچ یک محصول
def search_product():
    reader=read_file()
    print("****** search product ******\n")
    input_product = input('enter a name product= ')
    for line in reader:
        if line['product'] == input_product:
            print(line)

#ویرایش محصول
def update_product():
    reader = read_file()
    print("****** update product ******\n")
    input_product = input('enter a name product= ')
    input_price=int(input('enter a price product= '))
    input_stock=int(input('enter a stock product= '))
    for line in reader:
        if line['product']==input_product:
            line['price']=input_price
            line['stock']=input_stock
    with open('products.txt', 'w') as file:
        for line in reader:
            file.write(f"Product: {line['product']}, Price: {line['price']}, Stock: {line['stock']}\n")

    print(' Product updated successfully!')

#نمایش محصولاتی که موجودی صفر دارند
def zero_balance():
    reader = read_file()
    print("****** Display all products that are out of stock ******\n")
    for line in reader:
        if line['stock']==0:
            print(line)

#نمایش همه ی محصولات
def show_all_product():
    reader=read_file()
    print("****** Show all products ******\n")
    for line in reader:
        print(line)

#موجودی های بالای 0 رو نشون میده
def count_stock():
    print("****** Product inventories that are above zero ******\n")
    for line in lst:
        if line['stock']>0:
            print(line)

#قیمت کل موجودی ها
def all_price():
    print("****** Total inventory price ******\n")
    reader=read_file()
    total_value = 0
    result_list = []
    for pro in reader:
        result = pro['price'] * pro['stock']
        total_value += result
        result_list.append(f"Product: {pro['product']} | Price: {pro['price']} | Stock: {pro['stock']} | Total: {result}")
    print(f"Total Value of All Products: {total_value}")
    return result_list

#سیو کردن اطلاعات در یک فایل جدید
def save_file():
    reader= all_price()
    with open('./new_product.txt','w') as file:
        for line in reader:
            file.writelines(line+'\n')
    print('successfully')



while True:
    print("1)Add product\n"
          "2)delete product\n"
          "3)search product\n"
          "4)update product\n"
          "5)zero_balance\n"
          "6)show_all_product\n"
          "7)Product inventories that are above zero\n"
          "8)Total inventory price\n"
          "9)save_file\n"
          "10)exit ")
    Choice=input('enter a number please= ')

    if Choice == '1':
        add_product()
    elif Choice == '2':
        del_product()
    elif Choice == '3':
        search_product()
    elif Choice == '4':
        update_product()
    elif Choice == '5':
        zero_balance()
    elif Choice == '6':
        show_all_product()
    elif Choice == '7':
        count_stock()
    elif Choice == '8':
        all_price()
    elif Choice == '9':
        save_file()
    elif Choice == '10':
        break
    else:
        print('Worning')