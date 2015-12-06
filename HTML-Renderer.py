#!/usr/bin/python

import Tkinter
from Tkinter import Label, Text, Scrollbar

"""		Event handler for key release events
"""
def onKeyReleased(event):
	print 'key released: ' + event.char

# Tkinter.Tk: Base class to inherit from for standard windows.
base = Tkinter.Tk()

"""		Title
"""
base.title("HTML Renderer")

"""		Window Label
"""
title = Label(base,
			text='A more interactive HTML coding environment!',
			font='Times 10 bold',
			fg='white',		# Text color
			bg='black',		# Text background color
			anchor='center')
title.pack()	# Fit the size of the window to text

"""		Text Box For User Input
"""
usrInput = Text(base,
			font='Times 14',
			fg='black',
			bg='white')
usrInput.pack(fill='y', padx=10, side='left')
usrScroll = Scrollbar(base)
usrScroll.pack(fill='y', side='left')
usrScroll.config(command=usrInput.yview)
usrInput.config(yscrollcommand=usrScroll.set)
# Bind user input text box to key release event
usrInput.bind('<KeyRelease>', onKeyReleased)

"""		Message Box to Reflect User Inputs
"""
output = Text(base,
			font='Times 14 bold',
			fg='black',
			bg='white')
outScroll = Scrollbar(base)
outScroll.pack(fill='y', side='right')
output.pack(fill='y', padx=10, side='right')
outScroll.config(command=output.yview)
output.config(yscrollcommand=outScroll.set)

# Display the window
base.mainloop()
