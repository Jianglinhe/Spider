#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-13 上午10:17
    @Author:      hezhiqiang
    @FileName:    try_lxml.py
    @IDE:         PyCharm

    lxml使用注意点:
        1.lxml能够修正html代码,但可能会改错了
            -使用etree.tostring观察修改之后的html的样子,根据修改之后的html字符串写xpath

        2.提取页面数据的思路
            -先分组,取到一个包含分组标签的列表
            -遍历,取其中每一组进行数据的提取,不会造成数据的错乱(有的组中有值为空,刻意设置为None)

        3.lxml能够接收bytes和str字符串
"""

from lxml import etree

# href = "link1.html"

text = '''<div><ul>
    <li class="item-1"><a>first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-inactive"><a href="link3.html">third item</a></li>
    <li class="item-1"><a href="link4.html">fourth item</a></li>
    <li class="item-0"><a href="link5.html">fifth item</a>
    </ul></div> '''

html = etree.HTML(text)
print(html) # <Element html at 0x7f1daf229208>
# 查看Element对象中包含的字符串
# print(etree.tostring(html).decode('utf-8')) # 将修改之后的输出观察

# 获取class为item-1 li下的a的href
ret1 = html.xpath("//li[@class='item-1']/a/@href")
print(ret1)

# 获取class为item-1 li下的a的文本
ret2 = html.xpath("//li[@class='item-1']/a/text()")
print(ret2)

# 每个li是一个新闻,把url和文本组成字典
for href in ret1:
    item = {}
    item["href"] = href
    item["title"] = ret2[ret1.index(href)]
    print(item)

print("*"*100)

# 分组,根据li标签进行分组,对每一组继续写xpath
ret3 = html.xpath("//li[@class='item-1']")  # 得到的是Element对象数组
for i in ret3:
    item = {}
    # i.xpath("./a/text()")结果是列表,要把其中的元素拿出来,即title拿出来
    item['title'] = i.xpath("./a/text()")[0] if len(i.xpath("//a/text()"))>0 else None
    item['href'] = i.xpath("./a/@href")[0] if len(i.xpath("./a/@href"))>0 else None

    print(item)
