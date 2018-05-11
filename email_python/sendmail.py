#!/usr/bin/python
# -*- coding: UTF-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.header import Header
import traceback

# thirs parties service
mail_host = "smtp.qq.com"  # set service
mail_user = "2216859338@qq.com"  
mail_pass = "oqzjvolpxudrdjge"


sender = "2216859338@qq.com"
receivers = ['809684907@qq.com']

message = MIMEText('Python email test ...', 'plain', 'utf-8')
message['From'] = Header("Dean", 'utf-8')
message['To'] = Header('ZWG', 'utf-8')

subject = 'Python SMTP email test'
message['Subject'] = Header(subject, 'utf-8')

try:
	smtpObj = smtplib.SMTP_SSL()
	# smtpObj.set_debuglevel(1)
	smtpObj.connect(mail_host, 465)  # 587 is the port of SMTP
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print("send email success")
	smtpObj.quit()
except:
	print("send email error")
	# print(traceback.format_exc())
