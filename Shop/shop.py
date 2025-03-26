import csv


file_name='inventory.txt'

#تابع برای خواندن
def read_shop():
        with open(file_name , 'r' , newline='' , encoding='utf-8') as file:
            reader=csv.DictReader(file)
            return list(reader)

#برای خواندن محصولات
def display_shop():
    inventory = read_shop()
    for item in inventory:
        print(f"{item['id']} - {item['name']} | {item['category']} | قیمت: {item['price']} | تعداد: {item['quantity']}")


#تابع برای اضافه کردن محصول
def add_shop ():
    inventory_id=input('enter a id for product= ')
    inventory_name=input('enter a name for product= ')
    inventory_category=input('enter a category for product= ')
    inventory_price=input('enter a price for product= ')
    inventory_quantity=input('enter a quantity for product= ')

    with open(file_name , 'a' , newline='\n' , encoding='utf-8') as file:
        field_name=['id' , 'name', 'category' ,'price','quantity']
        witer= csv.DictWriter(file ,fieldnames=field_name )

        file.seek(0,2)
        if file.tell() == 0:
            witer.writeheader()
        witer.writerow({'id':inventory_id , 'name':inventory_name , 'category':inventory_category,'price':inventory_price, 'quantity':inventory_quantity})
        print(f" محصول {inventory_name} با موفقیت اضافه شد!")

#بروزرسانی محصول
def update_shop():
    inventory=read_shop()
    product_id = input("شناسه محصول: ")
    new_quantity = input("تعداد جدید: ")
    for item in inventory:
        if item['id'] == product_id:
             item["quantity"] = new_quantity
             break
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "category", "price", "quantity"])
        writer.writeheader()
        writer.writerows(inventory)
        print("موجودی به‌روزرسانی شد.")


#حذف محصول
def del_shop():
    inventory=read_shop()
    product_id = input("شناسه محصول: ")
    inventory=[item for item in inventory if item['id'] !=product_id]

    with open(file=file_name ,mode='w', newline='' , encoding='utf-8') as file:
        witer=csv.DictWriter(file , fieldnames=['id','name','category','price','quantity'])
        witer.writeheader()
        witer.writerows(inventory)
    print("محصول حذف شد.")





#جستجو محصول
def search_shop():
    inventory = read_shop()
    search_name = input("نام محصول موردنظر: ").lower()

    results = [item for item in inventory if search_name in item["name"].lower()]
    if results:
        for item in results:
            print(f"{item['id']} - {item['name']} | قیمت: {item['price']} | تعداد: {item['quantity']}")
    else:
        print("محصولی یافت نشد.")


#
def main():
    while True:
        print("\nسیستم مدیریت موجودی فروشگاه")
        print("1. نمایش موجودی")
        print("2. اضافه کردن محصول جدید")
        print("3. به‌روزرسانی موجودی")
        print("4. حذف محصول")
        print("5. جستجو محصول")
        print("6. خروج")

        choice = input("انتخاب کنید: ")

        if choice == "1":
            display_shop()
        elif choice == "2":
            add_shop()
        elif choice == "3":
           update_shop()
        elif choice == "4":
            del_shop()
        elif choice == "5":
            search_shop()
        elif choice == '6':
            print(" خروج از برنامه...")
            break
        else:
            print(" انتخاب نامعتبر! لطفاً عدد صحیح وارد کنید.")

if __name__ == "__main__":
    main()
