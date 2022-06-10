from pathlib import Path
from navigationWindow import generate_navigation_window
# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from turtle import window_width
from urllib.parse import unquote_to_bytes


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def change_window():
    home_window.destroy()
    generate_navigation_window()
    

home_window = Tk()

home_window.geometry("1300x700")
home_window.configure(bg = "#2C0A59")


canvas = Canvas(
    home_window,
    bg = "#2C0A59",
    height = 700,
    width = 1300,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

home_window.btn_inactive = PhotoImage(file=relative_to_assets("button_1.png"))
home_window.btn_active = PhotoImage(file=relative_to_assets("ButtonActive.png"))

canvas.place(x = 0, y = 0)

def on_enter(event):
    button_1.config(image=home_window.btn_active)

def on_leave(event):
    button_1.config(image=home_window.btn_inactive)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg="#2C0A59",
    bd=0,
    relief="sunken",
    cursor="hand2",
    activebackground="#2C0A59",
    command=change_window,
)
button_1.place(
    x=338.0,
    y=180.0,
)

button_1.bind("<Enter>", on_enter)
button_1.bind("<Leave>", on_leave)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    650.0,
    561.0,
    image=image_image_1
)



home_window.resizable(False, False)
home_window.mainloop()
