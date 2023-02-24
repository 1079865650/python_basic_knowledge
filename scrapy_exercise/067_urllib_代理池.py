proxies_pool = [
    {'http':'202.109.157.66:9000'},
    {'http':'202.109.157.66:90001'},
    {'http':'202.109.157.66:90002'},
]
import random

proxies = random.choice(proxies_pool)

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
import urllib.request
request = urllib.request.Request(url=url,headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('daili.html', 'w', encoding='utf-8')as fp:
    fp.write(content)