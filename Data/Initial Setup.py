import tkinter as tk
from time import sleep
import os
import sys
import tkinter.filedialog as filedialog
root = tk.Tk()
photo = tk.PhotoImage(file = 'Icon.png')  
root.iconphoto(False, photo) 

install = tk.Button(root, text='Install')
root.withdraw()

path = tk.StringVar()

def browsefunc():
    filename = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    print(filename)
    
browsebutton = tk.Button(root, text='Select install location.', command=lambda: print(filedialog.askdirectory(parent=root,initialdir="/",title='Please select an install location')))
browsebutton.pack()
#install a repo from git hub
def install():
    #
    print()
    
root.mainloop()