#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-12 下午3:17
    @Author:      hezhiqiang
    @FileName:    get_36k.py
    @IDE:         PyCharm
"""

import re
import json

from parse_url import parse_url

url = "https://36kr.com/"

html_str = parse_url(url)

ret = re.findall("<script>window.initialState=(.*?)</script>", html_str)[0]

with open('36kr.json', 'w', encoding='utf-8') as f:
    f.write(ret)


ret = json.loads(ret)
print(ret)