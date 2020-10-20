#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: email_demo_05.py
# @time: 2020/10/18 2:06 下午

import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com',25)
smtp.login('329999897@qq.com','wvcsgattkyqqbhah')  #邮箱授权码

email_content = 'from newdream test...'
msg = MIMEText(email_content,'html','utf-8')
msg['from'] = '329999897@qq.com'
msg['to'] = '329999897@qq.com'
msg['Cc'] = '294608794@qq.com'
msg['subject'] = '测试邮件'

# smtp.sendmail('329999897@qq.com','329999897@qq.com',msg.as_string()) #发件人、收件人
smtp.sendmail('329999897@qq.com',['329999897@qq.com','294608794@qq.com'],msg.as_string()) #发件人、收件人

smtp.close()