# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 15:38
# @Author : wws
# @File : 087_爬虫_requests_代理
# @Project : python基础

import requests
url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

data = {
    'wd': 'ip'
}
proxy = {
    'http':'121.13.252.61:3256'
}
# get参数可以放字典
response = requests.get(url=url,params=data,headers=headers,proxies=proxy)
content = response.text
with open('daili.html', 'w', encoding='utf-8')as fp:
    fp.write(content)