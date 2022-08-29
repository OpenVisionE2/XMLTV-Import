# -*- coding: utf-8 -*-
# logging for XMLTV importer
#
# One can simply use
# import log
# print>>log, "Some text"
# because the log unit looks enough like a file!

import sys
from six import StringIO
import threading

logfile = StringIO()
# Need to make our operations thread-safe.
mutex = threading.Lock()


def write(data):
	with mutex:
		if logfile.tell() > 51200:
			# Do a sort of 50k round robin
			logfile.truncate(0)
			logfile.seek(0)

		logfile.write(data)
	sys.stdout.write(data)


def getvalue():
	with mutex:
		pos = logfile.tell()
		head = logfile.read()
		logfile.seek(0)
		tail = logfile.read(pos)
	return head + tail
