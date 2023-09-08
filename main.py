import pandas as pd
import datetime
from getAnnoun import get_Announ
from getNews import get_news
from getPaper import get_paper
from getQA import get_QA

def fixStockCode(rawStockList):
    stockList = []
    for stock_code in rawStockList:
        stock_code = str(stock_code)
        if len(stock_code) > 6:
            stockList.append(stock_code[:-3])
        elif len(stock_code) < 6:
            while len(stock_code) != 6:
                stock_code = '0' + stock_code
            stockList.append(stock_code)
        else:
            stockList.append(stock_code)
    return stockList

if __name__ == '__main__':
    print("正在读取股票excel文件...")
    df = pd.read_excel('stockInfo.xlsx')
    rawStockList = df.iloc[:, 0].tolist()
    stockList = fixStockCode(rawStockList)
    
    print("读取成功")
    print('功能选项：')
    print('1. 爬取股票资讯')
    print('2. 爬取股票研报')
    print('3. 爬取股票公告')
    print('4. 爬取股票董秘问答数据')
    
    print('请选择你要是用的功能（只输入数字）： ')
    x = input()
    opt = int(x)
    
    print('请输入爬取股票的数量（只输入数字）： ')
    numNews = 10
    x = input()
    numNews = int(x)
    
    print('是否限定时间段（y/n): ')
    x = input()
    start_date = None
    end_date = None
    if (x.lower() == 'y'):
        # Prompt user for date range
        start_s = input("Enter the start date (YYYY/MM/DD): ")
        end_s = input("Enter the end date (YYYY/MM/DD): ")
        # Convert user input into datetime objects
        start_date = datetime.datetime.strptime(start_s, "%Y/%m/%d")
        end_date = datetime.datetime.strptime(end_s, "%Y/%m/%d")
    
    for i in range(numNews):
        stock_code = stockList[i]
        if (opt == 1):
            get_news(stock_code, start_date, end_date)
        elif (opt == 2):
            get_paper(stock_code, start_date, end_date)
        elif (opt == 3):
            get_Announ(stock_code, start_date, end_date)
        else:
            get_QA(stock_code)
    
    print('运行成功！')
    exit()