# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 12:19
# @Author : wws
# @File : 080_爬虫_selenium_元素信息以及交互
# @Project : python基础

from selenium import webdriver
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.baidu.com'
browser.get(url)
# 根据id找返回的不是一个列表
input = browser.find_element('su','*')
input(input.get_attribute('class'))
