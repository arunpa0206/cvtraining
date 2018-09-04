import cv2
import numpy as np

img = cv2.imread('car.jpg')
ball = img[104:240, 154:370]
img[154:290, 204:420] = ball

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
