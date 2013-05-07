#!/usr/bin/env python2
#-*-encoding:utf-8-*-

class logging:
	def __init__(self,logfile):
		self.logfile=logfile
		self.f = open(self.logfile, "w")
		self.f.write("-----------------f4ckDir logs-------------------- \n")
	def writelog(self,message):
		try:
			self.f.write(message)
		except IOError:
   	 		pass	
   	def close(self):
   		self.f.close()