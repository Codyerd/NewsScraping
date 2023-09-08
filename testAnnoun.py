import requests
from bs4 import BeautifulSoup

req = requests.get("https://guba.eastmoney.com/o/news,000001,1306582539.html")
soup = BeautifulSoup(req.text, 'html.parser')
s1 =  soup.find('p', style='line-height: 164.28%;') 
print(s1.text)
