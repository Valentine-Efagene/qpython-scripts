#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import urllib.request 
import re
import androidhelper

droid = androidhelper.Android()
amountInDollars = float(droid.dialogGetInput('Amount in dollars').result)
fp = urllib.request.urlopen("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=NGN") 
mybytes = fp.read() 
mystr = mybytes.decode("utf8") 
fp.close() 

if re.search("\d{2,}.\d{2,} NGN", mystr):
  l_rate = re.findall("\d{2,}.\d{2,} NGN", mystr)
  s_rate = l_rate[0] 
  regex = re.compile(" NGN");
  s_rate = regex.sub("", s_rate);
  rate = float(s_rate)
  amountInNaira = rate * amountInDollars
  d = "%.2f" %amountInDollars
  n = "%.2f" %amountInNaira
  print(d)
  print(n)
  title = "$" + d + "  in naira is";
  message = "N" + n
  droid.dialogCreateAlert(title, message)
  droid.dialogShow()
else:
  print("ERROR:")
  print("Could not obtain exchange rate.")
