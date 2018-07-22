from androidhelper import Android
import time

status = {
    	1:"unknown",
    	2:"charging",
    	3:"discharging",
    	4:"not charging",
    	5:"full"
    	}
    	
health = {
	1: "unknown",
	2: "good",
	3: "overheat",
	4: "dead",
	5: "over voltage",
	6: "unspecified failure"
	}
	
plug = {
	-1: "unknown",
	0: "unplugged",
	1: "AC power source",
	2: "USB power source",
	}
	
droid = Android();
droid.batteryStartMonitoring()
time.sleep(1)


def printStatus():
    batStat = droid.batteryGetStatus().result
    print "Status: " + status[batStat]

def printLevel():
    batLevel = droid.batteryGetLevel().result
    print "Battery level: " + str(batLevel) + "%"
    
def printTemperature():
    batTemp = droid.batteryGetTemperature().result
    print "Battery temperature: " + str(batTemp)
    
def printHealth():
    batHealth = droid.batteryGetHealth().result
    print "Battery health: " + health[batHealth]
    
def printPlug():
    batPlug = droid.batteryGetPlugType().result
    print "Battery plug: " + plug[batPlug]
    
printLevel()
printStatus()
printHealth()
printPlug()
droid.batteryStopMonitoring()
