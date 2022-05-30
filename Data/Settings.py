import tkinter as tk
import os
import subprocess
root = tk.Tk()
root.title('Settings Selection')
photo = tk.PhotoImage(file = 'Icon.png')  
root.iconphoto(False, photo)
    
audio = tk.Button(root, text='Audio settings', command=lambda: subprocess.Popen(['Audio.py'], shell=True, creationflags=subprocess.SW_HIDE)
audio.grid(row=0, column=0, columnspan=4, pady=3)



root.mainloop()
    


