import re

str = "hello"
pattern = "h"

if re.search(pattern, str) :
    print "found"
else:
    print "not found"