#!/usr/bin/python

import Tkinter
from Tkinter import Label

# Tkinter.Tk: Base class to inherit from for standard windows.
base = Tkinter.Tk()

title = Label(base,
			text="HTML Renderer",
			font="Times 20 bold",
			fg="white",
			bg="black")
title.pack()	# Fit the size of the window to text

# Opens/Runs the GUI
base.mainloop()
