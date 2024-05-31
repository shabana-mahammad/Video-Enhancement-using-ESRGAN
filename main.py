# Importing all necessary libraries 
import cv2 
import os 
from PIL import Image
# Read the video from specified path 
cam = cv2.VideoCapture("tree-low.mp4") 
skz= 0 # size of the original image
try: 
	
	# creating a folder named data 
	if not os.path.exists('data'): 
		os.makedirs('data') 

# if not created then raise error 
except OSError: 
	print ('Error: Creating directory of data') 

# frame 
currentframe = 0

while(True): 
	
	# reading from frame 
	ret,frame = cam.read() 

	if ret: 
		# if video is still left continue creating images 
		name = './data/frame' + str(currentframe) + '.png'
		print ('Creating...' + name) 

		# writing the extracted images 
		cv2.imwrite(name, frame) 
		image = Image.open(name)
		print("before-img-size",image.size)
		image.thumbnail((120, 68))
		if(currentframe==0):
			skz=image.size
		image.save('./img-dict/frame' + str(currentframe) + '.png')
		print("after-size",image.size)
		
		# increasing counter so that it will 
		# show how many frames are created 
		currentframe += 1
		
	else: 
		break

# Release all space and windows once done 
print("THE SIZE OF THE ORIGINAL IMAGE ",skz)
cam.release() 
cv2.destroyAllWindows() 

