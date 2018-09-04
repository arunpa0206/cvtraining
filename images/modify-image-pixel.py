import cv2
import numpy as np

img = cv2.imread('car.jpg')

px = img[100,100]
#Aeeat with B,G,R is returned
print('[b,g,r]', px)

# accessing only blue pixel
blue = img[100,100,0]
print('b',blue)

#Modify pixel values
img[100,100] = [255,255,255]
print(img[100,100])


#Print the shape of an image
print(img.shape)

#Total number of pixels
print(img.size)
#Print the data type of image
print(img.dtype)
