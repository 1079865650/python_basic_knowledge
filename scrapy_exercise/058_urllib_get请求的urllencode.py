# _*_ coding : utf-8 _*_
# @Time : 2023-01-11 14:23
# @Author : wws
# @File : 058_urllib_get请求的urllencode
# @Project : python基础

# https://www.baidu.com/s?wd=周杰伦&sex=男
# import urllib.parse
# data = {
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国台湾省'
# }
# # 吧列表中的键值对用&拼接起来
# a = urllib.parse.urlencode(data)
# print(a)

# 获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%E7%9C%81
import urllib.request
import urllib.parse
base_url = 'https://www.baidu.com/s?'
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}
new_data = urllib.parse.urlencode(data)
print(new_data)
#请求资源路劲
url = base_url + new_data
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器想服务器发送请求
response = urllib.request.urlopen(request)
# 获取网页源码的数据
content = response.read().decode('utf-8')
# 打印数据
print(content)