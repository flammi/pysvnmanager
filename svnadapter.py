#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import shutil
import pysvn
import json

class FolderNotFound(Exception):
	pass

class RepoNameInUse(Exception):
	pass

class NotAnSVN(Exception):
	pass

class SVNAdapter():
	def __init__(self, dbfile=None):
		if dbfile is not None:
			self.repolist = json.load(open(dbfile,"r"))
		else:			
			self.repolist = {}
		self.pysvnclient = pysvn.Client()
	def addRepo(self, name, path):
		if not os.path.exists(path):
			raise FolderNotFound()
		if name in self.repolist:
			raise RepoNameInUse()
		#Validate .svn dir
		if not os.path.exists(os.path.join(path, ".svn")):
			raise NotAnSVN()
		self.repolist[name] = os.path.abspath(path)
	def updateRepo(self, name):
		self.pysvnclient.update(self.repolist[name])
	def checkRepoForUpdates(self, name):
		repoStatus = self.pysvnclient.status(self.repolist[name], recurse=True, get_all=False, update=True)
		mustBeUpdated = False
		for status in repoStatus:
			print status.path," - ",str(status.repos_text_status)
			if not status.repos_text_status in [pysvn.wc_status_kind.normal, pysvn.wc_status_kind.none]:
				mustBeUpdated = True
		return mustBeUpdated
	def saveToDisk(self, dbFile):
		json.dump(self.repolist, open(dbFile,"w"),sort_keys=True, indent=4)
	def delRepo(self, name, removeFromDisk=False):
		if removeFromDisk:
			shutil.rmtree(self.repolist[name])
		del self.repolist[name]
	def listRepos(self):
		return self.repolist.items()

if __name__ == "__main__":
	adapter = SVNAdapter()
	adapter.addRepo("MyRepo", "testrepo_co")
#	adapter.updateRepo("MyRepo")
	adapter.saveToDisk("test.db")
	print adapter.checkRepoForUpdates("MyRepo")
	print adapter.listRepos()

	adapter2 = SVNAdapter("test.db")
	adapter2.listRepos()
#	adapter.delRepo("MyRepo",True)
