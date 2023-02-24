# _*_ coding : utf-8 _*_
# @Time : 2023-01-12 16:05
# @Author : wws
# @File : 073_解析_jsonpath
# @Project : python基础

import json
import jsonpath

obj = json.load(open('073_尚硅谷_爬虫_解析_jsonpath.json', 'r', encoding='utf-8'))
# print(obj)
# # 书店所有书作者
# author_list = jsonpath.jsonpath(obj,'$.store.book[0].author')
# # 所有的作者
# print(author_list)
# author_list = jsonpath.jsonpath(obj,'$..author')
# print(author_list)  # author_list 是一个指针 里面有自己的地址 有可以保存别人的地址 上一步 改变了 保存的地址

# store 下面的所有的元素
# tag_list = jsonpath.jsonpath(obj,'$.store.*')
# print(tag_list)

# store里面所哟丶东西price
# price_list = jsonpath.jsonpath(obj,'$.store..price')
# print(price_list)
#
# # 第三个书
# book = jsonpath.jsonpath(obj, '$..book[2]') # 两级的book[2]
# print(book)
#
# # 最后一本书
# book = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
# print(book)

# 前两本书
# book_list = jsonpath.jsonpath(obj, '$..book[:2]')
# print(book_list)
# 条件过滤需要在前面添加一个?
# 过滤出所有的包含isbn的书  ?选取过滤的文件 不要过滤的文件
# book_list = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
# print(book_list)

# 那本书超过了十块钱
book_list = jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
print(book_list)
