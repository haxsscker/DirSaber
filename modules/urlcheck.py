#!/usr/bin/env python2
#-*-encoding:utf-8-*-

def urlcheck(url):
	try:
	       	print ("[!] Checking website " + _url + "...")
	       	req = u2.Request(_url)
	       	u2.urlopen(req)
	       	print "[!] " +_url+" appears to be Online.\n"
   	except:
	        print("[-] Server offline or invalid URL")
	        sys.exit()