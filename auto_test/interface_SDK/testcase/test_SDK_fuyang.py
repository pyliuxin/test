#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:

import unittest
from page.Dy_para import *
from Methodfengzhuang.method import *
from utils.accesstoke import *


class SDK_FUYANG(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        pass
    
    def test_app_get_ghks_001(self):
        '''富阳-获取科室'''
        r = self.obj.post1(row=48, data=DTtime1(48))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "获取成功")
        print(r.text)
    
    def test_app_get_ghks_002(self):
        '''富阳-获取科室'''
        r = self.obj.post1(row=49, data=DTtime1(49))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0021")
        self.assertEqual(r.json()['msg'], "区域不存在")
        print(r.text)
    
    def test_app_get_ghks_003(self):
        '''富阳-获取科室'''
        r = self.obj.post1(row=50, data=DTtime1(50))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0006")
        self.assertEqual(r.json()['msg'], "请求参数[zzjgdm]不能为空")
        print(r.text)
    
    def test_app_get_yljg_001(self):
        '''富阳-获取富阳地区医疗机构信息'''
        r = self.obj.post1(row=51, data=DTtime1(51))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "查询成功")
        print(r.text)
    
    def test_app_get_yspb_001(self):
        '''富阳-医院医生排班信息获取'''
        r = self.obj.post1(row=52, data=DTtime1(52))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "查询成功")
        print(r.text)
    
    def test_app_get_yspb_002(self):
        '''富阳-医院医生排班信息获取'''
        r = self.obj.post1(row=53, data=DTtime1(53))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0006")
        self.assertEqual(r.json()['msg'], "请求参数[ksdm]不能为空")
        print(r.text)
    
    def test_app_get_sign_001(self):
        '''富阳-查询是否签约'''
        r = self.obj.post1(row=54, data=DTtime1(54))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-1")
        self.assertEqual(r.json()['msg'], "卡号,必填非空！")
        print(r.text)
    
    def test_app_get_sign_002(self):
        '''富阳-查询是否签约'''
        r = self.obj.post1(row=55, data=DTtime1(55))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "")
        print(r.text)
    
    def test_app_wsj_queryfile_001(self):
        '''富阳-获取富阳地区患者基本档案信息'''
        r = self.obj.post1(row=56, data=DTtime2(56))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0019")
        self.assertEqual(r.json()['msg'], "api验签失败")
        print(r.text)
        
    def test_app_query_credit_list_001(self):
        '''富阳-信用信息查询-成功'''
        r = self.obj.post1(row=57, data=DTtime1(57))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "成功")
        print(r.text)
        
    def test_app_get_useraccount_001(self):
        '''富阳-用户绑定信息获取-成功'''
        r = self.obj.post1(row=58, data=DTtime1(58))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "Success")
        print(r.text)
        
    def test_app_get_payurl_001(self):
        '''富阳-获取支付短地址-成功'''
        r = self.obj.post1(row=59, data=DTtime1(59))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-1")
        self.assertEqual(r.json()['msg'], "没有找到该区域就诊索引对应信息")
        print(r.text)
    
    def test_app_get_payurl_002(self):
        '''富阳-获取支付短地址-宏森看参数中日期格式'''
        r = self.obj.post1(row=60, data=DTtime1(60))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-1")
        self.assertEqual(r.json()['msg'], "没有找到该区域就诊索引对应信息")
        print(r.text)
    
    #61获取已签约的卡号信息-参数获取不到，不做自动化处理
    
    def test_app_get_empi_001(self):
        '''富阳-获取EMPI编号-sign为空'''
        r = self.obj.post1(row=62, data=DTtime2(62))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0019")
        self.assertEqual(r.json()['msg'], "sign为空")
        print(r.text)
    
    #63处方发药确认窗口-参数获取不全，不做处理

    def test_app_get_querycost_001(self):
        '''富阳-费用查询接口-sign为空-成功'''
        r = self.obj.post1(row=64, data=DTtime1(64))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "成功")
        print(r.text)
    
    def test_app_thcl_001(self):
        '''富阳-费用查询接口-成功'''
        r = self.obj.post1(row=64,data=DTtime1(64))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"成功")
        print(r.text)
    
    #65医院分时段号源信息获取-参数不全不做处理
    
    def test_app_ghcl_001(self):
        '''富阳-挂号处理'''
        r = self.obj.post1(row=66,data=DTtime2(66))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"-1")
        self.assertEqual(r.json()['msg'],"挂号时间已过就诊时间，无法挂号")
        print(r.text)
        
    def test_app_smkdata_update_001(self):
        '''富阳-更新富阳市民卡信息接口-api验签失败'''
        r = self.obj.post1(row=67,data=DTtime2(67))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0019")
        self.assertEqual(r.json()['msg'],"api验签失败")
        print(r.text)
        
    def test_app_thcl_001(self):
        '''富阳-退号-已退号 '''
        r = self.obj.post1(row=68,data=DTtime1(68))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"-1")
        self.assertEqual(r.json()['msg'],"已退号！")
        print(r.text)
        
    def test_app_wsj_queryMessage_001(self):
        '''富阳-查询医生留言-获取数据返回失败'''
        r = self.obj.post1(row=69,data=DTtime1(69))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"-1")
        self.assertEqual(r.json()['msg'],"获取数据返回失败！")
        print(r.text)
        
    def test_app_get_jhxxByJzxh_001(self):
        '''富阳-根据挂号序号获取叫号信息-获取数据返回失败'''
        r = self.obj.post1(row=70,data=DTtime1(70))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"-1")
        self.assertEqual(r.json()['msg'],"获取数据返回失败！")
        print(r.text)
        
    def test_app_get_ysxx_001(self):
        '''富阳-根获取富阳地区医疗机构内部医生信息-成功'''
        r = self.obj.post1(row=71,data=DTtime1(71))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"操作成功！")
        print(r.text)
        
    def test_app_get_jzjl_001(self):
        '''富阳-病例概况查询-api验签失败'''
        r = self.obj.post1(row=72,data=DTtime2(72))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"2008")
        self.assertEqual(r.json()['msg'],"验证码错误或失效")
        print(r.text)
        
    def test_app_wsj_queryifyjz_001(self):
        '''富阳-根据挂号序号查询是否已就诊-操作成功-jzbz为0 未就诊'''
        r = self.obj.post1(row=73,data=DTtime2(73))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"操作成功！")
        self.assertEqual(r.json()['data']['interface']['jzbz'],0)
        print(r.text)
        
    
    def test_app_get_jhxx_001(self):
        '''富阳-根据身份证号获取用户当天有效排队叫号信息列表'''
        r = self.obj.post1(row=74,data=DTtime2(74))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"-1")
        self.assertEqual(r.json()['msg'],"该病人在查询时间段没有排队叫号！")
        print(r.text)
    
    def test_app_get_ghxx_001(self):
        '''富阳-根据身份证号获取某个病人挂号信息列表-操作成功 '''
        r = self.obj.post1(row=75,data=DTtime2(75))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"操作成功！")
        print(r.text)
    
    def test_app_get_yljg_001(self):
        '''富阳-获取富阳地区医疗机构信息-查询成功 '''
        r = self.obj.post1(row=76,data=DTtime2(76))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"查询成功")
        print(r.text)
        
    def test_app_get_user_001(self):
        '''富阳-根据手机号码获取身份证号-Success '''
        r = self.obj.post1(row=77,data=DTtime2(77))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"Success")
        print(r.text)
        
    def test_app_bind_relationship_001(self):
        '''富阳-解绑常用就诊人-成功 '''
        r = self.obj.post1(row=78,data=DTtime2(78))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"Success")
        print(r.text)
        
    def test_app_bind_relationship_002(self):
        '''富阳-绑定常用就诊人-成功 '''
        r = self.obj.post1(row=79,data=DTtime2(79))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"Success")
        print(r.text)
        
    # def test_app_synchronization_user_001(self):
    #     '''富阳-用户注册同步-成功 '''
    #     r = self.obj.post1(row=80,data=DTtime2(80))
    #     self.assertEqual(r.status_code,200)
    #     self.assertEqual(r.json()['code'],"0")
    #     self.assertEqual(r.json()['msg'],"Success")
    #     print(r.text)
        
        
        
        
        
        
    
if __name__ == '__main__':
    unittest.main(verbosity=2)