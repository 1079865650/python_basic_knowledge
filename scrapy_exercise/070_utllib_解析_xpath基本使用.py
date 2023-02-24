# _*_ coding : utf-8 _*_
# @Time : 2023-01-12 12:08
# @Author : wws
# @File : 070_utllib_解析_xpath基本使用
# @Project : python基础

# 来自 lxml下面的 import包 etree
from lxml import etree
# xpath解析
# 本地文件 etree.parse etree.html()
# 服务器响应数据 response.read()decode('utf-8') ****
# xpath解析本地文件
tree = etree.parse('070_utllib_解析_xpath基本使用.html')
print(tree)
#  tree.xpath('xpath路径')
# 查找ul下面的li
# tree.xpath('xpath路径')
# 查找所有id的属性的li标签 text()获取标签中的内容
# li_list01 = tree.xpath('//ul/li[@id="l1"]/text()')
# li_list = tree.xpath('//body//li')  # 一个/儿子 //孙子
# # 判断列表的长度
# print(li_list)
# print(len(li_list))
# print(li_list01)
# print(len(li_list01))
# 查找到id为l1的li标签的class的属性值
# # 判断列表的长度
# li = tree.xpath('//ul/li[@id="l1"]/@class')

# 查新id中包含l的li标签s
# li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')

# 查询id的值以l开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
# 查询id为l1和class为c1的数据
# li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
# 查询出来 放在一个列表里面
li_list = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')
print(li_list)
print(len(li_list))







