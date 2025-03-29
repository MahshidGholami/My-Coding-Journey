#توسعه سیستمی که تصاویر را همزمان به چندین فرمت (PNG, JPEG, WebP) تبدیل کند

#**********************************************
import os
import time
import multiprocessing
from PIL import Image
#**********************************************

#مسیر پوشه ورودی و خروجی
INPUT_FOLDER="input_folder"
OUTPUT_FOLDER="output_folder"

#فرمت ها
FORMATES=["JPEG", "PNG", "WEBP"]

#بررسی و ایجاد پوشه خروجی در صورت نبودن 
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

#تبدیل تصویر به فرمت های مختلف
def convert_image(image_path):
    try:
        image=Image.open(image_path)
        filename=os.path.splitext(os.path.basename(image_path))[0]

        for frm in FORMATES:
            output_path=os.path.join(OUTPUT_FOLDER, f'{filename}.{frm.lower()}')
            image.save(output_path,format=frm)
            print(f" {filename} -> {frm} ذخیره شد در {output_path}")
    except Exception as e:
        print(f'خطا در پردازش {image_path}: {e}')

if __name__ == '__main__':
    start_time=time.time()
    #دریافت لیست تصاویر در پوشه ورودی
    images = [os.path.join(INPUT_FOLDER, f) for f in os.listdir(INPUT_FOLDER) if f.endswith(('jpg', 'jpeg', 'png'))]

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
                pool.map(convert_image, images)
    
    end_time = time.time()
    print(f" پردازش {len(images)} تصویر در {end_time - start_time:.2f} ثانیه انجام شد.")


