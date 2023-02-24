# _*_ coding : utf-8 _*_
# @Time : 2023-01-10 11:26
# @Author : wws
# @File : 008_爬虫_变量
# @Project : python基础

# 使用urllib来获取百度首页的源码
import urllib.request
# 定义一个url
url = 'http://www.baidu.com'
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
# 获取相应中的页面的源码
# read方法 返回的是字节新式的二进制数据
# 我们要将二进制的数据转换为字符串
# 二进制 到字符串 解码
content = response.read().decode('utf-8')
# 打印数据
print(content)











