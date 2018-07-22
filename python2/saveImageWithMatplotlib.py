import numpy as np 
import cv

 # Create a black image 
#img = np.zeros((512,512,3), np.uint8) 
img = cv.imread('great.jpg', 1)
 # Draw a diagonal blue line with thickness of 5 px 
img = cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.imwrite('blessed.jpg', img) 