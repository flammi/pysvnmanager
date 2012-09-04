#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class AddWindow:
	def __init__(self):
		self.window = gtk.Dialog()
		self.window.set_modal(True)
		self.window.set_title("Repo Add")
		self.window.set_border_width(10)

		hbox = gtk.HBox(spacing=5)

		self.url = gtk.Entry()

		hbox.add(gtk.Label("URL:"))
		hbox.add(self.url)
		
		okBtn = gtk.Button("Ok")
		okBtn.connect("button-press-event", self.ok_clicked, None)
		
		self.window.vbox.add(hbox)
		self.window.action_area.add(okBtn)
		self.window.show_all()
		self.window.run()
	def ok_clicked(self,widget,event,data=None):
		self.window.destroy()
		
	def getURL(self):
		return self.url.get_text()

class MainWindow:
	def destroy_event(self, widget, data=None):
		gtk.main_quit()
	def add_clicked(self, widget, event,data=None):
		#item = gtk.ListItem("New Item")
		#item.show()
		#self.repoList.append_items([item])
		addWindow = AddWindow()
		print addWindow.getURL()
		print "Add clicked"
	def del_clicked(self, widget, event, data=None):
		sel = self.repoList.get_selection()
		self.repoList.remove_items(sel)
		gtk.List()
		print "Delete clicked"
	def __init__(self):
		#Fenster erstellen
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("SVN Manager")
		self.window.connect("destroy", self.destroy_event, None)
		self.window.set_border_width(10)

		#VBox erstellen
		vbox = gtk.HBox(spacing=5,homogeneous=False)
		
		#Liste mit Repos erstellen
		self.repoList = gtk.List()
		i1 = gtk.ListItem("test")
		i1.show()
		i2 = gtk.ListItem("test2")
		i2.show()
		self.repoList.append_items([i1,i2])
		self.repoList.show()
		vbox.add(self.repoList)

		#Controls erstellen
		control_box = gtk.VBox()
		add_button = gtk.Button("Add")
		add_button.show()
		add_button.connect("button-press-event", self.add_clicked, None)
		del_button = gtk.Button("Del")
		del_button.show()
		del_button.connect("button-press-event", self.del_clicked, None)
		control_box.add(add_button)
		control_box.add(del_button)
		control_box.show()
		remove_button = gtk.Button("Del")
		remove_button.show()
		remove_button.connect("button-press-event", self.del_clicked, None)
		control_box.add(remove_button)
		control_box.show()
		vbox.add(control_box)
		vbox.show()
		
		#Fenster anzeigen
		self.window.add(vbox)
		self.window.show()
		print "Test"

if __name__ == "__main__":
	mw = MainWindow();
	gtk.main()
