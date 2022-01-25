import requests

url = 'https://weibo.com/u/5502931489'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
res = res.text
print(res)