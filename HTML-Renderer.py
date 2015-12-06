#!/usr/bin/python

import Tkinter
from Tkinter import Label
from Tkinter import Text

# Tkinter.Tk: Base class to inherit from for standard windows.
base = Tkinter.Tk()

"""		Title 		"""
base.title("HTML Renderer")

"""		Window Label		"""
title = Label(base,
			text="A more interactive HTML coding environment!",
			font="Times 10 bold",
			fg="white",		# Text color
			bg="black",		# Text background color
			anchor="center")
title.pack()	# Fit the size of the window to text

"""		Text Box For User Input		"""
usrInput = Text(base,
			font="Times 14",
			fg="black",
			bg="white")
usrInput.pack(fill="y", padx=10, side="left")

"""		Message Box to Reflect User Inputs		"""
output = Text(base,
			font="Times 14 bold",
			fg="black",
			bg="white")
#output.insert(index[,string])
output.pack(fill="y", padx=10, side="right")

# Display the window
base.mainloop()
