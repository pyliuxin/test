#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:



from page.md5data import *

T = round(int(time.time()*1000))
T1 = str(T)
'''进行实例化'''
operationJson = OperationJson()

def DTtime(row):
    '''读取time参数后的data'''
    par = operationJson.get_json_data(row=row)
    par['sign'] =TY
    par['time'] = p2
    return par
#print(DTtime(48))

def DTtime1(row):
    '''获取动态acctoken的data'''
    par = operationJson.get_json_data(row=row)
    par['pubParam']['accessToken'] = get_token()
    return par
#print(DTtime1(79))

def DTtime2(row):
    '''获取动态acctoken的data及sign'''
    par = operationJson.get_json_data(row=row)
    par['pubParam']['accessToken'] = get_token()
    par['pubParam']['sign'] = TY
    return par
#print(DTtime2(79))









