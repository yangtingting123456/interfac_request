#日志类
import os
import logging

current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path, '../log/testpython.log')

class logUtil:
    def __init__(self,logfile_path=log_path):
        self.logfile_path=log_path
        self.logger = logging.getLogger('__log_util__')
        self.logger.setLevel(level=logging.INFO)
        file_log = logging.FileHandler(log_path)  # 闯将一个文件日志对象
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)


    def info(self,message):
        self.logger.info(message)

    def error(self,errmessage):
         self.logger.error(errmessage)

log_info=logUtil(log_path)

if __name__ == '__main__':
    log=logUtil(log_path)
    log.error('系统异常')
    log.info('登录成功')
