# _*_ coding : utf-8 _*_
# @Time : 2023-01-12 9:13
# @Author : wws
# @File : 063_urllib_ajax的post请求肯德基官网
# @Project : python基础

# 1页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname:北京
# pid:
# pageIndex:1
# pageSize:10

# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname:北京
# pid:
# pageIndex:2
# pageSize:10

import urllib.request
import urllib.parse
# base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    # post请求 必须编码 编码之后再encode
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    # 创建一个自定义的request
    request = urllib.request.Request(url=base_url,headers=headers,data=data)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    # 发送request获得response 然后在response里面解析数据 解码方式'utf-8'
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    # 打开一个json文件 然后写入文件 打开一个文件指定编码方式
    with open('kfc_'+str(page)+'.json','w',encoding='utf-8',) as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        # 请求对象的定制  注释也得缩进一格
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载  content没有接受 所以没法调用
        down_load(page,content)















