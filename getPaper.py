from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime


def get_paper(stock_code, start_date=None, end_date=None):
    url = 'http://guba.eastmoney.com/list,' + stock_code + ',2,f.html'
    headers={'UserWarning-Agent':'Mozilla/5.0'}
    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    s1 = soup.find_all('span',{'class':'l3 a3'}) 
    s2 = soup.find_all('span',{'class':'l5 a5'})

    news = []
    # download top 10 announcements at the moment
    for i in range(1,11):
        try:
            news.append([s2[i].string, s1[i].string])
            print(stock_code, "added ", i, " papers")
        except:
            print(stock_code, "stopped after", i, 'iterations')
            break
        
    df = pd.DataFrame(news, columns=['Publish Date', 'Text'])
    if (start_date != None):
        df['Publish Date'] = pd.to_datetime(df['Publish Date'], errors='coerce')  
        df = df[(df['Publish Date'] >= start_date) & (df['Publish Date'] <= end_date)]

    df.to_csv('./papers/'+stock_code+'_papers.csv', index=False, encoding='utf_8_sig')
    
        

if __name__ == '__main__':
    stock_code = '300318'
    get_paper(stock_code)