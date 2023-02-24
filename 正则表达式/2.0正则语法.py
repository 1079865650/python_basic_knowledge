# _*_ coding : utf-8 _*_
# @Time : 2023-02-24 14:03
# @Author : wws
# @File : 2.0正则
# @Project : python基础
import re

"""
    re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置match()返回none
"""
"""
    search 匹配参数字符串中 第一次满足的
    findall 返回参数字符串中所有满足的
    ^ 为参数字符串的开始位置 方括号里面表示取反
    $ 参数字符串的结束位置
    + 前面的字符出现次数 >=1  {1,}
    * 前面的字符出现次数 >=0  {0,}
    ? 前面的字符出现次数 <=1  {0,1}
    | 两项之间的一个选择
    \\s 匹配所有空白符，包括换行  
    \\w 匹配字母，数字，下划线 == [A-Za-z0-9-]
    \\n 匹配一个换行符
    \\f 匹配一个换页符
    \\r 匹配一个回车符
    \\t 匹配一个制表符
    \\v 匹配一个垂直制表符
    \\d 匹配一个数字字符 等价于[0-9]
    {n} {n,} {n,m} {0,} >=0    {n} == n  {n,} >=n  {,m} <=m  {n,m} >=n <=m  
    定位符:
    ^ 匹配输入字符串开始的位置
    & 匹配输入字符串结束的位置
    \\b 匹配一个单词边界  'er\b' 匹配 'never'
    \\B 非单词边界匹配
    选择：
    exp1(?=exp2):查找后面是exp2的exp1             (?<=exp2)exp1：查找前面是exp2的exp1
    exp1(?!exp2):查找后面不是exp2的exp1          (?<!exp2)exp1：查找前面不是exp2的exp1
"""

pattern = r'^[^0-9]+abc$'  # ^为匹配输入字符串的开始位置（参数字符串的开始位置）
str1 = '123abc'  # 参数字符串的结束位置
result = re.search(r'^[0-9]+abc$', str1)

str1 = 'google runoob _taobao'
result = re.search(r'[a-zA-Z\s]+', str1)  # 匹配空格 直接在[] 输入空格 或者\s

result = re.search(r'[A-Za-z0-9_\s]+', str1)  # 字母数字下划线
str1 = '0234'
result = re.search(r'.*', str1)
str1 = '<h1>RUNOOB-菜鸟教程</h1>'
result = re.search(r'<\w+?>', str1)  # 贪婪模式 尽可能多匹配 ?贪婪但是不是十分贪婪 碰到第一个结束的 > 就结束
str1 = '123456runoob1123runoob456'
result = re.findall(r'([1-9])([a-z]+)', str1)  # <class 'list'>
# print(type(result))
result1 = re.search('([1-9])([a-z]+)', str1)
# print(result1[1], "=====result1")
# for r in result1:
#     print(r, "===r")  # TypeError:  're.Match'
# print(type(result1))
str1 = '123456runoob-google123runoob456'
result1 = re.search(r'(?<!123)runoob', str1)
result2 = re.search(r'(?<=123)runoob', str1)
result3 = re.search(r'runoob(?=456)', str1)
result4 = re.search(r'runoob(?!456)', str1)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
str1 = 'https://www.runoob.com:80/html/html-tutorial.html'
result = re.search(r'(\w+):\/\/([^\/]+)\/([^\/]+)\/([^\/]+)html', str1)  # object is not  iterable
str1 = 'Google runoob taobao runoob'
result = re.search(r'runoob', str1)
str1 = 'never'
result = re.search(r'er\b', str1)  # 但返回的不是单词 而是查找的字符串 单词边界查找
str1 = 'abcd test@runoob.com 1234'
result = re.search(r'[\w.%=-]+@[\w.-]+\.[a-zA-Z]{2,6}\b', str1)
str1 = 'abc123-_def'
result = re.search(r'[a-zA-Z0-9]*-_[a-z]{,3}', str1)
str1 = '<div id="mydiv"(([\s\S])*?)<div>asdsa</div></div>'
print(result)
