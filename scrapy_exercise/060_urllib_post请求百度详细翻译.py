# _*_ coding : utf-8 _*_
# @Time : 2023-01-11 16:37
# @Author : wws
# @File : 060_urllib_post请求百度详细翻译
# @Project : python基础

import urllib.request
import  urllib.parse
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '5e7a6733c0a796a7005a6bd62c54b6f0',
    'domain': 'common',
}
# post请求的参数 必须进行编码 并且要调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')
# 请求对象的定制
request = urllib.request.Request(url=url,data=data,headers=headers)
# 模拟浏览器服务其发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('utf-8')
print(content)
import json
obj = json.loads(content)
print(obj)