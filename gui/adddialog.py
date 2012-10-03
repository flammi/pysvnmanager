# -*- coding: utf-8 -*-

import wx

class AddDialog(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, title="SVN einfügen")
		box = wx.BoxSizer(wx.HORIZONTAL)
		box.AddSpacer(20)
		box.Add(wx.StaticText(self, -1, "Pfad:"),0)
		box.Add(wx.TextCtrl(self),1)
		addBtn = wx.Button(self,label="Hinzufügen")
		addBtn.Bind(wx.EVT_BUTTON, self.addClick)
		box.Add(addBtn)
		self.SetSizer(box)
	def addClick(self, event):
		pass
