#!/usr/bin/env python2
#-*-encoding:utf-8-*-
import msvcrt, os, threading

class ThreadGetKey(threading.Thread):
	def run(self):
		try:		   
			self.chr = msvcrt.getch()
			if self.chr == 'q':
				print "stopped by your action ( q )"
				os._exit(1)
		except:
			pass