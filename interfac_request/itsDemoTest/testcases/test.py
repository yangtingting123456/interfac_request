from itsDemoTest.comm.ReadConfig import config
import unittest
import requests
from itsDemoTest.comm.md5_password import psd
import jsonpath

# 登录接口，获取用户登录的token


class Login_info(unittest.TestCase):
    def get_token(self):
        post_params = {
            "name": "admin",
            "password":psd.get_md5_password()
        }
        header_param = {
            "Content-Type": "application/json"
        }

        response = requests.post(url='http://%s:8081/user/login' % config.getHOSTS,
                                 json=post_params,
                                 headers=header_param
                                 )
        # 将登录接口返回的数据转换成json

        return response.content

user_token = Login_info()
print(user_token.get_token())











