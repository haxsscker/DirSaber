#!/usr/bin/env python2
#-*-encoding:utf-8-*-

def chooseDic(smode):
	if mode == "shell":
		wordlist=shellwordlist
	elif mode == "backup":
		wordlist=backupwordlist
	elif mode == "admin":
		wordlist=adminwordlist
	elif mode == "dir": 
		wordlist=dirwordlist 
	elif mode == "files": 
		wordlist=fileswordlist 	
	else:
		print("[x] Mode not specified")
		exit()

	if not os.access(wordlist, os.F_OK):
	print(  "[x] File " + wordlist + " does not exist or "
		+ "you are not permitted to access to the file")
	exit()