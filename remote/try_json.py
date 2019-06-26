#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-10 下午8:53
    @Author:      hezhiqiang
    @FileName:    try_json.py
    @IDE:         PyCharm

    json在数据交换中起到一个载体的作用,承载着相互传递的数据

    json使用注意点
        -json字符串都是双引号引起来的
            -如果不是双引号
                -eval:能实现简单的字符串和python类型的转换
                -replace:把单引号替换为双引号
        -往一个json文件中写入多个json串,不再是一个json串,不能直接读取
            - 一行写一个json串,按照行来读取


"""


import requests
import json
from pprint import pprint   # 美化输出


url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&for_mobile=1&callback=jsonp1&start=0&count=18&loc_id=108288&_=0"

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer': 'https://m.douban.com/movie/nowintheater?loc_id=108288'
}

data = {
    'start' : '0',
    'count': '18',
    'loc_id': '108288',
}

response = requests.get(url=url, headers=headers, data=data)

html_str = response.content.decode()
# print(html_str) # str
html_str_new = html_str.replace(';jsonp1(', '').replace(');', '')   # 去掉这个结构;jsonp1();变成json格式
# print(html_str_new)


# json.loads()把json字符串转化为python类型
ret = json.loads(html_str_new)
# pprint(ret)
# print(type(ret))    # <class 'dict'>

# json.dumps() 将python字典类型转换为json字符串
# indent=2作用是格式化json,更加美观的展现
# ensure_ascii=False默认为True,以ascii码写入,需要保留中文,设置为False
# with open('douban.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(ret, ensure_ascii=False, indent=2))



# json.loads() 将json字符串转换为python字典
# with open('douban.json', 'r', encoding='utf-8') as f:
#     ret2 = f.read()
#     ret2 = json.loads(ret2)
#     print(ret2)
#     print(type(ret2))



# 类文件对象,具有read()和write()方法的对象就是类文件对象

# 使用json.load提取类文件对象中的数据(从douban.json中将数据读取出来)
with open('douban.json', 'r', encoding='utf-8') as f:
    ret3 = json.load(f)
    print(ret3)
    print(type(ret3))   # <class 'dict'>


# json.dump() 将python类型放入类文件对象中
with open('douban1.json', 'w', encoding='utf-8') as f:
    json.dump(ret, f, ensure_ascii=False, indent=2)


