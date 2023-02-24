# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 15:16
# @Author : wws
# @File : 086_requests_post请求
# @Project : python基础
import encodings

import requests
url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

data = {
    'kw': 'eye'
}
# url请求地址
# data请求参数
# kwargs字典
response = requests.post(url=url,data=data,headers=headers) # 关键字传递没有先后顺序
content = response.text
import json
# 该方法已经删除
# obj = json.loads(content,encodings='utf-8')
obj = json.loads(content.encode('utf-8'))
print(obj)
# 总结:
# post请求 不需要编解码
# post请求的参数是data
# 不需要请求对象的定制