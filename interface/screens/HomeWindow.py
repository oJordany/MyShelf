from pathlib import Path
# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from turtle import window_width
from urllib.parse import unquote_to_bytes


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class HomeWindow:
    def __init__(self):
        self.home_window = Tk()

        self.home_window.geometry("1300x700")
        self.home_window.configure(bg = "#2C0A59")


    def change_window(self):
        from interface.screens.MenuWindow import MenuWindow
        self.home_window.destroy()
        self.menu_window = MenuWindow()
        self.menu_window.generate_menu_window()

        
    def generate_home_window(self):

        canvas = Canvas(
            self.home_window,
            bg = "#2C0A59",
            height = 700,
            width = 1300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)

        self.home_window.button_home_active = PhotoImage(
            file=relative_to_assets("button_home.png"))
        self.home_window.button_home_inactive = PhotoImage(
            file=relative_to_assets("button_home_inactive.png"))

        button_home_image = PhotoImage(
            file=relative_to_assets("button_home_inactive.png"))
            
        button_home = Button(
            image=button_home_image,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            relief="sunken",
            cursor="hand2",
            activebackground="#2C0A59",
            command=self.change_window,
        )

        button_home.place(
            x=338.0,
            y=180.0,
        )

        button_home.bind("<Enter>", lambda e: button_home.config(image=self.home_window.button_home_active))
        button_home.bind("<Leave>", lambda e: button_home.config(image=self.home_window.button_home_inactive))

        image_image_reading = PhotoImage(
            file=relative_to_assets("image_reading.png"))
        
        canvas.create_image(
            650.0,
            561.0,
            image=image_image_reading
        )


        self.home_window.resizable(False, False)
        self.home_window.mainloop()
