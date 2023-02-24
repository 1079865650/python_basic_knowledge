# _*_ coding : utf-8 _*_
# @Time : 2023-02-10 17:54
# @Author : wws
# @File : 1.9re模块-方法详解
# @Project : python基础
import re

content = '''<title>this is python</title>'''
res = re.compile(r'<title>([\w\W]*)</title>')
print(res.match(content))

