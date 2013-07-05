#!/usr/bin/env python2
#-*-encoding:utf-8-*-
#Thanks for lazze

from modules.Saber_col import printError,printWait
printWait( '''
    #######################################################
    #                                                     #
    #                  DirSaber  v3.0                     #
    #             BY haxsscker#c0deplay.com               #
    #                  team.f4ck.net                      #
    #                                                     #
    #######################################################
''')

import getopt,sys
from modules.urlcheck import urlcheck
from modules.chooseDic import chooseDic
from modules.f4ckDir import f4ckDir
from modules.f4ckDirDG import f4ckDirDG
from lib.proxy import proxycheck
        
def printSyntax():
	 printWait( """
#-------------------------------------------------#
#	-m shell    :It looks for Webshells
#	-m backup   :It looks for Backup
#	-m admin    :It looks for Adminpages
#	-m dir      :It looks for Sensitive Directories
#	-m <others> :It looks for the dic you specified
#	-m all      :It looks for All Above
#
#   -d          :It will recursive the directory
#-------------------------------------------------#
# Usage	:  
        ./main.py <http:url> -m <mode> [-p <proxy>] [-t <asp/aspx/php/jsp>] [-d]
                   host.com  -m shell  [-p 127.0.0.1:8118] [-t asp] [-d]

""")

if __name__=='__main__':
	###################################################
	# Syntax check
	if len (sys.argv) < 4:
		printSyntax()
		sys.exit(1)
	
	else:
		try:
			opts, args = getopt.getopt (sys.argv[2:], "m:p:t:d")
		except:
			printSyntax()
			sys.exit(1)
	###################################################
	# Load input parameters
	sproxy = None
	smode = None
	sscript = None
	DG = None
	for opt, arg in opts:
		if opt == '-m':
			smode = arg
		elif opt == '-p':
			sproxy = arg
		elif opt == '-t':
			sscript = arg
		elif opt == '-d':
			DG = 1
		else:
			printError("Unknown options!!") 
			printSyntax()
			sys.exit(1)

	site = sys.argv[1]
	site = urlcheck(site)
	if site == None:
		sys.exit(1)
	sdir = chooseDic(smode)
	if sproxy:
		is_sproxy = proxycheck(sproxy,1)
		if not is_sproxy:
			go_on = raw_input("GO ON to check the website? (N/y): ")
			if go_on != "y":
				sys.exit(1)
	if sscript:
	    print "script: "+sscript
	if DG:
		f4ckDirDG(site,sdir,smode,sproxy,sscript)
	else:
		f4ckDir(site,sdir,smode,sproxy,sscript)





