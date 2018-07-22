from androidhelper import Android

droid = Android()
path = "/sdcard/qpython/photos/test.jpg"
droid.cameraCapturePicture(path)
#droid.cameraInteractiveCapturePicture(path)