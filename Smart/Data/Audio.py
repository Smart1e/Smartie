import tkinter as tk
import smartieJson as sj
root = tk.Tk()

micuse = tk.IntVar()
audiouse = tk.IntVar()
root.title('Audio settings')
photo = tk.PhotoImage(file = 'Icon.png')  
root.iconphoto(False, photo)

    
aud = tk.Checkbutton(root, text = "Would you like audio to be used by default?", variable = audiouse)
aud.grid(row=1, column=0, columnspan=4, pady=3)

micro = tk.Checkbutton(root, text = "Would you like microphone to be used by default?", variable = micuse)
micro.grid(row=2, column=0, columnspan=4, pady=3)


theme_accent = ['#00897B', '#FFC100', '#C6282B', '#673AB7']


def push_settings():
        sj.update("audio", str(audiouse.get()))
        sj.update("mic", str(micuse.get()))
        root.destroy()
        
def push_sure():
        sure.grid(row=10, column=0, columnspan=4, pady=3)
        enter.grid_remove()
        cancel.grid_remove()

enter = tk.Button(root, text='Enter', command=push_sure, width=15, background=theme_accent[0])
sure =  tk.Button(root, text='Are you sure?', command=push_settings, background=theme_accent[1], width=25)
cancel = tk.Button(root, text='Cancel', command=root.destroy, width=15, background=theme_accent[2])
enter.grid(row=10, column=2, columnspan=2, pady=3)
cancel.grid(row=10, column=0, columnspan=2, pady=3)




root.mainloop()
