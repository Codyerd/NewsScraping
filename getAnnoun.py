from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_Announ(stock_code, start_date=None, end_date=None):
    # getting url list
    url_list = []
    # Gallery of stock announcements
    url = 'http://guba.eastmoney.com/list,' + stock_code + ',3,f.html'
    headers={'User-Agent':'Mozilla/5.0'}
    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    # print(soup.prettify())
    # exit()
    s1 = soup.find_all('div',{'class':'title'}) 

    # include top 10 announcements 
    # index starts with 1 since s1[0] is the headers
    for i in range(1,min(11, len(s1))):
        url_list.append('https://guba.eastmoney.com' + s1[i].a.attrs['href'])
    
    # save file
    data = []
    for url in url_list:
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        # print(soup.prettify())
        # exit()
        s1 = soup.find('p', class_='publishdate')
        s2 = soup.find('p', style='line-height: 164.28%;') 
        try:
            data.append([s1.text[5:], s2.text[:-11]])
            print(stock_code, "added 1 announcement!")
        except:
            print(stock_code, "stuck!")
            continue
    
    df = pd.DataFrame(data, columns=['Publish Date', 'Text'])
    if (start_date != None):
        df['Publish Date'] = pd.to_datetime(df['Publish Date'], errors='coerce')  
        df = df[(df['Publish Date'] >= start_date) & (df['Publish Date'] <= end_date)]

    df.to_csv('./announcements/'+stock_code+'_announs.csv', index=False, encoding='utf_8_sig')
    print(stock_code, "'s announcements ready")

 

if __name__ == '__main__':
    # change stock_code by your interest
    stock_code = '000998'

    get_Announ(stock_code)
    