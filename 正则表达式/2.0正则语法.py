# _*_ coding : utf-8 _*_
# @Time : 2023-02-24 14:03
# @Author : wws
# @File : 2.0正则
# @Project : python基础
import re

pattern = r'^[^0-9]+abc$'  # ^为匹配输入字符串的开始位置（参数字符串的开始位置）
str1 = '123abc'  # 参数字符串的结束位置
result = re.search(r'^[0-9]+abc$', str1)
print(result)
