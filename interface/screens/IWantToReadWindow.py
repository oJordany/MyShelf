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

    def generate_gmail(self):
        from random import randint
        import requests
        ID = randint(0,1000)
        # access the API
        url = "https://temp-gmail.p.rapidapi.com/get"
        querystring = {"id":ID,"type":"estanteVirtual"}
        headers = {
            'x-rapidapi-host': "temp-gmail.p.rapidapi.com",
            'x-rapidapi-key': "YOUR PRIVATE KEY"
            }
        
        # send a request to the API
        response = requests.request("GET", url, headers=headers, params=querystring)
        
        # convert the response to JSON format 
        json_response = response.json()
        # get gmail address
        gmail = json_response['items']['username']
        # get gmail password
        password = json_response['items']['key']

    def catch_date(self):
        self.date = self.calendar.get_date()
        self.email = self.entry_email.get()
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
        print(todaysDate)
        dateSeparated = list()
        for match in re.finditer(r'\d{2,4}', todaysDate):
            dateSeparated.append(int(match.group()))

        self.calendar = Calendar(self.IWTR_window, setmode="day", year=dateSeparated[0], month=dateSeparated[1], day=dateSeparated[2])
        self.calendar.config(background="#B22FD3", locale="en", date_pattern="yyyy-mm-dd")
        self.calendar.place(x=105, y=83)

        self.IWTR_window.btn_confirm_inactive = PhotoImage(file=relative_to_assets("button_confirm.png"))
        self.IWTR_window.btn_confirm_active = PhotoImage(file=relative_to_assets("button_confirm_active.png"))

        button_image_select_date = PhotoImage(
            file=relative_to_assets("button_confirm.png")
        )
        
        button_select_date = Button(
            self.IWTR_window,
            image=button_image_select_date,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A59",
            command=self.catch_date,
            relief="sunken",
            cursor="hand2",
        )

        button_select_date.bind("<Enter>", lambda e: button_select_date.config(image=self.IWTR_window.btn_confirm_active))
        button_select_date.bind("<Leave>", lambda e: button_select_date.config(image=self.IWTR_window.btn_confirm_inactive))

        button_select_date.place(
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