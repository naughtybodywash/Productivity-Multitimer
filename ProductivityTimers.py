# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:38:35 2020

@author: joshb
"""

# Import packages
import threading
from tkinter import *
import datetime as dt
import time
import winsound

# Set up the main graphical box =
root = Tk()

# Show the program name inside the window
root.title("Productivity Timers")
water = Label(root, text="Start Hydrate Timer")
water.grid()
pom = Label(root, text="Start Pomodoro Timer")
pom.grid()

# Set the size of the window
root.geometry('350x200') 

# Define hydrate button function
def hydration(): 
    messagebox.showinfo("Water", "Hydrate Now!!") 
    # Next line to be uncommented when the timer itself is built
    water.configure(text="Hydration timer running...")
    
# Define pomodoro button function
def pomodoro(): 
    # Create time variables
    t_now = dt.datetime.now()
    t_pom = 25*60
    t_delta = dt.timedelta(0, t_pom)
    t_run = t_now + t_delta
    t_brk = 5*60
    t_pomend = t_now + dt.timedelta(0, t_pom + t_brk)
    
    #Messagebox
    pom.configure(text="Timer running...")
    
    total_pomodoros = 0
    breaks = 0
    # Pomodoro loop
    while True:
        # Pomodoro clock running
        if t_now < t_run:
            print("Pomodoro")
        elif t_delta <- t_now <- t_pomend:
            # ring a bell if it's the first time here
            print("In break")
            if breaks == 0:
                pom.configure(text=("On break!!!"))
                # annoying bell
                for i in range(5):
                    winsound.Beep((i+100), 700)
                print("Break time!")
                breaks += 1
        #Pomodoro and break are completed
        else: 
            print("Finished!")
            # Reset breaks
            breaks = 0
            # Let user know that break is over
            for i in range(10):
                winsound.Beep((i+100), 500)
            # Ask if user wants to start again
            usr_ans = messagebox.askyesno("Pomodoro Finished!", "Would you like to start another?")
            total_pomodoros += 1
            if usr_ans == True:
                #user wants to do another pomodoro. Reset timers
                t_now = dt.datetime.now()
                t_delta = dt.timedelta(0, t_pom)
                t_pomend = t_now + dt.timedelta(0, t_pom + t_brk)
                continue
            elif usr_ans == False:
                #user done...display stats
                messagebox.showinfo("Pomodoro finished!", "\nYou completed"+
                                    str(total_pomodoros)+ " pomodoros today!")
                break
        #Check every 20 seconds and update current time
        print('sleeping')
        time.sleep(20)
        t_now = dt.datetime.now()
        timenow = t_now.strftime("%H:%M")

# Create a separate thread for the pomodoro timer
def start_pom_thread(event):
    global pom_thread
    pom_thread = threading.Thread(target=pomodoro)
    pom_thread.daemon = True
    #progressbar.start()
    pom_thread.start()


#Create hydrate button
btnH = Button(root, text="Start", command=hydration)
btnP = Button(root, text="Start", command=lambda:start_pom_thread(None))

btnH.grid(column=1, row=0)
btnP.grid(column=1, row=1)

# Initialize the window and keep it open until we close it with "X" button
# Takes all widgets and objects, render them, and respond to interactions
root.mainloop()