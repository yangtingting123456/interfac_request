#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_create_tag_api_case.py
# @time: 2020/10/14 9:23 下午

import requests
import unittest
import json
from common.config_utils import config
from common import api_info

class TestCreatetagApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
    def tearDown(self) -> None:
        self.session.close()

    def test_create_tag(self):
        self._testMethodName = 'case04'
        self._testMethodDoc = '验证create_tag接口能否成功调用'
        token_id = api_info.get_access_token_value(self.session,self.HOSTS)
        post_data = {   "tag" : {     "name" : "梦想P3"   } }
        response = api_info.create_user_tag_api(self.session,self.HOSTS,token_id,post_data)
        actual_result = response.json()['tag']['name']
        self.assertEqual(actual_result,'梦想P3','case04 验证create_tag接口能否成功调用')

if __name__=='__main__':
    unittest.main(verbosity=2)