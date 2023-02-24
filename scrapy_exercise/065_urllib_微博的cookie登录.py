# _*_ coding : utf-8 _*_
# @Time : 2023-01-12 9:55
# @Author : wws
# @File : 065_urllib_微博的cookie登录
# @Project : python基础

# 适用的场景: 数据采集的时候 需要绕过登录 然后进入到某个页面
# 请求不成功 很大可能是 请求头的信息不够
import urllib.request
url = 'https://m.weibo.cn/profile/6746284330'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
# (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
# (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('utf-8')
# 将数据保存到本地
with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)
