#!/usr/bin/env python2
#-*-encoding:utf-8-*-
import msvcrt, os, threading

# class Loading(threading.Thread):
# 	def __init__(self,maxloading):
# 		self.maxloading = maxloading
# 		threading.Thread.__init__(self)
# 		self.percent = 0
# 	def run(self):
# 		while queue.qsize()>0 and self.percent < 100:
# 			self.percent = 100 * (self.maxloading - queue.qsize()) / self.maxloading
# 			if self.percent > 100:
# 				self.percent = 100
# 			print 'complete percent: ' + str(self.percent) + '%',
# 			sys.stdout.write("\r")
# 			time.sleep(1)


class ThreadGetKey(threading.Thread):
	def run(self):
		try:		   
			self.chr = msvcrt.getch()
			if self.chr == 'q':
				print "stopped by your action ( q )"
				os._exit(1)
		except:
			pass