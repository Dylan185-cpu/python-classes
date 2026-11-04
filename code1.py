# iMPORT NECESSARY LIBRARIES
from tkinter import *
from datetime import date

# Create window
root = Tk()# Tk class from tkinter, create a window

#set the window title and geometry
root.title('Getting started with widgets')#title of window
root.geometry('400x300')#size of window, X and Y axis

# Add widgets
#Add a label widget
lbl = Label(root, text='0Hey There!', fg="white", bg="#072F5F", height=1, width=300)
# placement method
lbl.pack()
#Add Label for getting name input from user
# Use Entry widget to create a text box for user input
name_lbl = Label(root, text="Full name", bg="#3895D3")
name_entry = Entry(root)
name_lbl.pack()
name_entry.pack()
#Function to display message
def display():
    # read input given by user
    name = name_entry.get()
    #delclaring deatails in a textbox
    #to make it accessible anywhere in the program
    global message
    message = "We;" \
    "lcome to the Application! \nToday's date is: "
    greet = "Hello "+ name+"\n"
    #Display details in a textbox
    #Specify where to add the details inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

#Add a text widget to display the message
text_box = Text(height=3, width=50)

#Add button and give value of command as name of the function
# press button, display function will be called automatically
btn = Button(root, text="BEGIN", command=display, height=1, bg="#1261A0", fg="white")
btn.pack()
text_box.pack()


# Start the GUI event loop
root.mainloop()