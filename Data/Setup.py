

try:
    import tkinter as tk
    import tkinter.ttk as ttk
    
except:
    import os
    from time import sleep
    modin1 = os.popen('pip install tkinter')
    if "'pip' is not recognized as an internal or external command" in str(modin1.read()):
        print('Python has not been installed correctly! Please go through the install (for python) again and make sure that you tick the boc to add python or pip to path')
        sleep(20)
        
else:
    from time import sleep
    root = tk.Tk()
    audiouse = tk.IntVar()
    micuse = tk.IntVar()
    passuse = 6
    passcode = False
    def finalize_details():
        global audiouse
        global micuse
        global passuse
        global passcode
        print(f'Audio {audiouse.get()}, Mic {micuse.get()}, Passused {passuse}, Passcode {passcode}.')
        
        
    #Themes formatted as [background, text, Window background]
    theme_dark = ['#1F2140', '#989BCD', '#121426']
    
    root.configure(bg=theme_dark[2])
    #root.geometry('400x200')
    root.title('Smartie Setup.')
    
    disclaim = tk.Entry(root, disabledbackground=theme_dark[0], disabledforeground=theme_dark[1], width=30)
    disclaim.insert(0, "All settings can be changed later!")
    disclaim.config(state='disabled')
    disclaim.grid(row=0, column=0, columnspan=4, pady=3)
    
    aud = tk.Checkbutton(root, text = "Would you like audio to be used by default?", variable = audiouse)
    aud.grid(row=1, column=0, columnspan=4, pady=3)
    
    micro = tk.Checkbutton(root, text = "Would you like microphone to be used by default?", variable = micuse)
    micro.grid(row=2, column=0, columnspan=4, pady=3)
    
    enter = tk.Button(root, text='Enter', command=finalize_details)
    enter.grid(row=5, column=2, columnspan=2, pady=3)
    

    
    root.mainloop()
    