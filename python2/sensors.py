from androidhelper import Android
import time 

droid = Android() 
droid.startSensingTimed(1, 250) 
time.sleep(1) 
s1 = droid.readSensors().result
s2 = droid.sensorsGetAccuracy().result
s3 = droid.sensorsGetLight().result 
s4 = droid.sensorsReadAccelerometer().result 
s5 = droid.sensorsReadMagnetometer().result 
s6 = droid.sensorsReadOrientation().result 
droid.stopSensing()

print s3