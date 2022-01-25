# 爬取新浪新闻
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
url = 'https://news.sina.com.cn/china/'
code = requests.get(url,headers=headers).encoding
print(code)  # ISO-8859-1

'''先编码，再获取text，就不会乱码'''
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
res = res.text
soup = BeautifulSoup(res, 'html.parser')
a = soup.select('.main-content .left-content-1 ul li a')
title = []
href = []
for i in a:
    title.append(i.text)
    href.append(i['href'])
news = pd.DataFrame()
news['标题'] = title
news['链接'] = href
print(news)
