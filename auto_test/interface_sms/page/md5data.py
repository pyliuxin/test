#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:
'''md5加密'''
from utils.operationJson import *
import time
import hashlib

T = round(int(time.time()*1000))
T1 = str(T)
#print(type(T1))
opera = OperationJson()
'''从json文件中取参数'''
a = opera.get_json_data(1)
'''从列表a中获取需要的参数'''
b = a['time'],a['signKey'],a['params']
c = list(b)
p1 = T1
p2 = c[1]
p3 = c[2]
"""data=从json中提取动态变量time+signKey+params"""
data = p1 + p2 + p3
"""data=从json中提取动态变量time+signKey"""
data1 = p1 + p2
#print(data)





"""data2=从json中提取动态变量time+signKey+count"""
a1 = opera.get_json_data(7)
b1 = a1['time'],a1['signKey'],a1['count']
c1 = list(b1)
pp1 = T1
pp2 = c1[1]
pp3 = c1[2]
data2 = pp1 + pp2 + pp3
# print(data2)
pt1 = ""
pt2 = c1[1]
#print(pt2)
'''time ='' + signkey'''
data3 = pt1 + pt2
def md5_file():
    """time+signKey+params进行加密"""
    D = data
    para = hashlib.md5(D.encode()).hexdigest()
    return para
TY = md5_file()
#print(TY)

def md5_file1():
    """time+signKey进行加密"""
    D1 = data1
    para1 = hashlib.md5(D1.encode()).hexdigest()
    return para1
TY1 = md5_file1()      #TY1是time+signkey的加密结果
#print(TY1)

def md5_file2():
    """time+signKey+count进行加密"""
    D2 = data2
    para2 = hashlib.md5(D2.encode()).hexdigest()
    return para2
TY2 = md5_file2()      #TY2是time+signkey+count的加密结果
#print(TY2)

def md5_file3():
    """time(为空字符串)+signkey进行加密"""
    D3 = data3
    para2 = hashlib.md5(D3.encode()).hexdigest()
    return para2
TY3 = md5_file3()
#print(TY3)

