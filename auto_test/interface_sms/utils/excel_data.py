#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:


class ExcelVariable:
    '''定义excel变量'''
    caseID=0
    title=1
    URL=2
    requestData=3
    Expect=4
    Result=5

def getCaseID():
    return ExcelVariable.caseID
def getUrl():
    return ExcelVariable.URL
def getRequestData():
    return ExcelVariable.requestData
def getExpect():
    return ExcelVariable.Expect
def getResult():
    return ExcelVariable.Result

def getHeadersValue():
    '''获取请求头'''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;Charset=UTF-8',
        'User-Agent': '',
        'Cookie': '',
        'Referer': ''}
    return headers