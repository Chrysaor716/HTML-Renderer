#!/usr/bin/python

import Tkinter
from Tkinter import Label, Text, Scrollbar

# Constants
DEFAULT_FONT_SIZE = 14

"""		Event handler (callback) for key release events.
"""
# ThisisprobablysuperinefficientI'msorry #cringe
def onKeyReleased(event):
	# Clear output text box every time script runs this frame
	output.delete('1.0', 'end')

	# Get all text from the user text box
	text = usrInput.get('1.0', 'end')
	# Look for important characters and parse
	for index, char in enumerate(text):
		if text[index-1] == '>':
			# Check if it's a header tag
			if text[index-3] == 'h':
				# See if it's the opening or closing tag
				if text[index-4] == '/' and text[index-5] == '<': # If closing tag
					# Do not output the HTML tags
					# No switch/case in Python :(
					if text[index-2] == '1': # Header 1
						output.tag_add('h1', tagStart, output.index('end - 1 chars'))
						output.tag_config('h1', font='Times 32 bold')
						output.delete(output.index('end - 6 chars'), output.index('end - 1 chars'))
					elif text[index-2] == '2': # Header 2
						output.tag_add('h2', tagStart, output.index('end - 1 chars'))
						output.tag_config('h2', font='Times 26 bold')
						output.delete(output.index('end - 6 chars'), output.index('end - 1 chars'))
					elif text[index-2] == '3': # Header 3
						output.tag_add('h3', tagStart, output.index('end - 1 chars'))
						output.tag_config('h3', font='Times 19 bold')
						output.delete(output.index('end - 6 chars'), output.index('end - 1 chars'))
					elif text[index-2] == '4': # Header 4
						output.tag_add('h4', tagStart, output.index('end - 1 chars'))
						output.tag_config('h4', font='Times 16 bold')
						output.delete(output.index('end - 6 chars'), output.index('end - 1 chars'))
					elif text[index-2] == '5': # Header 5
						output.tag_add('h5', tagStart, output.index('end - 1 chars'))
						output.tag_config('h5', font='Times 13 bold')
						output.delete(output.index('end - 6 chars'), output.index('end - 1 chars'))
					elif text[index-2] == '6': # Header 6
						output.tag_add('h6', tagStart, output.index('end - 1 chars'))
						output.tag_config('h6', font='Times 10 bold')
						output.delete(output.index('end - 6 chars'), output.index('end - 1 chars'))
					else: 			   # Invalid character; "default" case
						print 'Subliminal messaging.'
				if text[index-4] == '<': # Opening tag
					output.delete(output.index('end - 5 chars'), output.index('end - 1 chars'))
					tagStart = output.index('end - 1 chars')		 # this one is the \n char
		output.insert('end', char)

# Tkinter.Tk: Base class to inherit from for standard windows.
base = Tkinter.Tk()
base.config(bg='black')

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
usrInput.pack(fill='both', expand='true', padx=10, side='left')
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
output.pack(fill='both', expand='true', padx=10, side='right')
outScroll.config(command=output.yview)
output.config(yscrollcommand=outScroll.set)

# Display the window
base.mainloop()
