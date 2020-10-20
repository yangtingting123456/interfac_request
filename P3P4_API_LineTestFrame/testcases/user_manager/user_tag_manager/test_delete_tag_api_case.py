#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_create_tag_api_case.py
# @time: 2020/10/14 9:23 下午

import requests
import unittest
from common.config_utils import config
from common import api_info

class TestDeletetagApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
    def tearDown(self) -> None:
        self.session.close()

    def test_delete_tag(self):
        self._testMethodName = 'case05'
        self._testMethodDoc = '验证delete_tag接口能否成功调用'
        response = api_info.get_access_token_api(self.session,
                                                 self.HOSTS,
                                                 'wx55614004f367f8ca',
                                                 '65515b46dd758dfdb09420bb7db2c67f')
        token_id = response.json()['access_token']

        post_data = {   "tag":{   "id" : 414   } }
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=%s'%token_id,
                                     json=post_data)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,0,'case05 验证delete_tag接口能否成功调用')

if __name__=='__main__':
    unittest.main(verbosity=2)