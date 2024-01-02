# Digital Clock in Python
# Resolving the naming conflict with the 'time' module

# Importing necessary libraries
from tkinter import Label, Tk
import time

# Function to update the time on the label
def update_time():
    string = time.strftime('%H:%M:%S %p')  # Format the time as hour:minute:second AM/PM
    lbl.config(text=string)
    lbl.after(1000, update_time)  # Time updates every 1000 milliseconds

# Setting up the main window
root = Tk()
root.title("Digital Clock")  # Title of the window

# Creating and styling the label
lbl = Label(root, font=('ds-digital', 40, 'bold'), background='black', foreground='cyan')

# Placing the label into the window
lbl.pack(anchor='center')

# Running the update_time function and main loop
update_time()
root.mainloop()
