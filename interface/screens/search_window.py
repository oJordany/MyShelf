from pathlib import Path
# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def generate_search_window():
    search_window = Tk()

    search_window.geometry("1300x700")
    search_window.configure(bg = "#2C0A59")

    def back_to_home():
        from interface.screens.homeWindow import HomeWindow
        search_window.destroy()
        novaHome = HomeWindow()
        novaHome.generate_home_window()

    canvas = Canvas(
        search_window,
        bg = "#2C0A59",
        height = 700,
        width = 1300,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_icon = PhotoImage(
        file=relative_to_assets("icon.png"))
    button_icon = Button(
        image=button_image_icon,
        borderwidth=0,
        highlightthickness=0,
        command=back_to_home,
        relief="flat",
        bd=0,
        bg="#2C0A59",
        activebackground="#2C0A59",
        cursor="hand2",
    )
    button_icon.place(
        x=1197.0,
        y=19.0,
    )

    image_image_search = PhotoImage(
        file=relative_to_assets("image_search.png"))
    
    canvas.create_image(
        339.0,
        59.0,
        image=image_image_search
    )

    image_image_isbn = PhotoImage(
        file=relative_to_assets("image_isbn.png"))
    
    canvas.create_image(
        151.0,
        129.0,
        image=image_image_isbn
    )

    entry_image_search = PhotoImage(
        file=relative_to_assets("entry_search.png"))
    
    canvas.create_image(
        207.5,
        180.5,
        image=entry_image_search
    )

    entry_search = Entry(
        bd=0,
        bg="#93679A",
        highlightthickness=0,
        justify="center",
        font=('Georgia 20')
    )

    entry_search.place(
        x=65.5,
        y=161.5,
        width=284.0,
        height=30.75,
    )

    button_image_search = PhotoImage(
        file=relative_to_assets("button_search.png"))
    button_search = Button(
        image=button_image_search,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_search clicked"),
        relief="sunken",
        cursor="hand2",
        activebackground="#2C0A59",
        bg="#2C0A59",
        bd=0,   
    )
    button_search.place(
        x=386.0,
        y=162.0,
        width=40.3193359375,
        height=37.80328369140625
    )
    search_window.resizable(False, False)
    search_window.mainloop()
