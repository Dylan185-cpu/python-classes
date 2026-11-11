#import nesccessary libraries 
from tkinter import *

# Create a window
window = Tk()
window.title("Event handler")
window.geometry("100x100")

# Event handler for KeyPress event
def handle_keypress(event):
    """Print the character associated to the key pressed."""
    print(event.char)

# Bind Keypress event to handle_keypress() function
window.bind("<Key>", handle_keypress)

#Event handler event for button click
def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack()

# Bind button click event to handle_click() function
button.bind("<Button-1>", handle_click)

# Start the GUI event loop
window.mainloop()