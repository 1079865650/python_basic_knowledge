# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 14:51
# @Author : wws
# @File : 084_爬虫_requests_基本使用
# @Project : python基础

import requests
url = 'http://www.baidu.com'
response = requests.get(url=url)
# 一个类型和六个属性
# print(type(response))
# 设置响应的编码格式
# response.encoding = 'utf-8'
# 以字符串的形式来返回了网页的源码
# print(response.text)
# 返回url地址
# print(response.url)
# b'<><>' 返回的是二进制的数据 binary binary binary binary binary
# print(response.content)
# 响应状态码
# print(response.status_code)
# 返回的是响应头
print(response.headers)









