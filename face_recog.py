#import libraries of python OpenCV2
import cv2 

# load the required trained XML classifiers 
# haarcascade_frontalface_default.xml 
#keep the xml file and the python file in the same directory
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

# haarcascade_eye.xml- XML file for detecting eyes 
eye = cv2.CascadeClassifier('haarcascade_eye.xml') 
 
capture = cv2.VideoCapture(0) 

# loop runs if capturing has been initialized. 
while 1: 

	# reads faces from a camera 
	ret, img = capture.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face.detectMultiScale(gray, 1.3, 5) 
        #For capturing faces 
	for (x,y,w,h) in faces: 
		
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
		gray = gray[y:y+h, x:x+w] 
		color = img[y:y+h, x:x+w] 

		
		eyes = eye.detectMultiScale(gray) 

		#For capturing eyes 
		for (ex,ey,ew,eh) in eyes: 
			cv2.rectangle(color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 

	# To show the captured image
	cv2.imshow('img',img) 

	# Wait 5for Esc key to stop 
	k = cv2.waitKey(30) & 0xff
	if k == 28: 
		break

# Close the window 
capture.release() 
cv2.destroyAllWindows() 
