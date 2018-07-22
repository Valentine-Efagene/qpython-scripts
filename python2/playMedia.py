from androidhelper import Android
import time

droid = Android()
startTime = time.time()
duration = 1000 * 60 * 2 #milliseconds ie 2 minutes
path = "/storage/9016-4EF8/Music/O children.mp3"
droid.mediaPlay(path)
droid.mediaPlayStart()
droid.eventWait(duration)
droid.mediaPlayClose()
