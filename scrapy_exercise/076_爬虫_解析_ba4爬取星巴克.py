# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 10:22
# @Author : wws
# @File : 076_爬虫_解析_ba4爬取星巴克
# @Project : python基础

import urllib.request
url = 'https://www.starbucks.com.cn/menu/'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'lxml')
# //ul[@class="grid padded-3 product"]//strong/text()
name_list = soup.select('ul[class="grid padded-3 product"] strong')
for name in name_list:
    print(name.get_text())






