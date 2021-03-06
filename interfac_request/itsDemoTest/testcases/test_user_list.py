import requests
from itsDemoTest.comm.ReadConfig import config
from itsDemoTest.comm.md5_password import psd
import unittest
from itsDemoTest.comm.apiutils import API_Info
from itsDemoTest.comm.log_utils import logger

class UserListCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOST = config.GET_HOSTS
        self.PORT = config.GET_PORT
        self.pwd = psd.get_md5_password()
        self.UserName = config.GET_UserName
        self.PageNum = config.GET_PageNum
        self.PageSize = config.GET_PageSize

    def tearDown(self):
        self.session.close()
    #成功获取用户列表
    def test_user_list(self):
        ses_login = API_Info.Login_Api_Info(self.session,self.HOST,self.PORT,self.UserName,self.pwd)
        json_login_data = ses_login.json()
        token = json_login_data['data']['token']
        ses_user_list = API_Info.User_list_api(self.session,self.HOST,self.PORT,token,self.PageNum,self.PageSize)
        json_userlist_data = ses_user_list.json()
        code = json_userlist_data['code']
        self.assertEqual(code,200,'获取用户列表失败')
    # token值错误
    def test_user_list_fail(self):
        ses_login = API_Info.Login_Api_Info(self.session,self.HOST,self.PORT,self.UserName,self.pwd)
        # json_login_data = ses_login.json()
        # token = json_login_data['data']['token']
        ses_user_list = API_Info.User_list_api(self.session,self.HOST,self.PORT,'aldjlf',self.PageNum,self.PageSize)
        json_userlist_data = ses_user_list.json()
        code = json_userlist_data['code']
        self.assertEqual(code,1003,'token值错误，返回code1003')

if __name__ == '__main__':
    unittest.main(verbosity=2)

