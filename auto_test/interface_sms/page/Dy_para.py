#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:

from page.smsTemp import *
from page.md5data import *
from testcase.test_sms import SMS


'''进行实例化'''
operationJson = OperationJson()
sms = SMS()


def DTtime(row):
    '''sign=time+signKey+params加密后的参数'''
    par = operationJson.get_json_data(row=row)
    par['time'] = p1
    par['sign'] = TY
    return par
#print(DTtime(11))
def DTtime1(row):
    '''sign=time+signKey加密后的参数'''
    par = operationJson.get_json_data(row=row)
    par['time'] = p1
    par['sign'] = TY1
    par['jsonStr'] = temp
    return par
#print(DTtime1(12))

def DTcount(row):
    """sign=time+signKey+count加密后的参数"""
    par = operationJson.get_json_data(row=row)
    par['time'] = pp1
    par['sign'] = TY2
    return par
#print(p1)
#print(DTcount(7))

def DTnotime(row):
    '''sign=time+signKey加密后的参数'''
    par = operationJson.get_json_data(row=row)
    par['time'] = pp1
    par['sign'] = TY3
    return par
#print(DTnotime(19))


'''添加模块josnStr为空'''
def DTtime3(row):
    '''sign=time+signKey加密后的参数'''
    par = operationJson.get_json_data(row=row)
    par['time'] = p1
    par['sign'] = TY1
    return par
#print(DTtime3(26))



def DTtime4(row):
    '''sign=time+signKey加密后的参数'''
    par = operationJson.get_json_data(row=row)
    par['time'] = p1
    par['sign'] = TY1
    par['jsonStr'] = json_str()
    return par
#print(DTtime4(46))



    
    




