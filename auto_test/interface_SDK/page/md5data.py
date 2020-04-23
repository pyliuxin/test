#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:
'''md5加密'''
from utils.operationJson import *
import time
import hashlib
from utils.accesstoke import get_token

T = round(int(time.time()*1000))
T1 = str(T)
#print(T1)

opera = OperationJson()

'''从json文件中取参数'''
a = opera.get_json_data(1)
# a2 = opera.get_json_data(56)  #a2是获取富阳接口的signkey，appkey这俩参数
# print(a2)
'''从列表a中获取需要的参数'''
b = a['signKey'],a['time'],a['appKey']
c = list(b)
p1 = c[0]
p2 = T1
p3 = c[2]
#print(p3)

"""data=从json中提取动态变量time+signKey+appkey"""
data = p1 + p2 + p3

"""data=从json中提取动态变量time+signKey"""
data1 = p1 + p2

def md5_file1():
    """time+signKey进行加密"""
    D1 = data
    para1 = hashlib.md5(D1.encode()).hexdigest()
    return para1
TY = md5_file1()
#print(TY)

'''从json文件中获取到含有accessToken的参数'''
tok = opera.get_json_data(48)
#print(tok)
'''索引出accesssToken并赋值'''
tok['pubParam']['accessToken'] = get_token()
#print(get_token())

sin = opera.get_json_data(56)
#print(sin)



