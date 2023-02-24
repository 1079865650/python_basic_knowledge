# _*_ coding : utf-8 _*_
# @Time : 2023-01-12 10:25
# @Author : wws
# @File : 066_urllib_handler处理器的基本使用
# @Project : python基础

# 使用handler来访问百度 获取 网页源码

import urllib.request
url = 'http://www.baidu.com'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url,headers=headers)
# handler build_opener open
# 获取hanlder对象
handler = urllib.request.HTTPHandler()
# 获取opener对象
opener = urllib.request.build_opener(handler)
# 调用opne方法
response = opener.open(request)
content = response.read().decode('utf-8')
print(content)
