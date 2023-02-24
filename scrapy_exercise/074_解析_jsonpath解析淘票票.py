# _*_ coding : utf-8 _*_
# @Time : 2023-01-12 16:37
# @Author : wws
# @File : 074_解析_jsonpath解析淘票票
# @Project : python基础

import urllib.request
url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1673513071800_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    # ':authority':' dianying.taobao.com',
    # ':method':' GET',
    # ':path':' /cityAction.json?activityId&_ksTS=1673513071800_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme':' https',
    'accept':' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding':' gzip, deflate, br',
    'accept-language':' zh-CN,zh;q=0.9',
    'bx-v':' 2.2.3',
    'cookie':' cna=Db0dHKPyxjACAasIBgjhGZzy; miid=25183201284696141; t=afaeed2cc91a02efa3aa2c4f5c752d1b; cookie2=1ed13c59f45fa4922a6285e43ffa7f55; v=0; _tb_token_=5b07ee375b3e9; xlly_s=1; tb_city=110100; tb_cityName="sbG+qQ=="; tfstk=cv0cBjbaHmrfWYLtFxaXJpmay--dZjQaKVuSzQRzWhZ-umgPixjPYzw9Z-vB3G1..; l=fBxjxjTmT6z2Vj7FBOfwPurza77OxIRfguPzaNbMi9fPO3fH5zCNW673rn8MCnGVEsp2J3PZC7jvBo88gPaTCg9vK_ANBu-QDdTnwpzHU; isg=BAcHae6fKCHtf6y7ybDFQCPOlrvRDNvuArNr7dn0bBa9SCYK4Nj2PGGG6ggWoLNm',
    'referer': 'https://dianying.taobao.com/index.htm?spm=a1z21.3046609.city.1.20c0112a28x7O9&n_s=new&city=110100',
    'sec-ch-ua':' "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile':' ?0',
    'sec-ch-ua-platform':' "Windows"',
    'sec-fetch-dest':' empty',
    'sec-fetch-mode':' cors',
    'sec-fetch-site':' same-origin',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with':' XMLHttpRequest'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# split 切割
content = content.split('(')[1].split(')')[0]
with open('074_解析_jsonpath解析淘票票.json', 'w', encoding='utf-8')as fp:
    fp.write(content)
# print(content)
import json
import jsonpath
# 参数 不是一个字符串对象 而是一个文件 对象 使用open打开文件创建对象
obj = json.load(open('074_解析_jsonpath解析淘票票.json', 'r', encoding='utf-8'))
city_list = jsonpath.jsonpath(obj,'$..regionName')
print(city_list)
