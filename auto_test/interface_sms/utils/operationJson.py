#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:


import json
from utils.public import *
from utils.operationExcel import OperationExcel

class OperationJson:
    def __init__(self):
        self.excel = OperationExcel()

    def getReadJson(self):
        with open(data_dir(fileName='requestData.json'),encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    def get_json_data(self,row):
        '''获取请求参数'''
        a = json.dumps(self.getReadJson()[self.excel.get_Requestdata(row=row)])
        return json.loads(a)
    

opera=OperationJson()
a = opera.get_json_data(1)
#print(a)