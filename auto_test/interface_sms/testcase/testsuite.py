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
        start_dir = os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None)
    return suite
#print(alltests())


def GetNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())

'''将执行的文件写入report中并生成html报告'''
def run():
    fp = os.path.join(os.path.dirname(__file__),'report',GetNowTime() + 'TestReport.html')
    HTMLTestRunner.HTMLTestRunner(
        stream = open(fp,'wb'),
        title = '短信平台自动化测试报告',
        description = '自动化测试报告详细信息').run(alltests())

if __name__ == '__main__':
    run()


'''查看当前目录'''
# print(os.path.dirname(__file__))

'''查看report目录'''
# print(os.path.join(os.path.dirname(__file__),'report'))