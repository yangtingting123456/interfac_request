import requests
from itsDemoTest.comm.ReadConfig import config
from itsDemoTest.comm.md5_password import psd
import unittest

class Login_info(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_Login(self):
        post_params = {
            "name": "admin",
            "password": "0659c7992e268962384eb17fafe88364"
        }
        header_param = {
            "Content-Type": "application/json"
        }

        response = requests.post(url='http://dev.its.juneyaokc.com:8081/user/login',
                                 json=post_params,
                                 headers=header_param
                                 )
        body = response.json()
        code = body['code']
        user_token=body['data']['token']
        self.assertEqual(code,200,'登录失败')
        return user_token

if __name__ == '__main__':
    unittest.main(verbosity=2)











