# _*_ coding : utf-8 _*_
# @Time : 2023-01-11 16:56
# @Author : wws
# @File : 061_urllib_ajax的get请求豆瓣电影第一页
# @Project : python基础
import urllib.request

# get请求
# 获取豆瓣电影的第一页数据 并且保存起来
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
# 获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)
# # 数据下载到本地
# fp = open('douban.json','w',encoding='utf-8') # 写进去的有中文需要定义编码格式
# fp.write(content) # content是上面read()爬虫到的数据
with open('douban1.json','w',encoding='utf-8') as fp:
    fp.write(content)