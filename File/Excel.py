
import pandas as pd
#فایل اکسل
INPUT_FILE='Excel.xlsx'
#استعلام محصولاتی که تمام شدن
def inventory():
    filter_inventory="تمام‌شده"
    all_product=pd.read_excel(INPUT_FILE , usecols=["وضعیت محصول", "محصول"])
    filtered_data = all_product[all_product['وضعیت محصول']== filter_inventory ]
    print(filtered_data)

#تعداد فروش هر محصول
def sale():
    all_product=pd.read_excel(INPUT_FILE, usecols=["تعداد فروش", "محصول"])
    print(all_product)

#پر فروش ترین محصول
def Best_selling_product():
    all_product=pd.read_excel(INPUT_FILE, usecols=["تعداد فروش", "محصول"])
    Max=all_product["تعداد فروش"].max()
    filter_product= all_product[all_product['تعداد فروش'] == Max ]
    print(filter_product)

#محبوب ترین روش پرداخت
def payment():
    pass







Best_selling_product()
# OUTPUT_FILE='New_Excel.xlsx'
# read.to_excel(OUTPUT_FILE, index=False)