from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

def get_news(stock_code, start_date=None, end_date=None):
    url = 'http://guba.eastmoney.com/list,' + stock_code + ',1,f.html'
    headers={'User-Agent':'Mozilla/5.0'}
    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    # print(soup.prettify())
    # exit()
    s1 = soup.find_all('div',{'class':'title'}) 
    s2 = soup.find_all('div',{'class':'update'})
    # print(s1)
    # exit()
    news = []
    for i in range(1,len(s1)):
        title = s1[i].get_text()
        if (title[-1] == '）'):
            title = title[:-7]
        year = datetime.datetime.now().year
        news.append([f'{year}-{s2[i].string}', title])
        print(stock_code, "added", i, "news")

    df = pd.DataFrame(news, columns=['Publish Date', 'Text'])
    if (start_date != None):
        df['Publish Date'] = pd.to_datetime(df['Publish Date'], errors='coerce')  
        df = df[(df['Publish Date'] >= start_date) & (df['Publish Date'] <= end_date)]

    df.to_csv('./news/'+stock_code+'_news.csv', index=False, encoding='utf_8_sig')
    
if __name__ == '__main__':
    stock_code = '000998'
    get_news(stock_code)