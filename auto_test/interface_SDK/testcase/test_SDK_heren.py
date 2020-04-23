#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:

import unittest
from Methodfengzhuang.method import Method
from page.Dy_para import *
from utils.accesstoke import *

class SDK_HEREN(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        pass

    def test_hospitals_001(self):
        '''和仁-获取医疗机构信息-成功'''
        r = self.obj.post1(row=1, data=DTtime(1))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "成功")
        print(r.text)

    
    def test_hospitals_002(self):
        '''和仁-获取医疗机构信息-区域不存在'''
        r = self.obj.post1(row=2, data=DTtime(2))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0021")
        self.assertEqual(r.json()['msg'], "区域不存在")
        print(r.text)
        
    def test_departments_001(self):
        '''和仁-获取医院科室信息-根据 orgCode 查找 Node 错误'''
        r = self.obj.post1(row=3, data=DTtime(3))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-8")
        self.assertEqual(r.json()['msg'], "根据 orgCode 查找 Node 错误")
        print(r.text)
        
    def test_departments_002(self):
        '''和仁-获取医院科室信息-请求参数[startDateTime]不能为空'''
        r = self.obj.post1(row=4, data=DTtime(4))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0006")
        self.assertEqual(r.json()['msg'], "请求参数[startDateTime]不能为空")
        print(r.text)
        
    def test_departments_003(self):
        '''和仁-获取医院科室信息-成功'''
        r = self.obj.post1(row=5, data=DTtime(5))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "成功")
        print(r.text)
        
        
    def test_doctorinfo_001(self):
        '''和仁-获取医疗机构内部医生信息-成功'''
        r = self.obj.post1(row=6, data=DTtime(6))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "成功")
        print(r.text)
        
    def test_doctorinfo_002(self):
        '''和仁-获取医疗机构内部医生信息-请求参数[orgCode]不能为空'''
        r = self.obj.post1(row=7, data=DTtime(7))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0006")
        self.assertEqual(r.json()['msg'], "请求参数[orgCode]不能为空")
        print(r.text)
        
    def test_deptSchedule_001(self):
        '''和仁-按科室查询医生排班-成功'''
        r = self.obj.post1(row=8, data=DTtime(8))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "成功")
        print(r.text)
    
    def test_deptSchedule_002(self):
        '''和仁-按科室查询医生排班，跟上一个endtime不同-无法查询当前科室的挂号排班信息'''
        r = self.obj.post1(row=9, data=DTtime(9))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-1")
        self.assertEqual(r.json()['msg'], "无法查询当前科室的挂号排班信息！")
        print(r.text)
        
    def test_deptSchedule_003(self):
        '''和仁-按科室查询医生排班-请求参数[startDateTime]不能为空'''
        r = self.obj.post1(row=10, data=DTtime(10))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0006")
        self.assertEqual(r.json()['msg'], "请求参数[startDateTime]不能为空")
        print(r.text)
        
    def test_doctorSchedule_001(self):
        '''和仁-按医生查询医生排班-成功'''
        r = self.obj.post1(row=11, data=DTtime(11))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "成功")
        print(r.text)
        
    def test_doctorSchedule_002(self):
        '''和仁-按医生查询医生排班-请求参数[orgCode]不能为空'''
        r = self.obj.post1(row=12, data=DTtime(12))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0006")
        self.assertEqual(r.json()['msg'], "请求参数[orgCode]不能为空")
        print(r.text)
        
    def test_doctorSchedule_003(self):
        '''和仁-按医生查询医生排班-请求参数[deptCode]不能为空'''
        r = self.obj.post1(row=13, data=DTtime(13))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0006")
        self.assertEqual(r.json()['msg'], "请求参数[deptCode]不能为空")
        print(r.text)
        
    def test_doctorSchedule_004(self):
        '''和仁-按医生查询医生排班-请求参数[doctorCode]不能为空'''
        r = self.obj.post1(row=14, data=DTtime(14))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0006")
        self.assertEqual(r.json()['msg'], "请求参数[doctorCode]不能为空")
        print(r.text)
        
    def test_doctorSchedule_005(self):
        '''和仁-按医生查询医生排班-请求参数[startDateTime]不能为空'''
        r = self.obj.post1(row=15, data=DTtime(15))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0006")
        self.assertEqual(r.json()['msg'], "请求参数[startDateTime]不能为空")
        print(r.text)
        
    def test_doctorSchedule_006(self):
        '''和仁-按医生查询医生排班-请求参数[endDateTime]不能为空'''
        r = self.obj.post1(row=16, data=DTtime(16))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0006")
        self.assertEqual(r.json()['msg'], "请求参数[endDateTime]不能为空")
        print(r.text)
        
    def test_numberInfo_001(self):
        '''和仁-按排班班次查询号源详情-无法查询当前号源的排班信息'''
        r = self.obj.post1(row=17, data=DTtime(17))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-1")
        self.assertEqual(r.json()['msg'], "无法查询当前号源的排班信息！")
        print(r.text)
        
    def test_numberInfo_002(self):
        '''和仁-按排班班次查询号源详情-字段[periodType]定值范围校验失败1,2'''
        r = self.obj.post1(row=18, data=DTtime(18))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-109")
        self.assertEqual(r.json()['msg'], "字段[periodType]定值范围校验失败1,2")
        print(r.text)
        
    def test_numberInfo_003(self):
        '''和仁-按排班班次查询号源详情-成功'''
        r = self.obj.post1(row=19, data=DTtime(19))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "成功")
        print(r.text)

    def test_registerNumber_001(self):
        '''和仁-预约挂号-字段[accountType]定值范围校验失败01,02,03,04,05,99'''
        r = self.obj.post1(row=20, data=DTtime(20))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-109")
        self.assertEqual(r.json()['msg'], "字段[accountType]定值范围校验失败01,02,03,04,05,99")
        print(r.text)
    
    def test_registerNumber_002(self):
        '''和仁-预约挂号-服务内部错误'''
        r = self.obj.post1(row=21, data=DTtime(21))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-1")
        self.assertEqual(r.json()['msg'], "服务内部错误")
        print(r.text)
        
    def test_treatments_001(self):
        '''根据证件号码查询就诊列表-成功'''
        r = self.obj.post1(row=22,data=DTtime(22))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"成功")
        print(r.text)
        
    def test_treatments_002(self):
        '''根据证件号码查询就诊列表-请求参数[idType]不能为空'''
        r = self.obj.post1(row=23,data=DTtime(23))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0006")
        self.assertEqual(r.json()['msg'],"请求参数[idType]不能为空")
        print(r.text)
        
    def test_treatments_003(self):
        '''根据证件号码查询就诊列表-成功'''
        r = self.obj.post1(row=24,data=DTtime(24))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"成功")
        print(r.text)

    def test_archival_001(self):
        '''查询用户基本档案信息-appkey为空'''
        r = self.obj.post1(row=25,data=DTtime(25))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"-201")
        self.assertEqual(r.json()['msg'],"未查询到患者的基本信息")
        print(r.text)
        
    def test_archival_002(self):
        '''查询用户基本档案信息-成功'''
        r = self.obj.post1(row=26,data=DTtime(26))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"成功")
        print(r.text)
        
    def test_isSigned_001(self):
        '''查询用户是否签约-成功-患者不具备签约资格，未签约，不可进行信用就医'''
        r = self.obj.post1(row=27,data=DTtime(27))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"成功")
        self.assertEqual(r.json()['signInfo']['reason'], "患者不具备签约资格，未签约，不可进行信用就医")
        print(r.text)
        
    def test_isSigned_002(self):
        '''查询用户是否签约-患者未建档'''
        r = self.obj.post1(row=28,data=DTtime(28))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"成功")
        self.assertEqual(r.json()['signInfo']['reason'],"患者未建档")
        print(r.text)
        
    def test_subscription_001(self):
        '''查询用户信息和签约信息-患者未建档---此接口未使用有问题'''
        r = self.obj.post1(row=29,data=DTtime(29))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"-100")
        self.assertEqual(r.json()['msg'],"字段[idNo]不能为空")
        print(r.text)
        
    def test_creditLimit_001(self):
        '''查询用户信用额度--服务内部错误'''
        r = self.obj.post1(row=30,data=DTtime(30))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"-1")
        self.assertEqual(r.json()['msg'],"服务内部错误")
        print(r.text)

    def test_examineList_001(self):
        '''检查索引列表-成功'''
        r = self.obj.post1(row=31,data=DTtime(31))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"成功")
        print(r.text)
    
    def test_detectionList_001(self):
        '''按照证件号码查询检验索引列表-成功'''
        r = self.obj.post1(row=32,data=DTtime(32))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"成功")
        print(r.text)

    def test_prescriptionList_001(self):
        '''处方索引列表-成功'''
        r = self.obj.post1(row=33,data=DTtime(33))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"成功")
        print(r.text)
        
    def test_costList_001(self):
        '''费用索引列表-服务内部错误-院方问题'''
        r = self.obj.post1(row=34,data=DTtime(34))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"-1")
        self.assertEqual(r.json()['msg'],"服务内部错误")
        print(r.text)
        
    def test_mobilePhone_001(self):
        '''修改用户签约手机号码-服务内部错误-院方问题'''
        r = self.obj.post1(row=38,data=DTtime(38))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"-1")
        self.assertEqual(r.json()['msg'],"服务内部错误")
        print(r.text)
        
    def test_menzhen_001(self):
        '''门诊索引列表---接口错误-500'''
        r = self.obj.post1(row=39,data=DTtime(39))
        self.assertEqual(r.status_code,200)
        # self.assertEqual(r.json()['code'],"500")
        # self.assertEqual(r.json()['msg'],"服务内部错误")
        # print(r.text)
        
    def test_mezhenxq_001(self):
        '''门诊详情'''
        r = self.obj.post1(row=40,data=DTtime(40))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0016")
        self.assertEqual(r.json()['msg'],"获取用户信息失败")
        print(r.text)
        
    def test_regions_001(self):
        '''获取地区列表-500需要修改'''
        r = self.obj.post1(row=41,data=DTtime(41))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0021")
        self.assertEqual(r.json()['msg'],"region为空")
        print(r.text)
        
    
        
    






if __name__ == '__main__':
    unittest.main(verbosity=2)


    
    
