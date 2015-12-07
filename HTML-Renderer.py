#!/usr/bin/python

import Tkinter
from Tkinter import Label, Text, Scrollbar

# Constants
DEFAULT_FONT_SIZE = 14

"""		Event handler (callback) for key release events.
"""
# ThisisprobablysuperinefficientI'msorry #cringe
def onKeyReleased(event):
	tagStart = 0	# Start of index for syntax highlighting
#	insertChar = 1	# Boolean to prevent insertting HTML tags
	# Clear output text box every time script runs this frame
	output.delete('1.0', 'end')
	
	# Get all text from the user text box
	text = usrInput.get('1.0', 'end')
	# Look for important characters and parse
	for index, char in enumerate(text):
#		# Check whether or not user is typing an HTML tag
#		if char == '>':
#			if text[index-2] == 'h': # Header tags have an extra char
#				if text[index-3] == '<' or text[index-3] == '/':
#					insertChar = 0
#			elif text[index-1] == 'p': # Paragraph tag
#				if text[index-2] == '<' or text[index-2] == '/':
#					insertChar = 0
#			else:
#				insertChar = 1

		if text[index-1] == '>':
			# Check if it's a header tag
			if text[index-3] == 'h':
				# See if it's the opening or closing tag
				if text[index-4] == '/': # If closing tag
					# No switch/case in Python :(
					if text[index-2] == '1': # Header 1
						print 'font 32pt'
#						output.tag_config('h1', font='Times 32 bold')
#						output.tag_add('h1', 'tagStart', 'index')
					elif text[index-2] == '2': # Header 2
						print '24pt'
					elif text[index-2] == '3': # Header 3
						print '19pt'
					elif text[index-2] == '4': # Header 4
						print '16pt'
					elif text[index-2] == '5': # Header 5
						print '13pt'
					elif text[index-2] == '6': # Header 6
						print '10pt'
					else: 			   # Invalid character
						print 'Subliminal messaging.'
				#if text[index-4] == '<': # Opening tag
				#	tagStart = index

#		if insertChar == 1:
		output.insert('end', char)

# Tkinter.Tk: Base class to inherit from for standard windows.
base = Tkinter.Tk()

"""		Title
"""
base.title("HTML Renderer")

"""		Window Label
"""
title = Label(base,
			text='A more interactive HTML coding environment!\nPlease type your code in the left text box.',
			font='Times 10 bold',
			fg='white',		# Text color
			bg='black',		# Text background color
			anchor='center')
title.pack()	# Fit the size of the window to text

"""		Text Box For User Input
"""
usrInput = Text(base,
			font=('Times', DEFAULT_FONT_SIZE),
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
			font='Times',
			fg='black',
			bg='white')
outScroll = Scrollbar(base)
outScroll.pack(fill='y', side='right')
output.pack(fill='y', padx=10, side='right')
outScroll.config(command=output.yview)
output.config(yscrollcommand=outScroll.set)

# Display the window
base.mainloop()
