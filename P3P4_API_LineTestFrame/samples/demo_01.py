#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_01.py
# @time: 2020/10/18 9:49 上午

import logging

logging.basicConfig(level=30,  #logging.DEBUG
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    filename='test.log')
logging.debug('-----调试信息[debug]-----')
logging.info('-----有用的信息[info]-----')
logging.warning('-----警告信息[warning]-----')
logging.error('-----错误信息[error]-----')
logging.critical('-----严重错误信息[critical]-----')
# debug info warning error critical