from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver

def get_tmp():
    # Path to the webdriver
    driver_path = r'C:\Users\25074\Downloads\webdriver'
    driver = webdriver.Chrome(driver_path)
    url = 'https://finance.eastmoney.com/a/ccjxw.html'
    headers={'UserWarning-Agent':'Mozilla/5.0'}
    # Go to the page
    driver.get(url)

    # Get the dynamically-loaded HTML and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Close the driver
    driver.quit()
    urls = []
    # Find the div element
    div = soup.find('ul', {'id': 'newsListContent'})
    news_list = div.find_all('p',{'class':'title'}) 
    for news in news_list:
        urls.append(news.get_text())
        
    print(urls)
    
    
if __name__ == '__main__':
    stock_code = '000001'
    get_tmp()