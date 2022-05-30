import tkinter as tk
from time import sleep
import os
import requests
import sys
import tkinter.filedialog as filedialog
root = tk.Tk()
photo = tk.PhotoImage(file = 'Icon.png')  
root.iconphoto(False, photo) 
root.geometry("500x500")
install = tk.Button(root, text='Install')


path = tk.StringVar()

def browsefunc():
    filename = filedialog.askdirectory(parent=root,initialdir="/",title='Please select an install location')
    print(filename)
    
browsebutton = tk.Button(root, text='Select install location.', command=browsefunc)
browsebutton.grid(row=0)

install.grid(row=1)
#install a repo from git hub
def install():
    
    url = "https://api.github.com/repos/Smart1e/Smartie/releases/assets/id"
    local_filename = "name_file.zip"
    headers = {
        "Accept": "application/octet-stream",
        "Authorization": "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"
    }
    with requests.get(url, headers=headers, stream=True) as r:# Important the stream=True flag
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    
root.mainloop()