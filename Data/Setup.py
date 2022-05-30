try:
    import tkinter as tk
    import tkinter.ttk as ttk
    import json
except:
    import os
    from time import sleep
    modin1 = os.popen('pip install tkinter')
    if "'pip' is not recognized as an internal or external command" in str(modin1.read()):
        print('Python has not been installed correctly! Please go through the install (for python) again and make sure that you tick the boc to add python or pip to path')
        sleep(20)
        
else:
    from time import sleep
    import os
    import sys
    
    
    root = tk.Tk()
    audiouse = tk.IntVar()
    micuse = tk.IntVar()
    passuse = tk.IntVar()
    passcode = tk.StringVar()
    username = tk.StringVar()
    theme_select = 'dark'
    photo = tk.PhotoImage(file = 'Icon.png')  
    root.iconphoto(False, photo) 
    
    def finalize_details(file='settings.json'):
        global audiouse
        global micuse
        global passuse
        global passcode
        global username
        global theme
        global theme_oled
        global theme_dark
        global theme_pink
        
        if username.get() != '':
            theme_check_pink.grid_remove();theme_check_oled.grid_remove();theme_check_dark.grid_remove();must_user.grid_remove();sure.grid_remove();enter.grid_remove();disclaim.grid_remove();aud.grid_remove();micro.grid_remove();ask_user_tell.grid_remove();ask_user.grid_remove();ask_pass_tell.grid_remove();ask_pass.grid_remove()
            if os.name == 'nt':
                #Windows
                system = '2'
                
            if os.name == 'posix':
                #Mac or Linux
                system = '1'
                
            if os.name != 'posix' and os.name == 'nt':
                #Unable to find an os name
                system = '0'
                
            
            if theme == theme_dark:
                final_theme = 'dark'
                
            elif theme == theme_oled:
                final_theme = 'oled'
                
            else:
                final_theme = 'pink'
                
                
            settings = {"system": system, "user": str(username.get()), "passUsed": str(passuse.get()), "password": str(passcode), "audio": str(audiouse.get()), "mic": str(micuse.get()), "theme": final_theme}
            myJSON = json.dumps(settings)
            print(f'Audio {audiouse.get()}, Mic {micuse.get()}, Passused {passuse.get()}, Passcode {passcode.get()}, the system is {system}, username is {username.get()}.')
            with open(file, "w") as f:
                f.write(myJSON)
                

            sys.exit()
        else:
            sure.grid_remove()
            must_user.grid(row=10, column=0, columnspan=4, pady=3)  
            
    def passcomm():
        global passuse
        global ask_pass
        if passuse.get() == 1 or passuse.get()== '1':
            ask_pass.grid(row=6, column=0, columnspan=4, pady=3)
        else:
            ask_pass.grid_remove()
    #Themes formatted as [background, text, Window background, border colours]
    theme_dark = ['#1F2140', '#989BCD', '#121426', '#1F2933']
    theme_oled = ['#000011', '#BAE6D9', '#000000', '#102A43']
    theme_pink = ['#923551', '#BAE6D9', '#451926', '#2E111A']
    theme_accent = ['#00897B', '#FFC100', '#C6282B', '#673AB7']
    theme = theme_pink

    #root.geometry('400x200')
    root.title('Smartie Setup.')
    
    disclaim = tk.Entry(root, width=30)
    disclaim.insert(0, "All settings can be changed later!")
    disclaim.config(state='disabled')
    disclaim.grid(row=0, column=0, columnspan=4, pady=3)
    
    aud = tk.Checkbutton(root, text = "Would you like audio to be used by default?", variable = audiouse)
    aud.grid(row=1, column=0, columnspan=4, pady=3)
    
    micro = tk.Checkbutton(root, text = "Would you like microphone to be used by default?", variable = micuse)
    micro.grid(row=2, column=0, columnspan=4, pady=3)

    ask_user_tell = tk.Entry(root, width=33)
    ask_user_tell.insert(0, "Please enter a Username underneath.")
    ask_user_tell.config(state='disabled')
    ask_user_tell.grid(row=3, column=0, columnspan=4, pady=3)
    
    ask_user = tk.Entry(root, textvariable=username)
    ask_user.grid(row=4, column=0, columnspan=4, pady=3)
    
    ask_pass_tell = tk.Checkbutton(root, text="Please enter a Password underneath, unless you are not using one.",variable=passuse, width=58, command=passcomm)
    ask_pass_tell.grid(row=5, column=0, columnspan=4, pady=3)
    
    ask_pass = tk.Entry(root, textvariable=passcode, show='*')
    
    def theme_press(num):
        global theme
        global theme_dark
        global theme_pink
        global theme_oled
        
        if num == 0:
            theme = theme_dark
        elif num == 1:
            theme = theme_oled
        elif num == 2:
            theme = theme_pink
        
    theme_check_dark = tk.Button(root, text='Dark theme', command=lambda: theme_press(0),background=theme_dark[0], foreground=theme_dark[1])
    theme_check_dark.grid(row=7, column=0, columnspan=4, pady=3)

    
    theme_check_oled = tk.Button(root, text='Oled dark theme', command=lambda: theme_press(1), background=theme_oled[0], foreground=theme_oled[1])
    theme_check_oled.grid(row=8, column=0, columnspan=4, pady=3)
    
    theme_check_pink = tk.Button(root, text='Pink theme', command=lambda: theme_press(2), background=theme_pink[0], foreground=theme_pink[1])
    theme_check_pink.grid(row=9, column=0, columnspan=4, pady=3)

    def push_sure():
        sure.grid(row=10, column=0, columnspan=4, pady=3)
        enter.grid_remove()
        must_user.grid_remove()
        
        
    enter = tk.Button(root, text='Enter', command=push_sure, width=50, background=theme_accent[0])
    sure =  tk.Button(root, text='Are you sure?', command=finalize_details, background=theme_accent[1], width=50)
    must_user = tk.Button(root, text='Please enter a username!', command=push_sure, width=50, background=theme_accent[2])
    enter.grid(row=10, column=0, columnspan=4, pady=3)   
    
     
    root.mainloop()
    
