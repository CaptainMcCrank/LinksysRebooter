import httplib
import sys
import urllib2
import urllib
import sys
import re
import base64
from urlparse import urlparse

server = '172.16.0.1'
resource = '/AdminRebootConfig.asp'
username = ''
password = 'admin'

# if you want to run this example you'll need to supply
# a protected page with your username and password

httpcon = httplib.HTTPConnection(server)
httpcon.putrequest('GET', resource)
httpcon.putheader('Connection', 'keep-alive')
base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
authheader =  "Basic %s" % base64string
httpcon.putheader("Authorization", authheader)
try:
	httpcon.endheaders()
	reply = httpcon.getresponse()
	print "Router is rebooting"
except IOError, e:
	# here we shouldn't fail if the username/password is right
	print "It looks like the username or password is wrong."
	sys.exit(1)