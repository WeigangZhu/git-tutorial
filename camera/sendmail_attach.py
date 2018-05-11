#!/usr/bin/python
# -*- coding: UTF-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import traceback

def send_email():
	# thirs parties service
	mail_host = "smtp.qq.com"  # set service
	mail_user = "2216859338@qq.com"  
	mail_pass = "oqzjvolpxudrdjge"


	sender = "2216859338@qq.com"
	receivers = ['809684907@qq.com']

	message = MIMEMultipart()

	message['From'] = Header("Dean", 'utf-8')
	message['To'] = Header('ZWG', 'utf-8')
	subject = 'Someone actives your computer!'
	message['Subject'] = Header(subject, 'utf-8')

	# email plain
	message.attach(MIMEText('See the attach ...', 'plain', 'utf-8'))

	# construct a attach file
	att1 = MIMEApplication(open('pic.jpg', 'rb').read())
	att1.add_header('Content-Disposition', 'attachment', filename = 'pic.jpg')
	message.attach(att1)


	# construct another attach file
	att2 = MIMEApplication(open('file.log', 'rb').read())
	att2.add_header('Content-Disposition', 'attachment', filename = 'file.log')
	message.attach(att2)

	try:
		smtpObj = smtplib.SMTP_SSL()
		# smtpObj.set_debuglevel(1)
		smtpObj.connect(mail_host, 465)  # 465 is the port of SMTP
		smtpObj.login(mail_user, mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		print("send email success")
		smtpObj.quit()
	except:
		print("send email error")
		# print(traceback.format_exc())
		
if __name__ == '__main__':
	send_email()
