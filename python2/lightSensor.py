from androidhelper import Android
import time 

droid = Android() 

while True:
  droid.startSensingTimed(1, 50) 
  time.sleep(0.1) 
  s3 = droid.sensorsGetLight().result 
  droid.stopSensing()
  print s3