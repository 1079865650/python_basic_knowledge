# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 14:20
# @Author : wws
# @File : 082_爬虫_selenium_phantomjs的基本使用
# @Project : python基础

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    # path是你自己的chrome浏览器的文件路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    # path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser
browser = share_browser()
browser.get('http://www.baidu.com/')














