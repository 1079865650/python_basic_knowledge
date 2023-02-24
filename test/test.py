# _*_ coding : utf-8 _*_
# @Time : 2023-02-23 13:59
# @Author : wws
# @File : test
# @Project : python基础
import datetime
import re

# date_time = datetime.date.today() - datetime.timedelta(days=30)
# # date_time = datetime.datetime.now()
# # print(type(date_time))
# # print(date_time)
# start_time = datetime.date.today()
# end_time = start_time - datetime.timedelta(days=20)
# date_time01 = datetime.date(2022, 1, 1)
# print(type(date_time01), date_time01)
# print(type(start_time), type(end_time))
# print(start_time, end_time)

# p1 = re.match(r'(HBL |File_)((.*?)(,|\d$))')
str1 = 'Invoice Pack - Dest Rotterdam, HBL CGOA29353, ETA_ 08-01-23, SEA, ZHENGZHOU LEDREM NETWORK TECHNOLOGY CO LTD'
# str2 = re.findall(r'(HBL |File_)((.*?)(,|\d$))', str1)
str2 = 'Invoice Pack - Dest Rotterdam, HBL CGOA26724, ETA_ 07-10-22, SEA, ZIEL INTERNATIONAL CO., LIMITED'
# str4 = re.search(r'(HBL |File_)((.*?)(,|\d$))', str3)
# print(str4)
# pattern = re.compile(r'(HBL |File_)((.*?)(,|\d$))')
# result = pattern.search(str1)
# print(type(result))
# print(result)
# rs = result.group()
# print(type(rs))
# print(rs)

uid_list = {'PFR': 1, 'PFR': 2, 'DGF': 3}
print(type(uid_list.keys()))  # <class 'dict_keys'>

item = {'aa': 11}
key = item.keys()
for k in key:
    print(k, type(k))
print(key[0])




