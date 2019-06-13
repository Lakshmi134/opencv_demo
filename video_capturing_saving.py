import cv2
from datetime import datetime

def rescale(frame, percent = 78):
	width = int(frame.shape[1] * percent/100)
	height = int(frame.shape[0] * percent/100)
	dim = (width,height)
	return cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)


cap = cv2.VideoCapture('cctv_main_door.mp4')

font = cv2.FONT_HERSHEY_SIMPLEX

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0,(int(cap.get(3)*0.75),int(cap.get(4)*0.75)),False) 

if(cap.isOpened() == False):
	print("error opening the file")

while(cap.isOpened()):
	ret, frame = cap.read()
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	if frame is not None:
		cv2.putText(gray,str(datetime.now()),(10,30),font,1,(0,0,255),2,cv2.LINE_AA)
		height,width = gray.shape
		upper_left = (int(width/2-10.51),int(height/2-10.51))
		bottom_right = (int(width/2+10.51),int(height/2+10.51))
		cv2.rectangle(gray, upper_left,bottom_right,(255,255,255),2)
		cv2.imshow("video", gray)
		gray = rescale(gray,percent=75)
		out.write(gray)
		if cv2.waitKey(25) & 0xFF == ord('q') :
			break


	else:
		print("Frame is none")
		break

cap.release()
out.release()
cv2.destroyAllWindows()
print("Video Stop")
