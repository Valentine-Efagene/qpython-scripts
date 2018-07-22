import androidhelper

Droid = androidhelper.Android()
Droid.startSensingTimed(1, 250)
sensor = Droid.sensorsReadOrientation().result
Droid.stopSensing()