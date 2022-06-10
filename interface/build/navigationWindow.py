from pathlib import Path

from tkinter import *
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from turtle import window_width
from urllib.parse import unquote_to_bytes

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def generate_navigation_window():

    navigation_window = Tk()

    navigation_window.geometry("1300x700")
    navigation_window.configure(bg = "#2C0A59")


    canvas = Canvas(
        navigation_window,
        bg = "#2C0A59",
        height = 700,
        width = 1300,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    Logo_image = PhotoImage(
        file=relative_to_assets("Icon.png"))
    Logo = canvas.create_image(
        1250.0,
        60.0,
        image=Logo_image
    )



    navigation_window.resizable(False, False)
    navigation_window.mainloop()
