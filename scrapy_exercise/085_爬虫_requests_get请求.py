# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 15:01
# @Author : wws
# @File : 085_爬虫_requests_get请求
# @Project : python基础

# urllib
# 一个类型以及六个方法
# get请求
# post请求 百度翻译
# ajax的get请求
# ajax的post请求
# cookie登录 微博
# 代理

# requests
# 一个类型以及六个属性
# get请求
# post请求
# 代理
# cookie  验证码

import requests
url = 'https://www.baidu.com/s?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
data = {
    'wd': '北京'
}
# url 请求资源路径
# params 参数
# kwargs 字典
response = requests.get(url=url,params=data,headers=headers)
content = response.text # content是二进制 .text转换为文本
print(content)
# 总结:
# 参数使用params传递
# 参数无需urlencode编码
# 不需要请求对象的定制
# 请求资源路径中？会自动拼接
