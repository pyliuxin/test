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
        """参数data不存在变量"""
        try:
            r=requests.post(url=self.excel.get_Url(row=row),
                            data=self.operationJson.get_json_data(row=row),
                            headers=getHeadersValue())
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生异常')
        pass
    
    def post1(self,row,data):
        """参数data中存在变量"""
        try:
            r=requests.post(url=self.excel.get_Url(row=row),
                            data=data,
                            headers=getHeadersValue())
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生异常')