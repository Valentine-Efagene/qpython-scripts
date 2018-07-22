#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from androidhelper import Android

droid = Android()

for k, v in android.usbserialGetDeviceList().result.items():
        print(k, v)