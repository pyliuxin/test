#!/usr/bin/python
# -*- coding:utf-8 -*-
#Auther:liuxin
#Date:
import unittest
import json
from page.Dy_para import *
from utils.accesstoke import *


class SDK_ERTONG(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        pass
    
    def test_001(self):
        r = self.obj.post1(row=1, data=DTtime())
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)