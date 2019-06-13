import cv2

face_cascade = cv2.CascadeClassifier('/home/satish/opencv/data/haarcascades_cuda/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/satish/opencv/data/haarcascades_cuda/haarcascade_eye.xml')

cap = cv2.VideoCapture('face_test.mp4')

while 1:
	ret, img = cap.read()

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(gray, 1.05, 5, 30) 
	
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h,x:x+w]

		#eyes = eye_cascade.detectMultiScale(roi_gray)
		#for (ex, ey, ew, eh ) in eyes:
			#cv2.rectangle (roi_color,(ex,ey), (ex+ew,ey+eh), (0,127,255),2)
	cv2.imshow('face detection',img)

	if cv2.waitKey(25) & 0xFF == ord('q') :
		break

cap.release()
cv2.destroyAllWindows()
