#!/usr/bin/python

import Tkinter
from Tkinter import Label, Text, Scrollbar

"""		Event handler (callback) for key release events.
"""
# ThisisprobablysuperinefficientI'msorry #cringe
def onKeyReleased(event):
	# Get all text from the user text box
	text = usrInput.get('1.0', 'end')
	# Look for important characters and parse
	for index, char in enumerate(text):
		if char == '>':
			# See if it's the opening or closing tag
			if text[index-3] == '/': # If closing tag
				# No switch/case in Python :(
				if text[index-1] == '1': # Header 1
					print '32pt'
				elif text[index-1] == '2': # Header 2
					print '24pt'
				elif text[index-1] == '3': # Header 3
					print '19pt'
				elif text[index-1] == '4': # Header 4
					print '16pt'
				elif text[index-1] == '5': # Header 5
					print '13pt'
				elif text[index-1] == '6': # Header 6
					print '10pt'
				else: 			   # Invalid character
					print 'Do nothing; keep at default font size'

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
