#To install Tkinter package
#sudo apt install python3-tkD

#one of the easiest widgets of Tk (Tkinter), i.e. a label.
#A Label is a Tkinter Widget class, which is used to display text or an image.
#The label is a widget that the user just views but not interact with.

from tkinter import *

#To initialize tkinter, we have to create a Tk root widget,
#which is a window with a title bar and other decoration provided by the window manager.
#The root widget has to be created before any other widgets and there can only be one root widget.

root = Tk()

#The first parameter of the Label call is the name of the parent window, in our case "root".So our Label widget is a child of the root widget
#The keyword parameter "text" specifies the text to be shown

w = Label(root, text="Hello Ayush!")

#The pack method tells Tk to fit the size of the window to the given text.

w.pack()

#The window won't appear until we enter the Tkinter event loop.

root.mainloop()

#Our script will remain in the event loop until we close the window.
