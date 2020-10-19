import requests
from its_demo.comm.url_info import urlinfo
from its_demo.api.login import Login_info
from its_demo.api.user_list import User_list
from its_demo.comm.md5_password import get_md5_password

u_ids = User_list()
u_id= u_ids.get_user_id()
usertoken=Login_info()
md5_password = get_md5_password()
 # 修改密码
post_params = {
    "id": 8,
    "email": "1m1in.yao@juneyaokc.com",
    "realName": "aaa",
    "mobile": "11345678922",
    "wechat": "aaaa",
    "companyId": 2,
    "departmentId": 3,
    "jobTypeId": "11",
    "jobId": "1",
    "status": "1",
    "jobNumber": "1daaa",
    "address": "a2aaa"
}

header_param = {
     "Content-Type": "application/json",
      "token": usertoken.get_token()
        }

response = requests.post(url='%s/user/update' % urlinfo.url_hostname_info(),
                         json=post_params,
                          headers=header_param
                                 )
print(response.text)
