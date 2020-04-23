#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:

import os
import unittest
import time
import HTMLTestRunner


def alltests():
    suite = unittest.TestLoader().discover(
        start_dir= os.path.dirname(__file__),
        #pattern='test_SDK_c*.py',
        #pattern='test_SDK_fu*.py',    #执行不同方法下的测试用例切换方法名
        pattern='test_SDK_he*.py',
        top_level_dir=None
    )
    return suite
#print(alltests())

def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())

def run():
    fp = os.path.join(os.path.dirname(__file__),'report',getNowTime() + 'TestReport.html')
    HTMLTestRunner.HTMLTestRunner(
        stream=open(fp,'wb'),
        title='接口平台自动化测试报告',
        description= '自动化测试报告详细信息').run(alltests())
    
if __name__ == '__main__':
    run()