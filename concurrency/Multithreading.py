import os
import time
import threading
import requests

IMAGE_URLS = [
    "https://picsum.photos/400/300",
    "https://picsum.photos/500/400",
    "https://picsum.photos/600/500",
    "https://picsum.photos/700/600",
    "https://picsum.photos/800/700",
]


OUTPUT_FOLDER = "downloaded_images"


if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def download_image(url, index):
  
    try:
        response = requests.get(url)  
        if response.status_code == 200:
            filename = os.path.join(OUTPUT_FOLDER, f"image_{index}.jpg")
            with open(filename, "wb") as file:
                file.write(response.content)  
            print(f" تصویر {index} دانلود شد: {filename}")
        else:
            print(f" خطا در دانلود تصویر {index}")
    except Exception as e:
        print(f" خطای غیرمنتظره در تصویر {index}: {e}")

if __name__ == "__main__":
    start_time = time.time()
    
    threads = []  
    for i, url in enumerate(IMAGE_URLS):
        thread = threading.Thread(target=download_image, args=(url, i+1))
        threads.append(thread)
        thread.start()  #

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f" دانلود {len(IMAGE_URLS)} تصویر در {end_time - start_time:.2f} ثانیه انجام شد.")
