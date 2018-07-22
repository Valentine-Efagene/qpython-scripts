import urllib 
import urllib2

params = {'param1': 'value1'} 
req = urllib2.Request("http://cnn.com", urllib.urlencode(params)) 
res = urllib2.urlopen(req) 
data = res.read()
print data