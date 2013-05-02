class f4ckDir:
	with open(wordlist) as comfile:
		for line in comfile:
			line = line.strip("\r\n")
			req = u2.Request(sys.argv[1] + "/" + line)
			try:
				u2.urlopen(req)
			except u2.HTTPError as hr:
				if hr.code == 404:
					print mode+": " + line.ljust(50,' ') + "[Not found]"
			except u2.URLError as ur:
				print "URL error:", ur.args
				exit()
			except ValueError as vr:
				print "Value error:", vr.args
				exit()
			except:
				print "Unknown exception: exit..."
				exit()
			else:
				print mode+": " + line.ljust(50,' ') + "[OK]"
				if logging_support !=0:
				   logging_session.writelog(mode+": " + line.ljust(50,' ') + "[OK]\n")
				else:
					pass
			try:
				pass
			except KeyboardInterrupt as kierr:
				print "\nInterrupted by user: (CTRL+C or Delete)"
				exit()