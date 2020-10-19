import requests
from itsDemoTest.comm.ReadConfig import config
from itsDemoTest.comm.md5_password import psd

class ApiUtils:
    #用户登录api
    def Login_Api_Info(self,session,hosts,port,name,password):
        post_params = {"name":name,"password":password}
        header_param = {"Content-Type": "application/json"}
        response = session.post(url='http://%s:%s/user/login'%(hosts,port),json=post_params,headers=header_param )
        return response

    #用户登出api
    def user_logout_api(self,session,hosts,port,token):
        header_param = {"token": token,"Content-Type": "application/json"}
        response = session.post(url='http://%s:%s/user/logout' % (hosts, port), headers=header_param)
        return response

    # 获取用户列表api
    def User_list_api(self,session,host,port,token,pageNum,pageSize):
        get_params = {"pageNum": pageNum, "pageSize": pageSize}
        header_param = {"token": token}
        response = session.post(url='http://%s:%s/user/list' % (host, port),data=get_params,headers=header_param )
        return response

    # 获取更新用户信息api
    def update_userinfo_api(self, session, host, port, token):
        post_params = {"id": "1", "name": "admin", "mobile": "15173661874", "wechat": "aaaa",
                       "email": "tingting.yang@juneyaokc.com", "status": "1", "jobNumber": "12as323",
                       "address": "a2aaa", "jobTypeId": "2", "jobId": "1", "realName": "aaaAAA",
                       "companyId": "1", "departmentId": "1", "company": "上海均瑶集团有限公司", "department": "市场部",
                       "jobType": "sxx", "job": "aaasa"}
        header_param = {"Content-Type": "application/json","token":token}
        response = session.post(url='http://%s:%s/user/logout' % (host, port),json=post_params,headers=header_param)
        return response

    # 获取用户列表api
    def User_Message_list_api(self, session, host, port, token, pageNum, pageSize):
        get_params = {"pageNum": pageNum, "pageSize": pageSize}
        header_param = {"token": token}
        response = session.post(url='http://%s:%s/user/message-list' % (host, port), data=get_params, headers=header_param)
        return response

API_Info = ApiUtils()
Response = API_Info.Login_Api_Info(requests.session(),
    config.GET_HOSTS,config.GET_PORT,config.GET_UserName,psd.get_md5_password()                             )
res = Response.json()
token = res['data']['token']
# print(token)
# logout_response=API_Info.user_logout_api(requests.session(),config.GET_HOSTS,config.GET_PORT,
#                                         'eyJpZCI6IjEiLCJuYW1lIjoiYWRtaW4iLCJwYXNzd29yZCI6IjA2NTljNzk5MmUyNjg5NjIzODRlYjE3ZmFmZTg4MzY0IiwidW5pcWlkIjoiNWY4ZDQ1YjllNTdmZiJ9')
# print(logout_response.text)
# ses=API_Info.User_list_api(requests.session(),
#                              config.GET_HOSTS,config.GET_PORT,token,config.GET_PageNum,config.GET_PageSize).json()
# print(ses['data']['list'][0]['id'])

# ses=API_Info.update_userinfo_api(requests.session(),
#                              config.GET_HOSTS,config.GET_PORT,token).content.decode('utf-8')
# print(ses)
# ses=API_Info.User_Message_list_api(requests.session(),
#                              config.GET_HOSTS,config.GET_PORT,token,
#                                    config.GET_PageNum,config.GET_PageSize).content.decode('utf-8')
# print(ses)
