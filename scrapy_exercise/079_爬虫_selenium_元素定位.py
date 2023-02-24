# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 11:59
# @Author : wws
# @File : 079_爬虫_selenium_元素定位
# @Project : python基础
from selenium import webdriver
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.baidu.com'
browser.get(url)
# 元素定位
# 根据id来找到对象
button = browser.find_element('id','su')
print(button)

# 根据标签属性的属性值来获取对象的
# button = browser.find_element('input','button')
# 根据xpath语句来获取对象
# button = browser.find_elements('//input[@id="su"]')

# 根据标签的名字来获取对象
# button = browser.find_elements('input')
# print(button)

# button = browser.find_element('#su')
# print(button)

button = browser.find_element()