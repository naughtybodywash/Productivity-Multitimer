# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:38:35 2020

@author: joshb
"""

# Import everything from Tkinter
from tkinter import *

# Set up the main graphical box =
root = Tk()

# Show the program name inside the window
root.title("Productivity Timers")
water = Label(root, text="Start Hydrate Timer")
water.grid()

# Set the size of the window
root.geometry('350x200') 

# Define hydrate button function
def hydration(): 
    messagebox.showinfo("Water", "Hydrate Now!!") 
    # Next line to be uncommented when the timer itself is built
    #water.configure(text="Hydration timer running...")

#Create hydrate button
btnH = Button(root, text="Start", command=hydration)

btnH.grid(column=1, row=0)

# Initialize the window and keep it open until we close it with "X" button
# Takes all widgets and objects, render them, and respond to interactions
root.mainloop()