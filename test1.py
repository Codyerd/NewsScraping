from bs4 import BeautifulSoup
import requests

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/si",
	"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
	"Connection": "keep-alive",
	"Accept-Encoding": "gzip, deflate, br",
	"Host": "so.eastmoney.com",
	# 需要更换Cookie
	"Cookie": "qgqp_b_id=0a8278adcbfe5cb20ba41e266b16d6e1; HAList=ty-0-000001-%u5E73%u5B89%u94F6%u884C%2Cty-116-01810-%u5C0F%u7C73%u96C6%u56E2-W%2Cty-0-301179-%u6CFD%u5B87%u667A%u80FD%2Cty-0-002230-%u79D1%u5927%u8BAF%u98DE; st_si=75868804832188; st_pvi=65687750529230; st_sp=2023-05-17%2022%3A16%3A25; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=5; st_psi=20230524092455313-118000300903-8483795642; st_asi=delete"
}
#html.encoding = html.apparent_encoding
def get_url_list(keyword):
    url = 'https://so.eastmoney.com/news/s?'
    params = {'keyword': keyword, 'sort': 'default'}
    response = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())
    exit()
    results = soup.find_all('div', class_='news_item_url')
    print(results)
    exit()
    for result in results:
        try:
            title = result.h3.a.text
            link = result.h3.a['href']
            desc = result.find('div', class_='c-abstract').text
            print(title)
            print(link)
            print(desc)
        except:
            pass


if __name__ == '__main__':
    keyword = '平安银行'
    get_url_list(keyword)