import cv2
import time


log_path = '/home/dean/projects/git-tutorial/camera/'

def mkdir(path):
	import os
	
		
	is_exist = os.path.exists(path)
	
	if not is_exist:
		os.makedirs(path)
		return True
	else:
		print('path exists\n')
		return False

#The function will take a picture to the log_path

def take_pic():
	cap = cv2.VideoCapture(0)
	# get a frame
	ret, frame = cap.read()
	# show a frame
	# cv2.imshow("capture", frame)
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	cv2.imwrite(log_path + "pic.jpg", frame)
		
	cap.release()
	# cv2.destroyAllWindows()

def take_pic_t():
	cap = cv2.VideoCapture(0)
	ret, frame = cap.read()
	
	t1 = (time.strftime('%Y%m%d',time.localtime(time.time())))
	t2 = (time.strftime('%H%M%S',time.localtime(time.time())))
	# print(t1)
	# print(t2)
	
	log_path_f = log_path + 'pic/' + t1
	mkdir(log_path_f)
	log_path_re = log_path_f +'/' + t2 + '.jpg'
	# print(log_path_re)
	cv2.imwrite(log_path_re, frame)	
	cap.release()

	
		
##########################################################################
	
if __name__ == '__main__':
	take_pic()
	
		
