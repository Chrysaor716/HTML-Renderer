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
text = Text(base)
text.pack()

# Display the window
base.mainloop()
