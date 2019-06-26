#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-4 下午3:20
    @Author:      hezhiqiang
    @FileName:    demo7.py
    @IDE:         PyCharm
"""


"""
    正向代理和反向代理的区别:
        是否知道最终服务器的地址
    
        1.正向代理(知道的),如vpn
        2.反向代理(真不知道),如nginx,更加安全
        
        requests中的使用代理
    
    使用代理ip注意事项:
        1.可以使用requests添加超时参数,判断ip质量
        2.在线代理ip质量检测网站
        3.不能一直使用一个代理ip,应该一开始准备一堆ip地址,组成ip池,随机选择一个ip来使用
        4.如何随机选择代理ip(让使用次数较少的ip地址有更大机会被使用)
            -{"ip":ip, "times":0}
            -[{},{},{}]对ip列表按使用次数进行排序,选择使用次数较少的10个ip地址,从中进行随机选择一个

"""

import requests

proxies = {
    "http": "182.91.216.7:25321"
}

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

r = requests.get("https://www.baidu.com/", proxies=proxies, headers=headers)

print(r.status_code)




