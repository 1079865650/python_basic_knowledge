# _*_ coding : utf-8 _*_
# @Time : 2023-02-10 14:07
# @Author : wws
# @File : test
# @Project : python基础
import re

# print(re.match('.', 'sweb'))  # '.' 可以匹配任意字符 除了 \n
# print(re.match('.', '\n'))  # None
# print(re.match('.', '\t'))  # <re.Match object; span=(0,1), match='\t'>
# # \d 表示0-9之间的任意数字 包含字符吗？
# print(re.match('\d', '0$adsd'))  # 可以匹配字符 里面只能放str 是不是正则只匹配str
# # match try to apply the pattern at the start of the string
# # \D 表示非数字
# print(re.match('\D', '\n$adsasd'))  # 11匹配不上 可能只匹配第一个 \n 不加r 算一个字符串
# # \s 表示空白字符
# print(re.match('\s', "\t"))
# # \S 表示非空白字符
# print(re.match('\S', "\\t"))  # \\ 表示双\\ \t表示两个空白
# # 大小写字母，或则数字，下划线
# print(re.match('\w', '\\'))
# print(re.match('\w', '_____')) # only the first character can be matched
# print(re.match('\W', '$$#$'))
# print(re.match('[adbc]', 'ab'))  # the first character is in []?
# print(re.match('[abcd]', 'cd'))  # 匹配的是后一个字符
# print(re.match('[a-e]', 'cb'))  # a-e 之间所有的字母
# print(re.match('[0-9]', '3a'))  #
# print(re.match('[A-Z]', 'F3A'))
# print(re.match('[^a-e]', 'fb'))  # 取反 不是这里面的符号 可以 不是这里面的数字 全部替换为空
# print(re.match('[f-z]', 'fb'))
# print(re.match('[a-zA-Z]', 'F3a'))  # 包含里面所有的内容
# print(re.match('[0-9][0-9]', '100'))  # 匹配前两个数
# print(re.match('[0-9][a-b]', '5a'))  # 匹配前两个字符
# print(re.match('[\w\W][\w\W]', '我rG2#')) # 一个[]里面匹配一个
# str1 = r'c:\\python\ne\test.py'
# print(str1)
# print(re.match('\d', '\d'))
# print(re.match('\\d', '\d'))
# print(re.match('\\\d', '\d'))
# print(re.match('\\\\d', '\d'))  # \\\\也能匹配
#
# # 有限使用python ,在使用正则表达式处理字符
# print(re.match('\\n', '\n'))
# 匹配一个电话
print(re.match('\d'*11, '13898761234'))  # 既然里面放字符串就可以使用python关于字符串的语法
print(re.match('\d*', '13898a761234'))  # 贪婪匹配 尽可能多的匹配
# +
print(re.match('\d+', '138987a612#34'))  # 贪婪模式
print(re.match('\d?', '138987a612#34'))
print(re.match('\d?', 'a'))  # 0次或则多次
print(re.match('\d?', 'a'))

# {m},{m},{m,n}
print(re.match('\d{3}', '138987a612#34'))
print(re.match('\d{5,}', '138987a612#34'))  # 至少{5,} 至少五次以上




