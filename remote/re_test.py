#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-12 下午4:19
    @Author:      hezhiqiang
    @FileName:    re_test.py
    @IDE:         PyCharm

    测试正则表达式
    注意:
        -re.findall("a(.*?)b", "str") 能够返回括号中间的内容,括号起到定位和过滤的效果
        -原始字符串r,待匹配字符串中有反斜杠的时候,使用r能忽视反斜杠带来的转义效果
        -点号默认情况下平匹配不到'\n'
        -\s的能够匹配到空白字符,不仅仅包括空格,还有\t
"""

import re
b = "chuan1zhi2"

# sub替换
print(re.sub("\d", "_", b)) # 产生一个新的字符串
print(b)


# compile方法来节省时间,直接添加正则表达式
p = re.compile("\d")
print(p.findall(b))
print(p.sub("_", b))


print(r'\n')    #  添加r表示原始字符串

c = r'a\nb'
print(len(c))
print(c[1])