# _*_ coding : utf-8 _*_
# @Time : 2023-02-10 16:23
# @Author : wws
# @File : test01
# @Project : python基础
import re
t = "2021-09-31"
print(re.match('2021-09-24', '2021-09-24'))
print(re.match('\d{4}-\d{2}-24', '2021-09-24'))
print(re.match('\d{4}-(0[1-9]|1[0-2])-([0-2]\d|[3][0-1])', t))  # |或则 |的优先级比较高 把前后划分成两端
print(re.match('\d{4}-(0[1-9]|1[0-2])-([0-2]\d|[3][0-1])', t).group())
print(re.match('\d{4}-(0[1-9]|1[0-2])-([0-2]\d|[3][0-1])', t).group(0))
print(re.match('\d{4}-(0[1-9]|1[0-2])-([0-2]\d|[3][0-1])', t).group(1))
print(re.match('\d{4}-(0[1-9]|1[0-2])-([0-2]\d|[3][0-1])', t).group(2))
print(re.match('(\d{4})-(0[1-9]|1[0-2])-([0-2]\d|[3][0-1])', t).group(1))  # .group()的分组是按()来分组的 从1开始
