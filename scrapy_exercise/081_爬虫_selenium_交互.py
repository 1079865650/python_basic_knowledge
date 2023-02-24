# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 13:55
# @Author : wws
# @File : 081_爬虫_selenium_交互
# @Project : python基础
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url
url = 'https://www.baidu.com'
browser.get(url)
import time
time.sleep(2)
# 获取文本框对象
input = browser.find_element('id','kw')
# 在文本框输入对象
input.send_keys('周杰伦')
time.sleep(2)
# 获取百度一下的按钮
button = browser.find_element('id','su')
# 点击按钮 获取的对象可以使用点击指令
button.click()
time.sleep(2)
# 滑到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(2)
# 获取下一页按钮
# next = browser.find_element_by_xpath('//a[@class="n"]')  方法过时了
# chrome = Chrome # 启动chromedriver
next = browser.find_element(By.XPATH, '//a[@class="n"]')
# next点击下一页
next.click()
time.sleep(2)
# 回到上一页
browser.back()
time.sleep(2)
# 回去
browser.forward()
time.sleep(2)
# 退出
browser.quit()
