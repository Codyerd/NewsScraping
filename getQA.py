from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_QA(stock_code):
    url = 'https://guba.eastmoney.com/qa/qa_search.aspx?company=' + stock_code + '&keyword=&questioner=&qatype=1'
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    # Find all div elements with class "qa_list_item"
    divs = soup.find_all('div', {'class': 'qa_list_item'})
    # Extract all urls
    urls = []
    for div in divs:
        qa_answer = div.find('div', {'class': 'qa_answer'})
        a = qa_answer.find('a')  # Find all a elements in this div
        href = a.get('href')  # Get the href attribute
        if href is not None:
            urls.append("https://guba.eastmoney.com" + href)
    data = []

    for url in urls:
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        s = soup.find('div', {'class': 'newstext'})
        # ignore the bracket part
        text = s.get_text().split('】')
        text = text[1:]
        ans = text[-1].split('¶¶')
        
        data.append([ans[1][:-2], text[0][:-3], ans[0]])
       
    df = pd.DataFrame(data, columns=['Date', 'Question', 'Answer'])
    df.to_csv('./QA/'+stock_code+'_Q&A.csv', index=False, encoding='utf_8_sig')
    print(stock_code, "'s Q&A extracted")


if __name__ == '__main__':
    stock_code = '000001'
    get_QA(stock_code)