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
