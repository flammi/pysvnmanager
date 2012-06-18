#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def getWCStatus(path):
	svnProcess = subprocess.Popen(["svn", "status", path],stdout=subprocess.PIPE)
	(output,st) = svnProcess.communicate()

	result = []
	for line in output.split("\n"):
		if line != "":
			result.append((line[0],line[1:].lstrip()))
	return result


if __name__ == "__main__":
	res = getWCStatus("/home/fabian/Uni Bremen/Robotik 1/")
	res = filter(lambda (x,y): x=='M', res)
	for elm in res:
		print "[%s] - %s" % (elm[0], elm[1])
