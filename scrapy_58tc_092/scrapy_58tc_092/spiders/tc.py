import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://zz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_D']
    # https://zz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_D
    start_urls = ['https://zz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_D']

    def parse(self, response):
        # response.text 获取响应的字符串
        # content = response.text
        # 二进制数据
        # 获取的是二进制数据
        # content = response.body
        # print('=================')
        # print(content)
        span_list = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        print("========================")
        print(span_list)

        pass
