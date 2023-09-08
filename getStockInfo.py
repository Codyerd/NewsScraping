import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrape_stock_data(stock_code):
    url = 'https://q.stock.sohu.com/zs/' + stock_code + '/lshq.shtml'
    headers = {'UserWarning-Agent': 'Mozilla/5.0'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    print(soup.prettify())
    exit()
    tbody = soup.find('table', {'class': 'tableQ', 'id': 'BTZ_hq_historySearch'}).find('tbody')
    rows = tbody.find_all('tr', {'style': True})
    # delete first row 
    rows = rows[1:]
    data = []
    for row in rows:
        columns = row.find_all('td')
        row_data = [column.text.strip() for column in columns]
        data.append(row_data)

    columns = ['Date', 'Open', 'Close', 'amount_change', 'amount_change_percent', 'Low', 'High', 'Volume', 'volume_currency', 'rand'] 
    df = pd.DataFrame(data, columns=columns)

    return df


if __name__ == '__main__':
    stock_code = '000001'
    df = scrape_stock_data(stock_code)
    print(df)
