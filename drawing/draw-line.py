import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

#Draw green rectangle from top keft corner to bottom right
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#Draw a circle with center and radius
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

#Draw ellipse

'''
To draw the ellipse, we need to pass several arguments. One argument is the center location (x,y). Next argument is axes lengths (major axis length, minor axis length). angle is the angle of rotation of ellipse in anti-clockwise direction. startAngle and endAngle denotes the starting and ending of ellipse arc measured in clockwise direction from major axis. i.e. giving values 0 and 360 gives the full ellipse. For more details, check the documentation of cv2.ellipse(). Below example draws a half ellipse at the center of the image.
'''

img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

'''
To draw a polygon, first you need
coordinates of vertices. Make those
points into an array of shape ROWSx1x2
where ROWS are number of vertices and it
should be of type int32. Here we draw a
small polygon of with four vertices in
 yellow color.

'''
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))



cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
