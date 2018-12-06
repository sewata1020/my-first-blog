# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:31:32 2018

@author: 今村晃一
"""

import urllib
import oauth2
import random 

#
CK = ''
CS = '' 
#
AT = ''
AS = ''

def API():

	client = oauth2.Client(
	oauth2.Consumer(key=CK,secret=CS),
	oauth2.Token(AT,AS)
	)
 
	rnd_str = "".join([random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for x in xrange(10)])
 
	params = urllib.urlencode({
	'screen_name' : rnd_str,
	'password' : GenePW,
	'email' : rnd_str+'@gmail.com',
	'name' : rnd_str,
	})
 
	res = client.request(
	'http://api.twitter.com/1/account/generate.json','POST',params
	)
 
	if res[0]['status'] == '200':
		print "ID: "+rnd_str
		print "PW: "+GenePW
	else:
		print res[1]
 
if __name__ == '__main__':
	API() 