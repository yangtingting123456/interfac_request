#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_04.py
# @time: 2020/10/18 11:47 上午

from nb_log import LogManager

logger = LogManager('newdream').get_logger_and_add_handlers(40)

logger.debug('P1')
logger.info('P2')
logger.warning('P3')
logger.error('P4')
logger.critical('P5')
print('hello')