#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from android import Android 
import pprint

droid = Android()
apps = droid.getLaunchableApplications()
pprint.pprint(apps.result)