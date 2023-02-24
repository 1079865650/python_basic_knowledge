# _*_ coding : utf-8 _*_
# @Time : 2023-01-12 14:07
# @Author : wws
# @File : 071_解析_百度网站
# @Project : python基础

# （1）获取网页的源码
# （2）解析 解析的服务器响应的文件 etree.HTML
# （3）打印
import urllib.request
url = 'https://www.baidu.com'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器访问服务器
response = urllib.request.urlopen(request)
# 获取网页源码
content = response.read().decode('utf-8')
# print(content)
# 解析网页源码来获取 我们的想要的数据
from lxml import etree

# 解析服务器响应的文件
tree = etree.HTML(content)
# 获取想要的数据 xpath的返回值是一个列表类型的数据
# 返回的数据类型是一个 列表 然后[0] 获取列表的第一个元素
result = tree.xpath('//input[@id="su"]/@value')[0]

print(result)

















