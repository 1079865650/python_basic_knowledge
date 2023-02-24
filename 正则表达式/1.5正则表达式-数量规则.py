# _*_ coding : utf-8 _*_
# @Time : 2023-02-10 16:03
# @Author : wws
# @File : test01
# @Project : python基础
import re
tel = '13512354611'
# [1] [358] [56789]
# print(re.match('\d*', tel))
print(re.match('^1[358][5-9]\d{8}$', tel))  # ^1 不是取反
str1 = 'I put a lighted match to the letter and watched it burn.'
print(re.findall(r'ed\b', str1))  # 找到所有的'ed'
print(re.findall('\\bed', str1))  # 以'ed'开头的
print(re.findall('\\Bed', str1))  # 不是以'ed' 开头的


