import wx
import gui.mainwindow

app = wx.App()
mainwindow = gui.mainwindow.MainWindow()
mainwindow.Show()
app.MainLoop()
