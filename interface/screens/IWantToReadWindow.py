from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from turtle import bgcolor, mode
from webbrowser import BackgroundBrowser


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class IWantToReadWindow:

    def __init__(self):        
        self.IWTR_window = Toplevel()
        self.IWTR_window.title("I Want to Read")
        self.IWTR_window.geometry("530x292")
        self.IWTR_window.configure(bg = "#2C0A59")
        self.IWTR_window.maxsize(width=988, height=700)#configura as dmensoes maximas da tela
        self.IWTR_window.minsize(width=400, height=170)

    def get_date(self):
        self.date = self.calendar.get_date()

    def i_dont_know(self):
        self.date = "NULL"

    def generate_IWTR_window(self):
        from datetime import date
        from tkcalendar import Calendar
        import re
        canvas = Canvas(
            self.IWTR_window,
            bg = "#2C0A59",
            height = 270,
            width = 870,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        image_image_WTR= PhotoImage(
            file=relative_to_assets("WTR.png"))
        canvas.create_image(
            179.0,
            47.0,
            image=image_image_WTR
        )

        image_image_OR= PhotoImage(
            file=relative_to_assets("Or.png"))
        canvas.create_image(
            395.0,
            177.0,
            image=image_image_OR
        )

        canvas.place(x=0,y=0)
        
        todaysDate = str(date.today())
        print(todaysDate)
        dateSeparated = list()
        for match in re.finditer(r'\d{2,4}', todaysDate):
            dateSeparated.append(int(match.group()))

        self.calendar = Calendar(self.IWTR_window, setmode="day", year=dateSeparated[0], month=dateSeparated[1], day=dateSeparated[2])
        self.calendar.config(background="#B22FD3", locale="en", date_pattern="yyyy-mm-dd")
        self.calendar.place(x=40, y=100)

        self.IWTR_window.btn_IDKinactive = PhotoImage(file=relative_to_assets("button_IDK.png"))
        self.IWTR_window.btn_IDKactive = PhotoImage(file=relative_to_assets("button_IDKActive.png"))

        button_image_IDK = PhotoImage(
            file=relative_to_assets("button_IDK.png"))

        button_IDK = Button(
            self.IWTR_window,
            image=button_image_IDK,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A59",
            command=self.i_dont_know,
            relief="sunken",
            cursor="hand2",
        )
        
        button_IDK.bind("<Enter>", lambda e: button_IDK.config(image=self.IWTR_window.btn_IDKactive))
        button_IDK.bind("<Leave>", lambda e: button_IDK.config(image=self.IWTR_window.btn_IDKinactive))
        
        button_IDK.place(
            x=300,
            y=200,

        )

        self.IWTR_window.btn_select_date_inactive = PhotoImage(file=relative_to_assets("button_select_date_inactive.png"))
        self.IWTR_window.btn_select_date_active = PhotoImage(file=relative_to_assets("button_select_date.png"))

        button_image_select_date = PhotoImage(
            file=relative_to_assets("button_select_date_inactive.png")
        )
        
        button_select_date = Button(
            self.IWTR_window,
            image=button_image_select_date,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A59",
            command=self.get_date,
            relief="sunken",
            cursor="hand2",
        )

        button_select_date.bind("<Enter>", lambda e: button_select_date.config(image=self.IWTR_window.btn_select_date_active))
        button_select_date.bind("<Leave>", lambda e: button_select_date.config(image=self.IWTR_window.btn_select_date_inactive))

        button_select_date.place(
            x=300,
            y=100,
        )

        self.IWTR_window.resizable(False, False)
        self.IWTR_window.mainloop()