import requests
import numpy as np
from bs4 import BeautifulSoup

pages = np.linspace(0,225,10)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
def movie(page):
    url = 'https://movie.douban.com/top250'+'?start='+page
    res = requests.get(url, headers=headers).text
    soup = BeautifulSoup(res, 'html.parser')
    img = soup.select('.grid_view .item .pic a img')
    for i in img:
        name = i.get('alt')
        src = i.get('src')
        img_res = requests.get(src, headers=headers)
        file = open('pic/' + name + '.jpg', 'wb')
        file.write(img_res.content)
        file.close()
for page in pages:
    page = str(page).split('.')[0]
    print(page)
    movie(page)