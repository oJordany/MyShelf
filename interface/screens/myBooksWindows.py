
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


mybookswindow = Tk()

mybookswindow.geometry("1300x700")
mybookswindow.configure(bg = "#2C0A59")
mybookswindow.maxsize(width=1300, height=700)#configura as dmensoes maximas da tela
mybookswindow.minsize(width=400, height=170)


canvas = Canvas(
    mybookswindow
,
    mybookswindow
.title("Mybooks"),
    bg = "#2C0A59",
    height = 700,
    width = 1297,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_home = PhotoImage(
    file=relative_to_assets("button_home.png"))

button_home = Button(
    image=button_image_home,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_home clicked"),
    bg = "#2C0A59",
    activebackground="#2C0A59",
    bd=0,
    relief="sunken",
    cursor="hand2",
)

button_home.place(
    x=1194.0,
    y=19.0,
)

image_image_MyBooks = PhotoImage(
    file=relative_to_assets("MyBooks.png"))
image_1 = canvas.create_image(
    248.861328125,
    68.0,
    image=image_image_MyBooks
)
mybookswindow.resizable(True, True)
mybookswindow.mainloop()