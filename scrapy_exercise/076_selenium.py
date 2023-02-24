# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 11:04
# @Author : wws
# @File : 076_selenium
# @Project : python基础

import urllib.request
url = 'https://www.jd.com/'

response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
print(content)