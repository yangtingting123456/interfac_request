import configparser
import os

config_file_path = os.path.join(os.path.dirname(__file__),'..','config','config.ini' )
print(config_file_path)

class ConfigUtils:
    def __init__(self,conf_path = config_file_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read( config_file_path )

    @property   # 类中的一个方法加property这个装饰器 属性方法
    def getHOSTS(self):
        hosts_value = self.cfg.get('default','HOSTS')
        return hosts_value

    @property  # 类中的一个方法加property这个装饰器 属性方法
    def getPORT(self):
        port_value = self.cfg.get('default', 'PORT')
        return port_value

config = ConfigUtils()

print('http://%s:%s/user/login'%(config.getHOSTS,config.getPORT))



