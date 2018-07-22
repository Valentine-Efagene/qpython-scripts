import android

droid = android.Android()
#droid.pickContact()
cont = droid.pickContact()
droid.phoneDial(cont[2]['data']) 