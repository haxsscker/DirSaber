#!/usr/bin/env python2
#-*-encoding:utf-8-*-
#-------------------------------------------#
#	-shell:It looks for Webshells
#	-backup:It looks for Backup
#	-admin:It looks for Adminpages
#	-dir:It looks for Sensitive Directories
#	-all:It looks for All Above
#-------------------------------------------#
from modules.Saber_col import printError,printWait
printWait( '''
    #######################################################
    #                                                     #
    #                  DirSaber  v1.0                     #
    #             BY haxsscker#c0deplay.com               #
    #               Thx lazze#t00ls.net                   #
    #                  team.f4ck.net                      #
    #                                                     #
    #######################################################
''')

import getopt,sys
from modules.urlcheck import urlcheck
from modules.chooseDic import chooseDic
from modules.f4ckDir import f4ckDir
        
def printSyntax():
	 printWait( """
#-------------------------------------------------#
#	-shell:It looks for Webshells
#	-backup:It looks for Backup
#	-admin:It looks for Adminpages
#	-dir:It looks for Sensitive Directories
#	-all:It looks for All Above
#-------------------------------------------------#
# Usage	:	./DirSaber.py <http:url> -m <mode> -p <proxy>
			http://host.com  -m shell -p 127.0.0.1:8118

""")

if __name__=='__main__':
	###################################################
	# Syntax check
	if len (sys.argv) < 4:
		printSyntax()
		sys.exit(1)
	
	else:
		try:
			opts, args = getopt.getopt (sys.argv[2:], "m:p:")
		except:
			printSyntax()
			sys.exit(1)
	###################################################
	# Load input parameters
	sproxy = None
	smode = None
	for opt, arg in opts:
		if opt == '-m':
			smode = arg
		elif opt == '-p':
			sproxy = arg
		else:
			printError("Unknown options!!") 
			printSyntax()
			sys.exit(1)

	site = sys.argv[1]
	site = urlcheck(site)
	if site == None:
		sys.exit(1)
	sdir = chooseDic(smode)

	f4ckDir(site,sdir,smode)





