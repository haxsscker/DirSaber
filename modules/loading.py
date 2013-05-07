#! /usr/bin/env python
#coding=utf-8

def getWordlistLength(_wordlist):
        num_lines = sum(1 for line in open(_wordlist))
        return num_lines

class Loading(threading.Thread):
    def __init__(self,maxloading):
        self.maxloading = maxloading
        threading.Thread.__init__(self)      
    def run(self):
        while queue.qsize()>0:
            self.percent = 100 * (self.maxloading - queue.qsize()) / self.maxloading
            if self.percent > 100:
                self.percent = 100
            print 'complete percent: ' + str(self.percent) + '%',
            sys.stdout.write("\r")
            time.sleep(1)
        print 'complete percent: 100%',

    maxloading = queue.qsize()
    view_loading = Loading(maxloading)
    view_loading.start()