import cv

#to use relative path, note that the working directory is the main qpython folder
#to use absolute path, just copy and paste the path from your file manager 
srcPath = 'great.jpg'
desPath = 'call.jpg'
img = cv.imread(srcPath, 0)
cv.imwrite(desPath, img)