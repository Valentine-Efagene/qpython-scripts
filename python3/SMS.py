import android

droid = android.Android()
number = droid.dialogGetInput('Send SMS', 'Phone Number?').result
message = 'Test SMS'
result = droid.smsSend(number, message)