#!/usr/bin/env python
import urllib2,socket,httplib
from modules.Saber_col import printError,printWait,printResult

def proxycheck(myhttpproxy,myproxy):
    try:
        if myproxy:
            printWait("[+] Testing Proxy...")
            h2 = httplib.HTTPConnection(myhttpproxy)
            h2.connect()
            printResult("[+] Proxy:"+myhttpproxy+"\n")
            return 1
    except(socket.timeout):
        printError("[-] Proxy Timed Out")
        return None
    except(NameError):
        printError("[-] Proxy Not Given")
        return None
    except:
        printError("[-] Proxy Failed")
        return None

def myproxy(proxyserver):
    try:
        if proxyserver[0:4] != "http":
            proxyserver = "http://" + proxyserver
        if proxyserver[-1] != "/":
            proxyserver = proxyserver + "/"
        proxy_handler = urllib2.ProxyHandler({'http': proxyserver})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        return True
    except:
        return None

# def proxy1(user,password):
#     # work
#     proxy = 'http://%s:%s@%s' % (user, passwd, proxyserver)
#     opener = urllib2.build_opener( urllib2.ProxyHandler({'http':proxy}) )
#     urllib2.install_opener( opener )

#     sContent = urllib2.urlopen(url)
#     print sContent.read()

# def proxy2():
#     # work for someone, but not for me
#     passmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
#     passmgr.add_password('realm', proxyserver, user, passwd)
#     authinfo = urllib2.ProxyBasicAuthHandler(passmgr)

#     proxy = 'http://%s' % proxyserver
#     opener = urllib2.build_opener(urllib2.ProxyHandler( {'http':proxy} ), authinfo)
#     urllib2.install_opener(opener)

#     sContent = urllib2.urlopen(url)
#     print sContent.read()

# def proxy3():
#     # work for someone, but not for me
#     authinfo = urllib2.HTTPBasicAuthHandler()
#     authinfo.add_password('realm', proxyserver, user, passwd)
    
#     proxy = 'http://%s' % proxyserver
#     opener = urllib2.build_opener(urllib2.ProxyHandler( {'http':proxy} ), authinfo)
#     urllib2.install_opener(opener)
    
#     sContent = urllib2.urlopen(url)
#     print sContent.read()


