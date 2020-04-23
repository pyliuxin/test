#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:

import os
import json
import base64

temp1 = [{"content":"您好，您的验证+码是{5}","tempName":"模板1号","type":1,"isTd":1}]

temp2 = [{"content":"你好，请来{20}楼寻#找{20}大夫","tempName":"模板2号","type":2,"isTd":0}]


temp = json.dumps(temp1 +temp2)
#print(temp)

picdir = 'D:\picture'
'''列出文件夹下所有的文件'''
lst = os.listdir(picdir)
# print(lst)

with open('D:\picture/0001.jpg', 'rb') as img:
    img_data1 = base64.b64encode(img.read()).decode()
    img.close()

with open('D:\picture/0002.jpg', 'rb') as img:
    img_data2 = base64.b64encode(img.read()).decode()
    img.close()

with open('D:\picture/0003.jpg', 'rb') as img:
    img_data3 = base64.b64encode(img.read()).decode()
    img.close()

with open('D:\picture/0004.jpg', 'rb') as img:
    img_data4 = base64.b64encode(img.read()).decode()
    img.close()

def json_str():
    imgs = []
    imgs.append([img_data1, img_data2, img_data3, img_data4])
    #print(imgs)
    json_Str1 = json.dumps(imgs)
    return json_Str1

#print(json_str())

