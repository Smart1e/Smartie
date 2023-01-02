from tkinter import *
import tkinter as tk
import os
import sys


def btn_clicked():
    print("Button Clicked")

'''Items to add:
-password changes
-user name changes
-theme changes
'''

window = Tk()
photo = tk.PhotoImage(file = 'Icon.png')  
window.iconphoto(False, photo)
window.geometry("1585x1080")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1585,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"settings_background.png")
background = canvas.create_image(
    668.5, 681.5,
    image=background_img)

img0 = PhotoImage(file = f"settings_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: os.startfile('Audio.pyw'),
    relief = "flat")

b0.place(
    x = 1185, y = 44,
    width = 377,
    height = 109)

img1 = PhotoImage(file = f"settings_img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: os.startfile('Password.pyw'),
    relief = "flat")

b1.place(
    x = 1185, y = 205,
    width = 377,
    height = 109)

img2 = PhotoImage(file = f"settings_img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = sys.exit,
    relief = "flat")

b2.place(
    x = 1185, y = 939,
    width = 377,
    height = 109)

img3 = PhotoImage(file = f"settings_img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = sys.exit,
    relief = "flat")

b3.place(
    x = 1185, y = 778,
    width = 377,
    height = 109)

window.resizable(False, False)
window.mainloop()
