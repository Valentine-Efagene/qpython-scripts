#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import re

str = "hfidbd361.00 NGN"

if re.search("\d{3}.\d{2} NGN", str):
  rate = re.findall("\d{3}.\d{2} NGN", str)
  rate = rate[0]
  print(rate)
else:
  print("found nothing")
