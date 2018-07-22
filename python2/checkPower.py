from androidhelper import Android
import time
	
droid = Android();
droid.batteryStartMonitoring()
time.sleep(1)

batStat = droid.batteryGetStatus().result

while batStat != 2:
    batStat = droid.batteryGetStatus().result
    
hour = time.localtime(time.time()).tm_hour
min = time.localtime(time.time()).tm_min
f = open("powerLog.txt", "a+")
f.write("Time: " + str(hour) + ": " + str(min) + "\n")
print "Time: ", hour, ": ", min
    
droid.batteryStopMonitoring()
