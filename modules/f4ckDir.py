#!/usr/bin/env python2
#-*-encoding:utf-8-*-
from modules.Saber_col import printError, printWait, printResult
from lib.logging import logging
import urllib2

def f4ckDir(site,sdir,smode):
	try:
		filename = site.replace ("http://","").replace ("/","")
		ldir = "/".join(sdir.split("/")[0:-2])
		logging_file=logging(ldir+"/log/"+filename+".txt")

	except Exception,e:
		print e
		pass

	with open(sdir) as dirfile:
		for line in dirfile:
			line = line.strip("\r").strip("\n")
			req = urllib2.Request(site + "/" + line)
			try:
				urllib2.urlopen(req,timeout=5)
			except urllib2.HTTPError as hr:
				if hr.code == 404:
					print smode+": " + line.ljust(50,' ') + "[Not found]"
			except urllib2.URLError as ur:
				printError("URL error:", ur.args)
				exit()
			except ValueError as vr:
				pprintError("Value error:", vr.args)
				exit()
			except:
				printWait("Unknown exception: exit...")
				exit()
			else:
				printResult(smode+": " + line.ljust(50,' ') + "[OK]")
				if logging.writelog !=0:
				   logging_file.writelog(smode+": " + line.ljust(50,' ') + "[OK]\n")
	try:
		logging_file.close()
	except:
		pass