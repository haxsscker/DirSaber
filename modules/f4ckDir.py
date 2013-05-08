#!/usr/bin/env python2
#-*-encoding:utf-8-*-
from modules.Saber_col import printError, printWait, printResult
from lib.logging import logging
import urllib2,sys,threading,Queue

def f4ckDir(site,sdir,smode):
    try:
        filename = site.replace ("http://","").replace ("/","")
        ldir = "/".join(sdir.split("/")[0:-2])
        logging_file=logging(ldir+"/log/"+filename+".txt")

    except Exception,e:
        print e
        pass

    global queue
    queue = Queue.Queue()
    threads = []

    with open(sdir) as dirfile:
        for line in dirfile:
            line = line.strip("\r").strip("\n")
            queue.put(line)
    for i in range(5):
        a = finder(site,smode,logging_file)
        a.start()
        threads.append(a)
    for j in threads:
        j.join()
            
    printWait(smode+"------->" + "task".ljust(48,' ') + "[ALL DONE]")
    try:
        logging_file.close()
    except:
        pass

class finder(threading.Thread):
    def __init__(self,site,smode,logging_file):
        threading.Thread.__init__(self)
        self.site = site
        self.smode = smode
        self.logging_file = logging_file

    def run(self):
        while 1:
            if queue.empty()== True:
                break
            self.line = str(queue.get())
            self.req = urllib2.Request(self.site + "/" + self.line)
            try:
                urllib2.urlopen(self.req,timeout=5)
            except urllib2.HTTPError as self.hr:
                if self.hr.code == 404:
                    print self.smode+": " + self.line.ljust(50,' ') + "[Not found]",
                    sys.stdout.write("\r")
            except urllib2.URLError as self.ur:
                printError("URL error:" + self.line.ljust(50,' ') + str(self.ur.args))
                exit()
            except ValueError as self.vr:
                pprintError("Value error:" + str(self.vr.args))
                exit()
            except:
                printWait("Unknown exception: exit...")
                exit()
            else:
                printResult(self.smode+": " + self.line.ljust(57,' ') + "[OK]")
                try:
                	self.logging_file.writelog(self.smode+": " + self.line.ljust(50,' ') + "[OK]\n")
                except:
                	pass
