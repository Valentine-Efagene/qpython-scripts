from android import Android

droid = Android()
path = "/sdcard/qpython/photos"
droid.cameraCapturePicture(path)
#droid.cameraInteractiveCapturePicture(path)