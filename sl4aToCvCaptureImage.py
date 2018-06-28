import cv
from androidhelper import Android

droid = Android()
path = "/sdcard/qpython/photos/test.jpg"
droid.cameraCapturePicture(path)
#droid.cameraInteractiveCapturePicture(path)
img = cv.imread(path)
cv.imwrite('/sdcard/qpython/photos/cvImage.jpg', img)