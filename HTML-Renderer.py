#!/usr/bin/python

import Tkinter
from Tkinter import Label
from Tkinter import Text
from Tkinter import StringVar
from Tkinter import Message

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
text = Text(base,
			font="Times 14",
			fg="black",
			bg="white")
text.pack()

"""		Message Box to Reflect User Inputs		"""
strVar = StringVar()
output = Message(base, textvariable=strVar)
strVar.set("TESTING: What up, world!")
output.pack()

# Display the window
base.mainloop()
