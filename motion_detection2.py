# motion detection using MOG2 algorithm

import cv2
import numpy as np

capture = cv2.VideoCapture("/home/satish/Desktop/SAS/cctv_main_door.mp4")

fgbg = cv2.createBackgroundSubtractorMOG2(300,30,True )  # history, threshold, detectshadows

framecount = 0

while 1:
	ret , frame = capture.read()
	
	if not ret :
		break
	
	framecount += 1
	
	resizedFrame = cv2.resize(frame, (0,0), fx = 0.50, fy = 0.50)
	
	fgmask = fgbg.apply(resizedFrame)

	count = np.count_nonzero(fgmask)
		
	#print('Frame : %d, Pixel Count : %d ' % (framecount, count))
	
	if(framecount > 1 and count >500):
		#print('motion detected')
		cv2.putText(resizedFrame, 'Motion detected',(10,50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255) ,2, cv2.LINE_AA)
	
	cv2.imshow('Frame',resizedFrame)
	cv2.imshow('Mask',fgmask)

	if cv2.waitKey(25) & 0xFF == ord('q') :
			break

capture.release()
cv2.destroyAllWindows()
