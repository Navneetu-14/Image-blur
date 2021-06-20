#image blur in this code we have done not only make image blur ,i have add two  more feature here that it Resize image and give output with three image one is original,next one is blur image and third one is Resize image at same time.

import cv2
 
img = cv2.imread('gov.jpg',0) #for color change of image in place of Zero put one it represent color image in original and in blur format..
# make sure that you have saved it in the same folder
#blurImg = cv2.blur(img,(10,10))
#cv2.imshow('blurred image',blurImg)
#cv2.imshow('gov.jpg',img)
#(type(img))  # Print the img variable data type
#print(np.shape(img))  # Print the img variable dimension at that time you have to import numpy package
print(img.shape)
width ,height =300 ,300
imgResize = cv2.resize(img,(width,height))
print(imgResize.shape)

#cv2.imshow("gov",img)
cv2.imshow("gov Resize",imgResize)
#blurImg = cv2.blur(img,(10,10))
blurimgResize = cv2.blur(imgResize,(10,10))
cv2.imshow('blurred image',blurimgResize)
cv2.imshow('gov.jpg',imgResize)

#make three copy of one image in three diffrernt view..
import cv2
import numpy as np
img = cv2.imread('leaf.jpg')  #download image from browser

print(np.shape(img))  # Print the img variable dimension in format of original image height and width
print(img.shape)
width ,height =300 ,300
imgResize = cv2.resize(img,(width,height)) #resize image
print(imgResize.shape)

cv2.imshow("gov Resize",imgResize)#print image

blurimgResize = cv2.blur(imgResize,(10,10))  #blur image display
cv2.imshow('blurred image',blurimgResize)
cv2.imshow('leaf.jpg',imgResize)

#CONVERT Original image in BGR format

lower_range = np.array([0,0,0])  # Set the Lower range value of color in BGR
upper_range = np.array([100,70,255])   # Set the Upper range value of color in BGR
mask = cv2.inRange(img,lower_range,upper_range) # Create a mask with range
result = cv2.bitwise_and(img,img,mask = mask)  # Performing bitwise and operation with mask in img variable

cv2.imshow('gov.jpg',result) # Image after bitwise operation


#Convert image into Gray Format
bw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # Converting the Orginal image to Gray
bw_bgr = cv2.cvtColor(bw,cv2.COLOR_GRAY2BGR) # Converting the Gray image to BGR format
result2 = cv2.bitwise_or(bw_bgr,result) # Performing Bitwise OR operation with gray bgr image and previous result image

cv2.imshow('gov.jpg',result2)  # Showing The Final Result Image'''

cv2.waitKey(0)
cv2.destroyAllWindows()





