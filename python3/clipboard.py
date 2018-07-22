#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from android import Android 

droid = Android()
s = droid.getClipboard()
print(s)