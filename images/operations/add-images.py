import numpy as np
import cv2

img1 = cv2.imread('car.jpg',0)
img2 = cv2.imread('messigray.png',0)

img=img1 + img2

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
