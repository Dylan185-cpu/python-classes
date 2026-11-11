# Import nessary libraries
from tkinter import *
from tkinter import messagebox

# setup Tkinter window
root = Tk()
root.geometry("200x200")

# Function to display Warning message
# This wil be called once the button is clicked
# messagebox.showwarning("window Name", "Text to be displayed")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding a button to the window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

# Enter the main event loop
root.mainloop()