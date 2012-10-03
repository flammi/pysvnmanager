import wx

class MainWindow(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None)
		self.buildGui()
	def buildGui(self):
		mainPanel = wx.Panel(self)

		vbox = wx.BoxSizer(wx.VERTICAL)
		vbox.Add(wx.StaticText(mainPanel,label="SVN-Repos:"))
		vbox.Add(wx.ListBox(mainPanel), 1, wx.EXPAND | wx.ALL)
		mainPanel.SetSizer(vbox)
		
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(mainPanel,1,wx.EXPAND | wx.ALL, 20)
		self.SetSizer(mainSizer)

app = wx.App()
wnd = MainWindow()
wnd.Show()
app.MainLoop()
