#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class MainWindow:
	def destroy_event(self, widget, data=None):
		gtk.main_quit()
	def add_clicked(self, widget, event,data=None):
		item = gtk.ListItem("New Item")
		item.show()
		self.repoList.append_items([item])
		print "test"
	def __init__(self):
		#Fenster erstellen
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("SVN Manager")
		self.window.connect("destroy", self.destroy_event, None)
		self.window.set_border_width(10)

		#VBox erstellen
		vbox = gtk.VBox(spacing=5)
		
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
		control_box = gtk.HBox()
		add_button = gtk.Button("Add")
		add_button.show()
		add_button.connect("button-press-event", self.add_clicked, None)
		control_box.add(add_button)
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
