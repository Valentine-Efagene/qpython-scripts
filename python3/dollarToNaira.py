#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import urllib.request 
import re
import androidhelper

droid = androidhelper.Android()
amountInDollars = float(droid.dialogGetInput('Username').result)
fp = urllib.request.urlopen("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=NGN") 
mybytes = fp.read() 
mystr = mybytes.decode("utf8") 
fp.close() 

if re.search("\d{3}.\d{3} NGN", mystr):
  l_rate = re.findall("\d{3}.\d{3} NGN", mystr)
  s_rate = l_rate[0] 
  regex = re.compile(" NGN");
  s_rate = regex.sub("", s_rate);
  rate = float(s_rate)
  amountInNaira = rate * amountInDollars
  print(rate)
  print(amountInNaira)
  title = str(amountInDollars) + " dollars in naira is";
  message = str(amountInNaira)
  droid.dialogCreateAlert(title, message)
  droid.dialogShow()
else:
  print("found nothing")
