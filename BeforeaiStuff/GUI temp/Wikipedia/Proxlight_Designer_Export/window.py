from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("645x598")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 598,
    width = 645,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    322.5, 299.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    411.0, 50.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#49b5d8",
    highlightthickness = 0)

entry0.place(
    x = 259, y = 20,
    width = 304,
    height = 58)

window.resizable(False, False)
window.mainloop()
