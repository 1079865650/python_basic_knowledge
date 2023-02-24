# _*_ coding : utf-8 _*_
# @Time : 2023-01-11 17:21
# @Author : wws
# @File : 062_urllib_ajax的get请求豆瓣前10页
# @Project : python基础

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
# start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20
# start=20#limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20
# start=40&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=60&limit=20
# start=60&limit=20
# page 1 2 3 4
# start 0 20 40 60
# start (page - 1)*20
# 下载豆瓣电影前10页的数据
# (1) 请求对象定制
# (2) 获取相应的数据
# (3) 下载数据

import urllib.parse
import urllib.request
def  create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    # post 请求需要加encode get请求不需要
    data = urllib.parse.urlencode(data)
    url = base_url + data
    print(url)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
# 程序的入口
def down_load(page,content):
    with open('douban_' + str(page) + '.json','w',encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始的页码:'))
    end_page = int(input('请输入结束的页码:'))
    for page in range(start_page,end_page + 1):
        print(page)
        # return一个返回值然后接收 传参给下一个方法
        request = create_request(page)
        # 获取响应的数据
        content = get_content(request)
        # 下载
        down_load(page,content)
