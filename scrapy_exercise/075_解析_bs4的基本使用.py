# _*_ coding : utf-8 _*_
# @Time : 2023-01-12 17:45
# @Author : wws
# @File : 075_解析_bs4的基本使用
# @Project : python基础

from bs4 import BeautifulSoup

# 解析本地文件 来讲bs4基础语法进行讲解
# 默认打开的文件的编码格式是gbk 所以在打开文件的时候需要制定编码
soup = BeautifulSoup(open('075_解析_bs4的基本使用.html',encoding='utf-8'),'lxml')
# 根据标签名字接着查找
# 找到的是第一个符合条件的数据
# print(soup.a)
# 获取标签的属性和属性值
# bs4的一些函数
# find
# 返回的是第一个符合条件的数据
# find_all
# 返回的是所有符合条件的数据
# select
# print(soup.find('a'))
# print(soup.find('a',title="a2"))
# print(soup.a.attrs)
# print(soup.find('a',class_="a1"))  # 找到 a标签中 class="a1"这个属性的所有信息
# # 如果想获取的是多个标签的数据 那么需要在find_all的参数中添加的是列表的数据
# print(soup.find_all(['a','span']))
# # limit的作用是查找前几个数据
# print(soup.find_all('li',limit=2))

# select(推荐) 返回是一个列表 并且返回多个数据
# print(soup.select('a'))
# print(soup.select('.a1')) # .代表class  class=a1 的标签类选择器
# print(soup.select('#l1'))
# # 属性选择器
# # 查找到li标签中有id的标签 li中有id的标签 通过属性来寻找对应的标签
# print(soup.select('li[id]'))
# 查找到li标签中id为12的标签
# print(soup.select('li[id="l2"]'))
# 层级选择器
# 后代选择器
# 找到的是div下面的li
# print(soup.select('div li'))
# 子代选择
# 某标签的第一季子标签
# 注意: 很多的计算机编程语言中 如果不加空格不会输出内容bs4中 不会报错 会显示内容
# print(soup.select('div > ul > li')) # 选取的数据放在列表里面我
# 找到a标签和li标签的所有对象
# print(soup.select('a,li')) # a li标签都拿到
# 节点信息的模块
# 获取节点内容
obj = soup.select('#d1')[0]  # 获取的是列表 列表里面保存了该标签所有内容 包括下级标签的内容
# 所以这个数据结构不一定是str所有String可能获取不到数据
# 如果标签对象中只有内容那么string和get_text()都可以使用
# 如果标签对象中 除了内容还有标签  那么string就获取不到数据 get_text是可以获取数据的
# print(obj.string)
# print(obj.get_text())
# 节点的属性
# obj = soup.select('#p1')[0]
# # name是标签的名字
# # print(obj.name)
# print(obj.attrs)  # 将属性值作为一个字典返回

# 获取节点的属性
obj = soup.select('#p1')[0]
print(obj.attrs.get('class'))
print(obj.get('class'))













