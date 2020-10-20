#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_02.py
# @time: 2020/10/18 9:55 上午

import logging

logger = logging.getLogger('test_p3p4')
logger.setLevel(logging.DEBUG) #设置日志默认

con_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(message)s')

sh = logging.StreamHandler() #创建控制台输出对象
sh.setFormatter( con_formatter )
sh.setLevel( logging.DEBUG )

fh = logging.FileHandler('test.log','a',encoding='utf-8')
fh.setFormatter( file_formatter )
fh.setLevel( logging.DEBUG )

logger.addHandler( sh )
logger.addHandler( fh )

logger.info('hello')

# 设置日志格式、等级 == setFormatter setLevel 》 设置Handler对象  == addHandler 》加载到logger对象

