#!/usr/bin/env python2
#-*-encoding:utf-8-*-
from modules.Saber_col import printError, printWait, printResult
from lib.logging import logging
import urllib2,sys,threading,collections,time
from lib.proxy import proxycheck,myproxy
from lib.ThreadGetKey import ThreadGetKey
import os,copy

def f4ckDirDG(site,sdir,smode,sproxy = None, sscript = None):
    if sproxy:
        connet_proxy = myproxy(sproxy)
        if not connet_proxy:
            printError("proxy Error!!")
            sys.exit(1)
    try:
        filename = site.replace ("http://","").replace ("/","")
        ldir = "/".join(sdir.split("/")[0:-2])
        logging_file=logging(ldir+"/log/"+filename+".txt")

    except Exception,e:
        print e
        pass

    global dpath
    dpath = []
    global queue
    global queueD
    firstRun = 1
    queue = collections.deque()
    queueD = collections.deque()
    threads = []

    if sdir.split('.')[-1] != "txt":
        files = os.listdir(sdir)
        for searchfile in files:
             if searchfile.split('.')[-1] == "txt":
                with open(sdir+searchfile) as dirfile:
                    for line in dirfile:
                        line = line.strip("\r").strip("\n")
                        if sscript and line.find(".") and line.split(".")[-1] == sscript:
                            queue.append(line) 
                        elif not sscript:
                            queue.append(line)
    else:
        with open(sdir) as dirfile:
            for line in dirfile:
                line = line.strip("\r").strip("\n")
                if sscript and line.find(".") and line.split(".")[-1] == sscript:
                    queue.append(line) 
                elif not sscript:
                    queue.append(line)
    queueD = copy.deepcopy(queue)
    ######################################################
    #shouhu_pro & jindu_pro
    shouhu = ThreadGetKey()
    shouhu.setDaemon(True)
    shouhu.start()

    # maxloading = queue.qsize()
    # view_loading = Loading(maxloading)
    # view_loading.start()

    #########################################################
    #lines start!
    while(dpath != [] or firstRun == 1):
        firstRun = 0
        Npath = None
        queue = copy.deepcopy(queueD)
        if dpath:
            Npath = dpath[0].strip("/")
            dpath = dpath.remove(dpath[0])
            if dpath == None:
                dpath = []
        for i in range(3):
            a = finderDG(site,smode,logging_file,Npath)
            a.start()
            threads.append(a)
        for j in threads:
            j.join()
        time.sleep(2)
            
    printWait(smode+"------->" + "task".ljust(48,' ') + "[ALL DONE]")
    try:
        logging_file.close()
    except:
        pass

class finderDG(threading.Thread):
    def __init__(self,site,smode,logging_file,Npath = None):
        threading.Thread.__init__(self)
        self.site = site
        self.smode = smode
        self.logging_file = logging_file
        self.Npath = Npath

    def run(self):
        while 1:
            try:
                self.line = str(queue.popleft())
            except:
                break
            if self.Npath:
                self.Npath = self.Npath
                self.req = urllib2.Request(self.site + "/" + self.Npath + "/" + self.line)
            else:
                self.req = urllib2.Request(self.site + "/" + self.line)
            try:
                urllib2.urlopen(self.req,timeout=10)
            except urllib2.HTTPError as self.hr:
                if self.hr.code == 404:
                    if self.Npath:
                        print self.smode+": " + self.Npath + "/" + self.line.ljust(70-len(self.Npath)-1,' '),
                    else:
                        print self.smode+": " + self.line.ljust(70,' '),
                    sys.stdout.write("\r")
            except urllib2.URLError as self.ur:
                printError("URL error:" + self.line.ljust(50,' ') + str(self.ur.args[0]).ljust(20,' '))
                exit()
            except ValueError as self.vr:
                pprintError("Value error:" + str(self.vr.args))
                exit()
            except:
                printWait("Unknown exception: exit...")
                exit()
            else:
                if len(self.line.split(".")) == 1:
                    if self.Npath:
                        dpath.append ( self.Npath + "/" + self.line.strip("/") )
                        printResult(self.smode+": " + self.Npath + "/" + self.line.ljust(56-len(self.Npath)-1,' ') + "[OK]".ljust(30,' '))
                    else:
                        dpath.append ( self.line )
                        printResult(self.smode+": " + self.line.ljust(56,' ') + "[OK]".ljust(30,' '))
                else:
                    printResult(self.smode+": " + self.line.ljust(56,' ') + "[OK]".ljust(30,' '))
                try:
                	self.logging_file.writelog(self.smode+": " + self.line.ljust(50,' ') + "[OK]\n")
                except:
                	pass
