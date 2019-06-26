#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @Time:        19-6-22 下午3:04
    @Author:      hezhiqiang
    @FileName:    try_selenium.py
    @IDE:         PyCharm
"""


from selenium import webdriver

# 实例化一个浏览器
driver = webdriver.Chrome()

# 发送请求
driver.get("http://www.baidu.com")
