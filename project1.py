# Import necessary libraries
from tkinter import *
from datetime import date
 
#  Create the main window
root = Tk()
root.title("Greeting")
root.geometry("400x300")
 
#  Create the heading label
heading = Label(
    text="Workshop Welcome  to the widget workshop!",
    fg="white",
    bg="#072F5F",
    height=1,
    width=300
)
 
#  Create a label and Entry widget
name_label = Label(
    text="Participant Name",
    bg="#3895D3"
)
name_entry = Entry()
 
# PART 4: Create the display function
def display_hi():
    # Read the participant's name from the Entry widget
    name = name_entry.get()
 
    # Create the multi-line welcome message
    greeting = "HI " + name + "!\n"
    message = "Welcome to the widget workshop!\n"
    workshop_date = "Date: " + str(date.today())
 
    # Insert the message into the Text widget
    text_box.insert(END, greeting)
    text_box.insert(END, message)
    text_box.insert(END, workshop_date)
 
#Create the Text widget
text_box = Text(
    height=4,
    width=40
)
 
#  Create the button and connect its command
welcome_button = Button(
    text="Check In",
    command=display_hi,
    height=1,
    bg="#5B88AD",
    fg="white"
)
 
#  Arrange the widgets
heading.pack()
name_label.pack(pady=10)
name_entry.pack()
welcome_button.pack(pady=10)
text_box.pack()
 
# Start the Tkinter event loop
root.mainloop()
