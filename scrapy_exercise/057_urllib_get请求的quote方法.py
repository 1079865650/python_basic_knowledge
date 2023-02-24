# _*_ coding : utf-8 _*_
# @Time : 2023-01-11 13:55
# @Author : wws
# @File : 057_urllib_get请求的quote方法
# @Project : python基础

# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
# 需要unicode转义
import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd='
# 请求对象的定制为了解决反扒的第一种手段
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
# 将汉字变成unicode编码的格式 我们需要依赖于urllib.parse
name = urllib.parse.quote('周杰伦')
url = url + name
print(url)
print(name)
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取相应的内容
content = response.read().decode('utf-8')
# 打印数据
print(content)
