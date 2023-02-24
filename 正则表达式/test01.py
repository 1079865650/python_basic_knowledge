# _*_ coding : utf-8 _*_
# @Time : 2023-02-10 17:14
# @Author : wws
# @File : test01
# @Project : python基础
import re


str1 = 'aadata.dat'
pattern = r'data(\w)?\.dat'  # \. ?
re1 = re.search(pattern, str1)  # <re.Match object; span=(0,8), match='data.dat'>
print(re1.start())  # start() 开始的下标 end() 返回的下标




