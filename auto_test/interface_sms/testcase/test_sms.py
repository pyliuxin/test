#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:


import unittest
from page.Dy_para import *
from Methodfengzhuang.method import *



class SMS(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        pass
    
    def test_sendmsg_0(self):
        '''发送短信：短信验证码：短信发送成功'''
        r=self.obj.post1(row=1,data=DTtime(1))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],"0")
        self.assertEqual(r.json()['msg'],"发送成功")
        print(DTtime(1))
        print(r.text)
    def test_pullmsg_001(self):
        '''拉取上行：验签失败'''
        r = self.obj.post1(row=2,data = DTcount(2))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "1025")
        self.assertEqual(r.json()['msg'], "验签失败")
        print(DTtime(2))
        print(r.text)
        pass
    def test_semdMsg_0003(self):
        '''appkey参数为空'''
        r = self.obj.post(3)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0003")
        self.assertEqual(r.json()['msg'], "appKey为空")
        print(r.text)

    def test_sendmsg_1019(self):
        """未传signid"""
        r = self.obj.post1(row=4,data = DTtime(4))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "1019")
        self.assertEqual(r.json()['msg'], "签名id必传")
        print(r.text)
        pass

    def test_sendmsg_1001(self):
        """输入signId签名参数不存在"""
        r = self.obj.post1(row=5,data=DTtime(5))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "1001")
        self.assertEqual(r.json()['msg'], "签名不存在")
        print(r.text)
        pass

    def test_sendmsg_1004(self):
        """输入temdId模板参数不存在"""
        r = self.obj.post1(row=6,data=DTtime(6))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "1004")
        self.assertEqual(r.json()['msg'], "模板不存在")
        print(r.text)
        pass

    def test_pullmsg_002(self):
        """pullmsg操作成功"""
        r = self.obj.post1(row=7,data=DTcount(7))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)

    def test_sendmsg_1006(self):
        """params参数为空"""
        r = self.obj.post1(row=8,data=DTtime(8))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "1006")
        self.assertEqual(r.json()['msg'], "短信验签失败")
        print(r.text)

    def test_sendmsg_tempid_None(self):
        """没有tempId参数"""
        r = self.obj.post1(row=9,data=DTtime(9))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-1")
        self.assertEqual(r.json()['msg'], "tempId必传")
        print(r.text)

    def test_sendmsg_params_None(self):
        """没有params参数"""
        r = self.obj.post1(row=10,data=DTtime(10))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-1")
        self.assertEqual(r.json()['msg'], "params必传")
        print(r.text)


    def test_sendmsg_signKey(self):
        """参数signKey输入有误"""
        r = self.obj.post1(row=11,data=DTtime(11))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0004")
        self.assertEqual(r.json()['msg'], "获取用户信息失败")
        print(r.text)

    def test_addTemp_001(self):
        """添加模板-添加成功"""
        r = self.obj.post1(row=12,data=DTtime1(12))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        getids = r.json()['data']
        print(getids)
        return getids
        
        
     
    def test_addTemp_002(self):
        """添加模板-appKey错误"""
        r = self.obj.post1(row=13,data=DTtime1(13))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0004")
        self.assertEqual(r.json()['msg'], "获取用户信息失败")
        print(r.text)


    def test_deleteTemp_001(self):
        """删除模板-短信验证码"""
        r = self.obj.post1(row=14,data={"time":p1,"sign":TY1,"ids":self.test_addTemp_001(),"signKey":"4nUiMQkjlp9","appKey":"b81ff6ac33844cd693445ef92b565c39"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)

    def test_deleteTemp_002(self):
        """appkey为空"""
        r = self.obj.post1(row=15,data=DTtime1(15))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0004")
        self.assertEqual(r.json()['msg'], "获取用户信息失败")
        print(r.text)

    def test_deleteTemp_003(self):
        """删除模板-没有要删除的模板-data=0"""
        r = self.obj.post1(row=16,data=DTtime1(16))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        self.assertEqual(r.json()['data'],0)
        print(r.text)

    def test_selectTemp_001(self):
        """选择模板成功"""
        r = self.obj.post1(row=17,data=DTtime1(17))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)

    def test_selectTemp_002(self):
        """appkey为空"""
        r = self.obj.post1(row=18,data=DTtime1(18))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0004")
        self.assertEqual(r.json()['msg'], "获取用户信息失败")
        print(r.text)

    def test_deletesign_001(self):
        """删除签名id成功"""
        r = self.obj.post1(row=19,data=DTtime1(19))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)

    def test_selectsign_001(self):
        """selectsign成功 status为0"""
        r = self.obj.post1(row=20,data=DTtime1(20))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)

    def test_selectsign_002(self):
        """selectsign审核中status为1"""
        r = self.obj.post1(row=21,data=DTtime1(21))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        """此处添加data返回值得审核状态"""
        print(r.text)

    def test_selectsign_003(self):
        """selectsign:签名模板为空，status为0"""
        r = self.obj.post1(row=22,data=DTtime1(22))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "1")
        self.assertEqual(r.json()['msg'], "数据为空")
        """此处添加data返回值得审核状态"""
        print(r.text)

    def test_detail_001(self):
        """短信发送详情"""
        r = self.obj.post1(row=23,data=DTtime1(23))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        """此处添加data返回值得审核状态"""
        print(r.text)

    def test_detail_002(self):
        """短信发送详情"""
        r = self.obj.post1(row=24,data=DTtime1(24))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0004")
        self.assertEqual(r.json()['msg'], "获取用户信息失败")
        """此处添加data返回值得审核状态"""
        print(r.text)

    def test_addTemp_003(self):
        """添加模板成功"""
        r = self.obj.post1(row=25,data=DTtime1(25))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)

    def test_addTemp_004(self):
        """模板参数为空"""
        r = self.obj.post1(row=26,data=DTtime3(26))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-1")
        self.assertEqual(r.json()['msg'], "模板参数必传")
        """此处添加data返回值得审核状态"""
        print(r.text)

    def test_addsign_001(self):
        """添加签名：appkey为空--获取用户信息失败"""
        r = self.obj.post1(row=27,data=DTtime1(27))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0004")
        self.assertEqual(r.json()['msg'], "获取用户信息失败")
        """此处添加data返回值得审核状态"""
        print(r.text)

    def test_addsign_002(self):
        """添加签名：无appkey参数--appkey为空"""
        r = self.obj.post1(row=28,data=DTtime1(28))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0003")
        self.assertEqual(r.json()['msg'], "appKey为空")
        """此处添加data返回值得审核状态"""
        print(r.text)

    def test_deletesign_001(self):
        """删除签名：参数ids为空--请输入签名id"""
        r = self.obj.post1(row=29,data=DTtime1(29))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-1")
        self.assertEqual(r.json()['msg'], "请传入签名id")
        """此处添加data返回值得审核状态"""
        print(r.text)

    def test_deletesign_002(self):
        """删除签名：没有要删除的签名ids，任意填写一个ids删除--操作成功"""
        r = self.obj.post1(row=30,data=DTtime1(30))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        self.assertEqual(r.json()['data'],0)
        print(r.text)

    def test_deletesign_003(self):
        """appkey为空-获取用户信息失败"""
        r = self.obj.post1(row=31,data=DTtime1(31))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0004")
        self.assertEqual(r.json()['msg'], "获取用户信息失败")
        print(r.text)

    def test_sentStats_001(self):
        """sentstats按时间查找成功"""
        r = self.obj.post1(row=32,data=DTtime1(32))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)

    def test_sentStats_002(self):
        """tempid"""
        r = self.obj.post1(row=33,data=DTtime1(33))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "1")
        self.assertEqual(r.json()['msg'], "数据为空")
        print(r.text)

    def test_billStats_001(self):
        """billstatus 操作成功"""
        r = self.obj.post1(row=34, data=DTtime1(34))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)

    def test_getchildkey_001(self):
        """获取子账号appkey"""
        r = self.obj.post1(row=35, data=DTtime1(35))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "1")
        self.assertEqual(r.json()['msg'], "数据为空")
        print(r.text)

    def test_demotd_001(self):
        """退订"""
        r = self.obj.post1(row=36, data=DTtime1(36))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-3")
        self.assertEqual(r.json()['msg'], "数据已存在")
        print(r.text)

    def test_demotd_002(self):
        """退订：已退订模板进行退订"""
        r = self.obj.post1(row=37, data=DTtime1(37))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)

    def test_demotd_003(self):
        """退订：参数temp..id为空"""
        r = self.obj.post1(row=38, data=DTtime1(38))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-2")
        self.assertEqual(r.json()['msg'], "参数有误")
        print(r.text)

    def test_selecttd_001(self):
        """退订-数据为空"""
        r = self.obj.post1(row=39, data=DTtime1(39))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "1")
        self.assertEqual(r.json()['msg'], "数据为空")
        print(r.text)

    def test_delecttd_001(self):
        """解除退订成功"""
        r = self.obj.post1(row=40, data=DTtime1(40))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)

    def test_deletetd_002(self):
        """退订"""
        r = self.obj.post1(row=41, data=DTtime1(41))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)

    def test_addTemp_003(self):
        """新增模板"""
        r = self.obj.post1(row=42, data=DTtime1(42))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0")
        self.assertEqual(r.json()['msg'], "操作成功")
        print(r.text)
        
        
    def test_demotd_004(self):
        """退订：参数phone为空"""
        r = self.obj.post1(row=43, data=DTtime1(43))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "-2")
        self.assertEqual(r.json()['msg'], "参数有误")
        print(r.text)
        
    def test_selectsign_004(self):
        """selectsign成功 status为1"""
        r = self.obj.post1(row=44,data=DTtime1(44))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "1")
        self.assertEqual(r.json()['msg'], "数据为空")
        print(r.text)
        
    def test_selectsign_005(self):
        """appkey为空 status为0"""
        r = self.obj.post1(row=45,data=DTtime1(45))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0003")
        self.assertEqual(r.json()['msg'], "appKey为空")
        print(r.text)

    def test_billStats_001(self):
        """appkey错误"""
        r = self.obj.post1(row=46, data=DTtime1(46))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], "0004")
        self.assertEqual(r.json()['msg'], "获取用户信息失败")
        print(r.text)
        

        
    
        

        
    


if __name__ == '__main__':
    unittest.main(verbosity=2)