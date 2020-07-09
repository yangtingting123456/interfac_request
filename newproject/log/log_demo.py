#日志模块
import os
import logging

current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path, '../log/testpython.log')

#创建一个log对象
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)  #设置全局日志等级debug，info，error,,,,,

#一，控制台打印
console = logging.StreamHandler()  #创建一个控制台输入对象
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
console.setLevel(level=logging.DEBUG)
logger.addHandler(console)

#二，写入到文件中
file_log = logging.FileHandler(log_path)  #闯将一个文件日志对象
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  #设置格式
file_log.setFormatter(formatter)
logger.addHandler(file_log)  #将日志写入文件中

logger.info('Hello word')
logger.info('I hava a 梦想')




