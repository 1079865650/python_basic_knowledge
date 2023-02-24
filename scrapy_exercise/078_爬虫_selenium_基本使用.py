# _*_ coding : utf-8 _*_
# @Time : 2023-01-13 11:21
# @Author : wws
# @File : 078_爬虫_selenium_基本使用
# @Project : python基础

# 导入selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 创建浏览器操作对象
# s = Service("chromedriver.exe")
# path = 'chromedriver.exe'
# browser = webdriver.Chrome(path)
# # 访问网站
# url = 'https://www.baidu.com'
# def main():
#     browser.get(url)
# if __name__ == '__main__':
#     main()
driver = webdriver.Chrome(r'chromedriver.exe')
# driver.implicitly_wait(3)
class ServiceConfig():
    def prepareWork(self,url):
        driver.get(url)
        content = driver.page_source
        print(content)
if __name__ == '__main__':
    url = 'https://www.jd.com'
    sc = ServiceConfig()
    sc.prepareWork(url)

