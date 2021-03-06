from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from webbrowser import BackgroundBrowser


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class IWantToReadWindow:

    def __init__(self):        
        self.IWTR_window = Toplevel()
        icon = PhotoImage(file=relative_to_assets("Logo.png"))
        self.IWTR_window.iconphoto(False, icon)
        self.IWTR_window.title("I Want to Read")
        self.IWTR_window.geometry("460x445")
        self.IWTR_window.configure(bg = "#2C0A59")

    def set_email_notification(self, event):
        import re
        self.email = self.entry_email.get()
        self.username = re.sub(r'@[\w\d\.]+', '', self.email)



    def catch_date(self):
        self.date = self.calendar.get_date()
        self.IWTR_window.destroy()

    def generate_IWTR_window(self):
        from datetime import date
        from tkcalendar import Calendar
        import re
        canvas = Canvas(
            self.IWTR_window,
            bg = "#2C0A59",
            height = 445,
            width = 460,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        image_image_IWTRin= PhotoImage(
            file=relative_to_assets("IWTRin.png"))
        canvas.create_image(
            227.0,
            47.0,
            image=image_image_IWTRin
        )

        canvas.place(x=0,y=0)
        
        todaysDate = str(date.today())
        dateSeparated = list()
        for match in re.finditer(r'\d{2,4}', todaysDate):
            dateSeparated.append(int(match.group()))

        self.calendar = Calendar(self.IWTR_window, setmode="day", year=dateSeparated[0], month=dateSeparated[1], day=dateSeparated[2])
        self.calendar.config(background="#B22FD3", locale="en", date_pattern="yyyy-mm-dd")
        self.calendar.place(x=105, y=83)

        self.IWTR_window.btn_confirm_inactive = PhotoImage(file=relative_to_assets("button_confirm.png"))
        self.IWTR_window.btn_confirm_active = PhotoImage(file=relative_to_assets("button_confirm_active.png"))

        button_image_confirm = PhotoImage(
            file=relative_to_assets("button_confirm.png")
        )
        
        button_confirm = Button(
            self.IWTR_window,
            image=button_image_confirm,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A59",
            command=self.catch_date,
            relief="sunken",
            cursor="hand2",
        )

        button_confirm.bind("<Enter>", lambda e: button_confirm.config(image=self.IWTR_window.btn_confirm_active))
        button_confirm.bind("<Leave>", lambda e: button_confirm.config(image=self.IWTR_window.btn_confirm_inactive))
        button_confirm.bind("<Button-1>", self.set_email_notification)
        button_confirm.place(
            x=127,
            y=360,
        )

        image_image_ETRRN= PhotoImage(
            file=relative_to_assets("ETRRN.png"))
        canvas.create_image(
            230.0,
            282,
            image=image_image_ETRRN
        )

        entry_image_email = PhotoImage(
            file=relative_to_assets("entry_search.png"))
        
        canvas.create_image(
            230,
            320,
            image=entry_image_email
        )

        self.entry_email = Entry(
            self.IWTR_window,
            bd=0,
            bg="#93679A",
            highlightthickness=0,
            justify="center",
            font=('Georgia 20')
        )

        self.entry_email.place(
            x=55,
            y=300.5,
            width=350.0,
            height=30.75,
        )

        self.IWTR_window.resizable(False, False)
        self.IWTR_window.mainloop()