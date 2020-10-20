#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_get_access_token_api_case.py
# @time: 2020/10/11 5:19 下午

import requests
import unittest
from nb_log import LogManager
from common.config_utils import config
from common.log_utils import logger
from common import api_info

class TestGetaccesstokenApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
        self.logger = LogManager('ApiCase').get_logger_and_add_handlers()
    def tearDown(self) -> None:
        self.session.close()

    def test_get_accesstoken_success(self):
        self._testMethodName = 'case01'
        self._testMethodDoc = '验证get_access_token接口能否成功调用'
        logger.info('case01 验证get_access_token接口能否成功调用 --开始执行--')
        self.logger.info('case01 验证get_access_token接口能否成功调用 --开始执行--')
        response = api_info.get_access_token_api(self.session,self.HOSTS,'wx55614004f367f8ca','65515b46dd758dfdb09420bb7db2c67f')
        actual_result = response.status_code
        logger.info('case01 验证get_access_token接口能否成功调用 --执行结束--')
        self.logger.info('case01 验证get_access_token接口能否成功调用 --执行结束--')
        self.assertEqual(actual_result,200,'case01 验证get_access_token接口能否成功调用')

    def test_get_accesstoken_error_appid(self):
        self._testMethodName = 'case02'
        self._testMethodDoc = '验证appid错误时，get_access_token接口能否正常处理'
        response = api_info.get_access_token_api(self.session,
                                                    self.HOSTS,
                                                    'wx55614004f367f8',
                                                    '65515b46dd758dfdb09420bb7db2c67f')
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,40013,'case02 验证appid错误时，get_access_token接口能否正常处理')

    def test_get_accesstoken_error_appsecret(self):
        self._testMethodName = 'case03'
        self._testMethodDoc = '验证appsecret错误时，get_access_token接口能否正常处理'
        get_param_dict = {
            "grant_type": "client_credential",
            "appid": "wx55614004f367f8ca",
            "secret": "65515b46dd758dfdb09420bb7db2c6"
        }
        response = self.session.get(url='https://%s/cgi-bin/token'%self.HOSTS,
                                    params=get_param_dict)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result, 40001, 'case03 验证appsecret错误时，get_access_token接口能否正常处理')

if __name__=='__main__':
    unittest.main(verbosity=2)