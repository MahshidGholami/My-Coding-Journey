
from bs4 import BeautifulSoup
import requests
import pandas as pd

counter = 1
url = f'https://vulmon.com/searchpage?q=2025&sortby=bydate&page={counter}'
all_data=[]
while counter <= 10:
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        soup = BeautifulSoup(text , 'html.parser')
        cves = [i.text for i in soup.find_all('div' , attrs = {'class' : 'value'})]
        scores = [i.text for i in soup.find_all('h2' , attrs = {'class': 'header'})]
        descriptions = [i.text for i in soup.find_all('div' , attrs = {'class' : 'description'})]
        result=list(zip(cves, scores, descriptions))
        all_data.extend(result)
        print(f'Page {counter} completed successfully')
        counter+=1
    else:
        print(response.status_code)
        break
colums=['CVE' , 'SCORE' , 'DESCRIPTION' ] 
df = pd.DataFrame(all_data, columns=colums)
df.to_excel("output.xlsx", index=False)
print('Done successfully')
