# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 15:54
# @Author : wws
# @File : 088_爬虫_requests_cookie登录古诗文网
# @Project : python基础

# 通过登录进入到主页面
# _VIEWSTATE:YS2MwgZOb0Mg9Joxswf95OxEv2EAnvBeMZ3NtSGwJjxofta9x/UdlBcjQ3r8eM8N3SKSfLLfPiUl5/zCJupu0lvt4uzfJq1xVKBZyJdXWoIPGkwy4i4EJ2TgOYn5WTWmLzOby24f45pQ3vJFnDF6Y5ffc40=
# __VIEWSTATEGENERATOR:C93BE1AE
# from:http://so.gushiwen.cn/user/collect.aspx
# email:18348441679@163.com
# pwd:qweqweq
# code:bx90
# denglu:登录

# (1)_VIEWSTATE _VIEWSTATEEGENERATOR 在页面的源码中 获取页面的源码 然后在源码里面解析数据就可以了
# (2)验证码
import requests
# 这是登录页面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
# 获取页面的源码
response = requests.get(url = url,headers=headers)
content = response.text
# print(content)
# 解析页面源码 然后获取
from bs4 import BeautifulSoup
soup = BeautifulSoup(content,'lxml')
# 获取_VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
# 获取_VIEWSTATEGENERATOR  因为__写成_所以没拿到数据 报列表越界
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# print(viewstate)
# print(viewstategenerator)
# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn'+code
# print(code_url)
# 有坑
import urllib.request
urllib.request.urlretrieve(url=code_url,filename='code.jpg')
# 获取了验证码的图片之后 下载到本地然后观察验证码 观察之后在控制台输入这个验证码 就可以将这个值给code
# code的参数就可以登录
code_name = input('请输入你的验证码')


















