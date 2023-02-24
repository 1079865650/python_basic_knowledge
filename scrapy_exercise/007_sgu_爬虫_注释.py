# _*_ coding : utf-8 _*_
# @Time : 2023-01-10 11:22
# @Author : wws
# @File : 007_sgu_爬虫_注释
# @Project : python基础

# import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'
# url代表的是下载的路径 filename文件的名字
# 在python中可以变量的名字 也可以直接写值
# urllib.request.urlretrieve(url_page,'baidu.html')
# 下载图片
# url_img = 'https://img0.baidu.com/it/u=1309359181,3567527426&fm=253&fmt=auto&app=138&f=JPEG?w=281&h=499'
# urllib.request.urlretrieve(url_img,'lisa.jpg')
# 下载视频
# url_video = 'https://www.bilibili.com/f92c2582-e36c-4359-b47d-b6d83680c221'
# urllib.request.urlretrieve(url_video,'bilibili.mp4')
import urllib.request
url = 'https://www.baidu.com'
# url的组成
# http/https  SSL加密 更加安全
# 协议
# 协议 主机 端口号
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
# 以为urlopen方法中不能存储字典 所以不能传入
# 请求对象定制
# 因为参数顺序的问题 不能直接写url 和 headers 中间还有一个data 需要 关键字 传参 先优先关键字 没有关键字 默认顺序
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)



