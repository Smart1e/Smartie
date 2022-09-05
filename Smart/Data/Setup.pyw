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
    import chardet 
    
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
        from cryptography.fernet import Fernet
        global audiouse
        global micuse
        global passuse
        global passcode
        global username
        global theme
        global theme_oled
        global theme_dark
        global theme_pink
        
        '''#Encodes Passcode
        if passuse.get() == 1:
            codepass = passcode.get()
            codepass = codepass.encode()
            
            key = Fernet.generate_key()
            the_encoding = chardet.detect(key)['encoding']
            crypter = Fernet(key)
            pw = crypter.encrypt(codepass)
            passwrd = str(pw)
            passwrd.replace("b'", '');passwrd.replace("'", '')
            key_2 = key.decode("UTF-8")
            key_2 = str(key_2)
            final_key = key_2.replace("'", '')
            final_key = final_key.replace("b'", '')
            
            print(final_key)
            the_encoding = chardet.detect(key)['encoding']
            print(the_encoding)
        '''
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
                
                
            settings = {"system": system, "user": str(username.get()), "passUsed": str(passuse.get()), "password": str(passcode.get()), "audio": str(audiouse.get()), "mic": str(micuse.get()), "theme": final_theme}#, "key": final_key}
            myJSON = json.dumps(settings)
            
            with open(file, "w") as f:
                f.write(myJSON)
                

            sys.exit()
        else:
            sure.grid_remove()
            must_user.grid(row=20, column=0, columnspan=4, pady=3)  
            
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
    theme_grey = ['#C9C9C9', '#252525', '#AFAFAF', '#2B2B2B']
    theme = theme_grey

    #root.geometry('400x200')username
    root.title('Smartie Setup.')
    root.configure(background=theme[2])
    
    disclaim = tk.Entry(root, width=30, disabledbackground=theme[0], disabledforeground=theme[1])
    disclaim.insert(0, "All settings can be changed later!")
    disclaim.config(state='disabled')
    disclaim.grid(row=0, column=0, columnspan=4, pady=3)
    
    aud = tk.Checkbutton(root, text = "Would you like audio to be used by default?", variable = audiouse, bg=theme[0], fg=theme[1])
    aud.grid(row=1, column=0, columnspan=4, pady=3)
    
    micro = tk.Checkbutton(root, text = "Would you like microphone to be used by default?", variable = micuse, bg=theme[0], fg=theme[1])
    micro.grid(row=2, column=0, columnspan=4, pady=3)

    ask_user_tell = tk.Entry(root, width=33, disabledbackground=theme[0], disabledforeground=theme[1])
    ask_user_tell.insert(0, "Please enter a Username underneath.")
    ask_user_tell.config(state='disabled')
    ask_user_tell.grid(row=3, column=0, columnspan=4, pady=3)
    
    ask_user = tk.Entry(root, textvariable=username, bg=theme[0], fg=theme[1])
    ask_user.grid(row=4, column=0, columnspan=4, pady=3)
    
    ask_pass_tell = tk.Checkbutton(root, text="Please enter a Password underneath, unless you are not using one.",variable=passuse, width=58, command=passcomm, bg=theme[0], fg=theme[1])
    ask_pass_tell.grid(row=5, column=0, columnspan=4, pady=3)
    
    ask_pass = tk.Entry(root, textvariable=passcode, show='*', bg=theme[0], fg=theme[1])
    
    def theme_press(num):
        global theme
        global theme_dark
        global theme_pink
        global theme_oled
        global theme_grey
        
        if num == 0:
            theme = theme_dark
            tick.grid(row=7)
        elif num == 1:
            theme = theme_oled
            tick.grid(row=8)
        elif num == 2:
            theme = theme_pink
            tick.grid(row=9)
        elif num == 3:
            theme = theme_grey
            tick.grid(row=10)
        
    theme_check_dark = tk.Button(root, text='Dark theme', width=14, command=lambda: theme_press(0),background=theme_dark[0], foreground=theme_dark[1])
    theme_check_dark.grid(row=7, column=0, columnspan=4, pady=3)

    
    theme_check_oled = tk.Button(root, text='Oled theme', width=14, command=lambda: theme_press(1), background=theme_oled[0], foreground=theme_oled[1])
    theme_check_oled.grid(row=8, column=0, columnspan=4, pady=3)
    
    theme_check_pink = tk.Button(root, text='Pink theme', width=14, command=lambda: theme_press(2), background=theme_pink[0], foreground=theme_pink[1])
    theme_check_pink.grid(row=9, column=0, columnspan=4, pady=3)

    theme_check_grey = tk.Button(root, text='Grey theme', width=14, command=lambda: theme_press(3), background=theme_grey[0], foreground=theme_grey[1])
    theme_check_grey.grid(row=10, column=0, columnspan=4, pady=3)
    
    def push_sure():
        sure.grid(row=20, column=0, columnspan=4, pady=3)
        enter.grid_remove()
        must_user.grid_remove()
        
        
    enter = tk.Button(root, text='Enter', command=push_sure, width=50, background=theme_accent[0])
    sure =  tk.Button(root, text='Are you sure?', command=finalize_details, background=theme_accent[1], width=50)
    must_user = tk.Button(root, text='Please enter a username!', command=push_sure, width=50, background=theme_accent[2])
    enter.grid(row=20, column=0, columnspan=4, pady=3)   
    
    tick = tk.Label(root, text='☑', bg=theme_accent[0], fg='#000000', font=('windings', '12'))
    tick.grid(row=10, column=2, columnspan=4, pady=5)
    
     
    root.mainloop()