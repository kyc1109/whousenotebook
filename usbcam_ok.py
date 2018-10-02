#python3
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#add test.py

'''
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
'''
def myCV_video_bk():
	import cv2
	import time
	import numpy as np
	# 1為選擇第二隻攝影機
	cap = cv2.VideoCapture(0)
	#fourcc = cv2.VideoWriter_fourcc(*'XVID')
	#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

	#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
	img = cv2.imread('download.jpg')
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#cv2.COLOR_BGR2GRAY
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
	    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = frame[y:y+h, x:x+w]
	    eyes = eye_cascade.detectMultiScale(roi_gray)
	    for (ex,ey,ew,eh) in eyes:
	        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	#cv2.imshow('img',img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	cv2.imshow('frame', frame)
	time.sleep(5)


	"""
	while(True):
		# 從攝影機擷取一張影像
		ret, frame = cap.read()
		frame=cv2.flip(frame,1) #1	水平翻转,0	垂直翻转,-1	水平垂直翻转

		# 顯示圖片
		cv2.imshow('frame', frame)
		time.sleep(5)
		# 若按下 q 鍵則離開迴圈
		if cv2.waitKey(1) & 0xFF == ord('q'):
			cv2.waitKey(0)
			cv2.destroyAllWindows()
			break
	"""
	# 釋放攝影機
	cap.release()
	# 關閉所有 OpenCV 視窗
	cv2.destroyAllWindows()

def myCV_jpg():
	import cv2
	import time
	import numpy as np
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
	img = cv2.imread('download.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cv2.COLOR_BGR2GRAY
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	    eyes = eye_cascade.detectMultiScale(roi_gray)
	    for (ex,ey,ew,eh) in eyes:
	        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	cv2.imshow('img', img)
	cv2.waitKey(0) #0= press any key, 1000=1s
	cv2.destroyAllWindows()

def getFacePhotoFile(duty_on_time=8,delay_time=600):
	import cv2
	import time
	import numpy as np
	import datetime
	import os
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
	# 1為選擇第二隻攝影機
	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
	dirname = 'img_file'
	if os.path.isdir(dirname):
		print("folder exist")
	else:
		os.mkdir(dirname)
	#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection
	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#cv2.COLOR_BGR2GRAY
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]
			#cv2.imwrite(".\\img_file\\img_"+str(datetime.datetime.now().strftime("%Y-%m-%d_%Hh_%Mm_%Ss"))+".jpg",frame) #file name do not support ":"
			filename=".\\img_file\\img_"+str(datetime.datetime.now().strftime("%Y-%m-%d_%Hh_%Mm"))+".jpg" #write jpg by every 1 min if find face.
			
			try:
				if cv2.imwrite(filename,frame):	#write a jpg file.
					sendPhoto(filename)
					time.sleep(delay_time) #delay_time:600
			except FileExistsError:
				print("File exist")

			print(".\\img_file\\img_"+str(datetime.datetime.now().strftime("%Y-%m-%d_%Hh_%Mm_%Ss"))+".jpg")
			eyes = eye_cascade.detectMultiScale(roi_gray)
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
				#roi_gray = gray[ey:ey+eh, ex:ex+ew] 
				#roi_color = frame[ey:ey+eh, ex:ex+ew]
		#cv2.imshow('img',img)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
#		cv2.imshow('frame', frame) #show video
		#time.sleep(5)
		#cv2.waitKey(0)
		if int(datetime.datetime.now().strftime("%H"))==duty_on_time: #break, if o'clock == duty on time 
			print("Duty on")
			break
		if cv2.waitKey(1) & 0xFF == ord('q'):
			cv2.waitKey(0)
			cv2.destroyAllWindows()
			break
	cap.release()
	cv2.destroyAllWindows()
def my_duty_off_time(duty_off_time=17,duty_on_time=8,delay_time=600):
	import datetime
	#print(str(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")))

	getHours=int(datetime.datetime.now().strftime("%H"))
	print("getHours:",getHours,"duty_off_time:",duty_off_time)
	if getHours>duty_off_time:
			getFacePhotoFile(duty_on_time,delay_time) # 1.duty_on_time >24 is always ON, 2.Delay_time:600
	else:
		print("Duty off")
		
def sendPhoto(img_file="download.jpg"):
	import telepot
	import datetime
	try:
		telegram_bot_photo(img_file)
	except:
		print(str(datetime.datetime.now().strftime("%Y-%m-%d_%Hh_%Mm_%Ss"))+" Upload jpg fail.")

def cleanJPGfile(dirname='img_file'):
	import os
	if os.path.isdir(dirname):
		os.system("cls")
		os.system("del .\\img_file\\img*.jpg")
		print("folder exist, del previous jpg file")

def telegram_bot_photo(img="KONAMI.JPG"):
    import telepot
    bot = telepot.Bot("you telegram token")
    bot.sendPhoto("you telegram ID",open(img,"rb"))

if __name__ == "__main__":
	#myCV_jpg() #ok
#	getFacePhotoFile() #ok
	cleanJPGfile('img_file')
	my_duty_off_time(17,8,600) #1.duty_OFF_time:17 2.duty_ON_timeok:8, >24 is always ON 3. delay_time:600s
#	sendPhoto()

