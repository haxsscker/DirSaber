#!/usr/bin/env python2
#-*-encoding:utf-8-*-
import urllib2
from modules.Saber_col import printResult,printProcess,printError

def urlcheck(site):
	if site[:4] != "http":
		site = "http://"+site
	if site.endswith("--"):
  		site = site.rstrip('--')
	if site.endswith("/*"):
  		site = site.rstrip('/*')
	try:
		printProcess("[!] Checking website " + site + "...")
		req = urllib2.Request(site)
		urllib2.urlopen(site,timeout = 10)
		printResult("[+] " + site +" appears to be Online.\n")
	except:
		printError("[-] Server offline or invalid URL")
		return None
	return site