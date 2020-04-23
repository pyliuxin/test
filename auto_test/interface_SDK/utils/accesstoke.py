#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:

from Methodfengzhuang.method import *
import time
import hashlib
import json

'''获取accesstoken的参数'''
access_par = {"appId":"e0393ef5e01544bda2ecfa643621f17c","time":"","passWord":""}
T = round(int(time.time()*1000))
T1 = str(T)
#print(T1)
P = 'Wfov2DT9iXH'
S = P + T1

def pwdss():
    """password+time进行加密"""
    password = hashlib.md5(S.encode()).hexdigest()
    return password
#print(pwdss())
pwd = pwdss()
access_par["passWord"] = pwd
#print(pwd)
access_par["time"] = T
get_accesstoekn = {"pubParam":access_par} #获取accesstoken函数打印出含有access的value
#print("获取accesstoken的参数:"%get_accesstoekn)   #获取token接口的参数：appid   time   passWord


def get_token():
    '''获取accesstoken接口返回的accessToken值'''
    obj = Method()
    r = obj.post2(data1=get_accesstoekn)
    param = json.loads(r.text)
    # 实时获取动态accesstoken接口返回的数据
    token_value = param['data']['accessToken']
    return token_value
#print(get_token())