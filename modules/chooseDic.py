#!/usr/bin/env python2
#-*-encoding:utf-8-*-
from modules.Saber_col import printError
import os,sys

def chooseDic(smode):
	path = sys.path[0]
	path = path.replace("\\","/")
	if smode == "shell":
		wordlist=path+"/dic/shell.txt"
	elif smode == "backup":
		wordlist=path+"/dic/backups.txt"
	elif smode == "admin":
		wordlist=path+"/dic/admins.txt"
	elif smode == "dir": 
		wordlist=path+"/dic/dir.txt"
	elif smode == "files": 
		wordlist=path+"/dic/files.txt"
	elif smode == "all": 
		wordlist=path+"/dic/"
	else:
		printError("[-]warning!!!: Mode not specified")
		wordlist=path+"/dic/"+smode+".txt"
	if smode != "all" and not os.access(wordlist, os.F_OK):
		printError ("[-] File " + wordlist + " does not exist or " + "you are not permitted to access to the file" )
		os._exit(1)
	return wordlist