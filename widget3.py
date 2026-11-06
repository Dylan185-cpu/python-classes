#Import nessary libraries
from tkinter import *

#create a window
root = Tk()
root.title('Login app')
root.geometry('400x400')

# Create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

# Add widgets
#Add a label widget
lbl1 = Label(frame, text = "Full Name: ", bg="#3895D3", fg="white", width=12)
lbl2 = Label(frame, text = "Email ID: ", bg="#3895D3", fg="white", width=12)
lbl3 = Label(frame, text = "Enter Password: ", bg="#3895D3", fg="white", width=12)

#Use entry Widgret to create a text box for user to eneter details
name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="*")

# Function to display message
def display():
    name = name_entry.get()
    greet = "Hello "+ name
    message = "\ncongratulations for your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

#text widget to display the message
textbox = Text(bg="#BEBEBE", fg="black")   

#add button, when pressed, meaage will be displayed in the text box
btn = Button(text ="Create Account", command=display, bg="red")

#arrange all widgets
frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
password_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

# Start the GUI event loop
root.mainloop()