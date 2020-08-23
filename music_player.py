# import tkinter as tk

# window = tk.Tk()
# window.title("Music Player")

# enter_your_Fname = tk.Label(master = window, text= "Enter your First Name").grid(row = 0, column = 0)

# text1 = tk.Entry(master = window,).grid(row = 0, column = 1)

# enter_your_Lname = tk.Label(master = window, text= "Enter your Last Name").grid(row = 1, column = 0)

# text1 = tk.Entry(master = window).grid(row = 1, column = 1)

# submit = tk.Button(master = window, text = 'Submit').grid(row = 2, column = 0)

# quit_button = tk.Button(text = 'Quit', command = window.quit).grid(row = 2, column = 1)

# bar = Progressbar()

# window.mainloop()

# importing tkinter module 
from tkinter import *
from tkinter.ttk import *

# creating tkinter window 
root = Tk() 

# Progress bar widget 
progress = Progressbar(root, orient = HORIZONTAL, 
			length = 100, mode = 'determinate') 

# Function responsible for the updation 
# of the progress bar value 
def bar(): 
	import time 
	progress['value'] = 20
	root.update_idletasks() 
	time.sleep(1) 

	progress['value'] = 40
	root.update_idletasks() 
	time.sleep(1) 

	progress['value'] = 50
	root.update_idletasks() 
	time.sleep(1) 

	progress['value'] = 60
	root.update_idletasks() 
	time.sleep(1) 

	progress['value'] = 80
	root.update_idletasks() 
	time.sleep(1) 
	progress['value'] = 100

progress.grid(row = 0, column = 0)

# This button will initialize 
# the progress bar 
Button(root, text = 'Start', command = bar).grid(row = 1, column = 0) 

# infinite loop
exit_button = Button(root, text = 'Quit', command = root.quit).grid(row = 1, column = 1)
mainloop()
