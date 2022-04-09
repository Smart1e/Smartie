try:
    import tkinter as tk
    
except:
    import os
    from time import sleep
    modin1 = os.popen('pip install tkinter')
    if "'pip' is not recognized as an internal or external command" in str(modin1.read()):
        print('Python has not been installed correctly! Please go through the install (for python) again and make sure that you tick the boc to add python or pip to path')
        sleep(20)
        
else:
    #Themes formatted as [background, text]
    theme_dark = ['#1F2140', '#401F31']
    root = tk.Tk()
    root.title('Smartie Setup.')
    
    disclaim = tk.Entry(root, disabledbackground=theme_dark[0], disabledforeground=theme_dark[1], state='disabled')
    disclaim.insert(0, "All settings can be changed later!")
    disclaim.pack()
    aud = tk.Checkbutton(root, text = "Would you like audio to be used by default?")
    aud.pack()
    
    
    
    root.mainloop()