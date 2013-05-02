#!/usr/bin/env python2
#-*-encoding:utf-8-*-

class logging:
	f=""
	def __init__(self,_logfile):
		self._logfile=_logfile
		self.f = open(self._logfile, "w")
		self.f.write("Sensitive finder logs \n")
	def writelog(self,_message):
		try:
			self.f.write(_message) # Write a string to a file
		except IOError:
   	 		pass	
   	def close(self):
   		self.f.close()