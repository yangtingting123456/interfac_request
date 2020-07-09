#读取配置文件类
import configparser
import os

#获取ini文件路径
current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path,'../conf/config.ini')

class ConfigUtils:
    #对ini的路径和对象进行处理
    def __init__(self,config_path=cfgpath):
        self.config_path=config_path
        self.conf = configparser.ConfigParser()  #创建一个cfg对象
        self.conf.read(self.config_path,encoding='utf-8')  #读取整个ini文件

    #  读取ini文件的内容
    @property
    def read_ini(self):
        return self.conf.get('default','excel_path')
    @property
    def read_email(self):
        return self.conf.get('email','username')

conf_test = ConfigUtils()

if __name__ == '__main__':
    conf_test = ConfigUtils()
    expath= conf_test.read_ini
    email=conf_test.read_email
    print(email)
    print(expath)