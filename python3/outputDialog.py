#-*-coding:utf8;-*-
#qpy:3
#qpy:console
from androidhelper import Android 

droid = Android()
amountInDollars = 32
amountInNaira = 1
title = str(amountInDollars);
message = str(amountInNaira)
droid.dialogCreateAlert(title, message)
