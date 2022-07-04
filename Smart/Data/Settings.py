import tkinter as tk
import os
from Quick_fix import start_fix

#Themes formatted as [background, text, Window background, border colours]
theme_dark = ['#1F2140', '#989BCD', '#121426', '#1F2933']
theme_oled = ['#000011', '#BAE6D9', '#000000', '#102A43']
theme_pink = ['#923551', '#BAE6D9', '#451926', '#2E111A']
theme_accent = ['#00897B', '#FFC100', '#C6282B', '#673AB7']
theme_grey = ['#C9C9C9', '#252525', '#AFAFAF', '#2B2B2B']
    
root = tk.Tk()
root.title('Settings Selection')
photo = tk.PhotoImage(file = 'Icon.png')  
root.iconphoto(False, photo)
    
description = tk.Label(root, text='Select the settings you want to change.', font=('Arial', 12))
description.grid(row=0, column=1, columnspan=8)

audio = tk.Button(root, text='Audio settings', command=lambda: os.startfile('Audio.py'), width=20)
audio.grid(row=1, column=0, columnspan=4, pady=3)

quick_fix = tk.Button(root, text='Quick fix (source only)', command=start_fix, width=20)
quick_fix.grid(row=1, column=5, columnspan=4, pady=3)

exit = tk.Button(root, text='Save & exit', command=root.destroy, width=10, bg=theme_accent[2])
exit.grid(row=10, column=0, columnspan=4, pady=3)

load_smartie = tk.Button(root, text='Load Smartie', command=lambda: os.startfile('run.py'), width=10, bg="pink")
load_smartie.grid(row=10, column=5, columnspan=4, pady=3)

root.mainloop()
    


