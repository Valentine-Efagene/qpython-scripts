from androidhelper import Android
import json
import time
import os

droid = Android()

def getDevice():
    for k, v in droid.usbserialGetDeviceList().result.items():
        if "1A86" in v:
           print k, v
        h = json.loads(v)[-1]
        return h
        
def getDeviceID(h):
    ret = droid.usbserialConnect(h)
    print "Connection status:", json.loads(ret.result)[0]
    uuid = json.loads(ret.result)[-1]
    return uuid
    
def waitForData(uuid):
    while not droid.usbserialReadReady(uuid).result:
        pass
        
def read():
    while True:
        buf = droid.usbserialRead(uuid)
        print buf
    
h = getDevice()

if h is not None:
    print "Connecting to", h
else:
    print "No device connected"
    os.exit(0)
    
uuid = getDeviceID(h)
print "Active connections", droid.usbserialActiveConnections().result.items()
print "Waiting for data..."
waitForData(uuid)
print "Reading..."
read()