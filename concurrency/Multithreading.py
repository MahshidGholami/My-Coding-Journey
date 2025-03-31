import requests
from bs4 import BeautifulSoup


URL="https://www.google.com/"

response=requests.get(URL)


if response.status_code == 200 :
    soup=BeautifulSoup(response.text, "html.parser")


    product_price=soup.find("span", class_='price').text.strip()

    print(f'price= {product_price}')
else:
    print('خطا')