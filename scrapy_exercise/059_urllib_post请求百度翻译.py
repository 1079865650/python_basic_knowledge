# _*_ coding : utf-8 _*_
# @Time : 2023-01-11 14:47
# @Author : wws
# @File : 059
# @Project : python基础

# post请求
import urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
data = {
    'kw': 'spider'
}
# post 请求的参数 必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')
# print(data)
# post请求的参数 是不会拼接在url后面的 而是需要放在请求对象定制的参数中
# post请求的参数 必须要进行编码
request = urllib.request.Request(url=url,data=data,headers=headers)
# print(request)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取相应的数据
print(response)
# 获取相应的数据
content = response.read().decode('utf-8')
print(content)
print(type(content))
import  json
obj = json.loads(content)
print(obj)
