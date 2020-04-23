#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:
import requests
from utils.excel_data import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

class Method:

    def __init__(self):
        self.excel=OperationExcel()
        self.operationJson=OperationJson()

    def post(self,row):
        """参数中不存在data中的变量参数时使用"""
        try:
            r=requests.post(url=self.excel.get_Url(row=row),
                            json=self.operationJson.get_json_data(row=row),
                            headers=getHeadersValue())
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生异常')
        pass
    
    def post1(self,row,data):
        """参数中存在data中的变量参数时使用"""
        try:
            r=requests.post(url=self.excel.get_Url(row=row),
                            json=data,
                            headers=getHeadersValue())
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生异常')

    def post2(self,data1):
        """获取accesstoken使用"""
        try:
            r = requests.post(url='https://api.heplat.com/iface2/getToken',
                              json=data1,
                              headers=getHeadersValue())
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生异常')
        pass
    
    def post3(self,data2):
        """获取accesstoken使用"""
        try:
            r = requests.post(url='https://api.heplat.com/iface2/getSmsCode',
                              json=data2,
                              headers=getHeadersValue())
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生异常')
        pass