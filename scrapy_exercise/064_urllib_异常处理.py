# _*_ coding : utf-8 _*_
# @Time : 2023-01-12 9:46
# @Author : wws
# @File : 064_urllib_异常处理
# @Project : python基础

import urllib.request
import urllib.error
# url = 'https://blog.csdn.net/Jason_WSYCY/article/details/1243802731'
url = 'http://www.doudan111.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
try:
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('系统正在升级..')
except urllib.error.URLError:
    print('piece of shit')


