import cv2



log_path = '/home/dean/projects/git-tutorial/camera/'

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


	
if __name__ == '__main__':
	take_pic()
	
		
