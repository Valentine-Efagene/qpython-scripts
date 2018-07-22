#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import urllib.request 
fp = urllib.request.urlopen("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=NGN") 
mybytes = fp.read() 
mystr = mybytes.decode("utf8") 
fp.close() 
print(mystr)
