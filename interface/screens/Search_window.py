from email.mime import image
from itertools import count
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scrollbar, font, Label, ttk, LEFT, BOTTOM, RIGHT, TOP, X, Y, StringVar, FLAT
from typing import final
import webbrowser
import asyncio
from numpy import size
from controller.request import request, request_google_books
from PIL import Image, ImageTk
from urllib.request import urlopen

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SearchWindow:

    def __init__(self):
        self.search_window = Tk()
        icon = PhotoImage(file=relative_to_assets("Logo.png"))
        self.search_window.iconphoto(False, icon)
        self.search_window.title("Search")
        self.search_window.geometry("1300x700")
        self.search_window.configure(bg = "#2C0A59")

    def back_to_home(self):
        from interface.screens.HomeWindow import HomeWindow
        self.search_window.destroy()
        self.novaHome = HomeWindow()
        self.novaHome.generate_home_window()

    def open_url(self, url):
        webbrowser.open_new(url)
        #lambda url="google.com": self.open_url(url)

    def renders_infos_book(self, books):
        counter = 1
        for book in books:
            if counter == 1:
                frame = ttk.LabelFrame(self.search_window, width=170, height=180)
                frame.place(x=160, y=230)
            elif counter == 5:
                frame = ttk.LabelFrame(self.search_window, width=170, height=180)
                frame.place(x=160, y=450)
            else:
                if counter > 1 and counter < 5:
                    x = 160 + ((counter-1) * 320)
                    y = 230
                else:
                    x = 160 + ((counter - 5) * 320)
                    y = 450
                frame = ttk.LabelFrame(self.search_window, width=180, height=180)
                frame.place(x=x, y=y)
            counter += 1 
        # try:
        #     self.labelTitle = Label(self.search_window, text=book["title"], relief=FLAT, background="#2C0A59", foreground="white", font=("Georgia 6 bold"))
        #     self.labelTitle.place(x=160, y=230)
        # except:
        #     pass
        # try:
        #     self.labelSubtitle = Label(self.search_window, text=book["subtitle"], relief=FLAT, background="#2C0A59", foreground="white", font=("Georgia 6 bold"))
        #     self.labelSubtitle.place(x=160, y=235)
        # except:
        #     pass

    async def renders_image_book(self, books):
        try:
            for labelImage in self.listlabelImage:
                labelImage.destroy()
        except:
            pass
        counter = 1
        try:
            for i in range(0, len(self.listLabels)):
                self.listLabels[i].destroy()
        except:
            pass

        self.listLabels = list()
        for i in range(0,len(books)):
            self.listLabels.append(None)
        for book in books:
            if counter == 1:
                try:
                    imageUrl = book["imageLink"]
                    u = urlopen(imageUrl)
                    raw_data = u.read()
                    u.close()
                    self.listLabelImage = list()
                    photo = ImageTk.PhotoImage(data=raw_data)
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter - 1].image = photo
                    self.listLabels[counter - 1].place(x=30, y=230)
                except:
                    photo = PhotoImage(file=relative_to_assets("noImageAvailable.png"))
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter -1].image = photo
                    self.listLabels[counter - 1].place(x=30, y=230)
            elif counter == 5:
                try:
                    imageUrl = book["imageLink"]
                    u = urlopen(imageUrl)
                    raw_data = u.read()
                    u.close()

                    photo = ImageTk.PhotoImage(data=raw_data)
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter - 1].image = photo
                    self.listLabels[counter - 1].place(x=30, y=450)
                except:
                    photo = PhotoImage(file=relative_to_assets("noImageAvailable.png"))
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter - 1].image = photo
                    self.listLabels[counter - 1].place(x=30, y=450)
            else:
                if counter > 1 and counter < 5:
                    x = 30 + ((counter-1) * 320)
                    y = 230
                else:
                    x = 30 + ((counter - 5) * 320)
                    y = 450
                try:
                    imageUrl = book["imageLink"]
                    u = urlopen(imageUrl)
                    raw_data = u.read()
                    u.close()

                    photo = ImageTk.PhotoImage(data=raw_data)
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter - 1].image = photo
                    self.listLabels[counter - 1].place(x=x, y=y)
                except:
                    photo = PhotoImage(file=relative_to_assets("noImageAvailable.png"))
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter -1].image = photo
                    self.listLabels[counter - 1].place(x=x, y=y)
            counter += 1
        self.label.destroy()

    def render_wait_msg(self, event):
        try:
            self.label.destroy()
        except:
            pass
        finally:
            self.var = StringVar()
            self.var.set("Wait a moment")
            self.label = Label( self.search_window, textvariable=self.var, relief=FLAT, background="#2C0A59", foreground="white", font=("Georgia 14 bold"))
            self.label.pack()

    def search_keyword(self):
        keyword = self.entry_search.get()
        books = asyncio.run(request_google_books(keyword))
        if type(books) != list:
            try: 
                self.label.destroy()
            except:
                pass
            finally:
                self.var.set(f"Error: {books}")
                self.label = Label( self.search_window, textvariable=self.var, relief=FLAT, background="#2C0A59", foreground="red", font=("Georgia 14 bold"))
                self.label.pack()
        else:
            asyncio.run(self.renders_image_book(books))
            self.renders_infos_book(books)

    def generate_search_window(self):
        self.canvas = Canvas(
            self.search_window,
            bg = "#2C0A59",
            height = 700,
            width = 1300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        button_image_icon = PhotoImage(
            file=relative_to_assets("icon.png"))
        button_icon = Button(
            image=button_image_icon,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A60",
            command=self.back_to_home,
            cursor="hand2",
        )
        button_icon.place(
            x=1197.0,
            y=19.0,
        )

        image_image_search = PhotoImage(
            file=relative_to_assets("image_search.png"))
        
        self.canvas.create_image(
            312.0,
            59.0,
            image=image_image_search
        )

        image_image_isbn = PhotoImage(
            file=relative_to_assets("keywordSearch.png"))
        
        self.canvas.create_image(
            240.0,
            129.0,
            image=image_image_isbn
        )

        entry_image_search = PhotoImage(
            file=relative_to_assets("entry_search.png"))
        
        self.canvas.create_image(
            235.5,
            180.5,
            image=entry_image_search
        )

        self.entry_search = Entry(
            bd=0,
            bg="#93679A",
            highlightthickness=0,
            justify="center",
            font=('Georgia 20')
        )

        self.entry_search.place(
            x=65.5,
            y=161.5,
            width=350.0,
            height=30.75,
        )

        button_image_search = PhotoImage(
            file=relative_to_assets("button_search.png"))
        self.button_search = Button(
            image=button_image_search,
            borderwidth=0,
            highlightthickness=0,
            command=self.search_keyword,
            relief="sunken",
            cursor="hand2",
            activebackground="#2C0A59",
            bg="#2C0A59",
            bd=0,   
        )
        self.button_search.place(
            x=450.0,
            y=162.0,
            width=40.3193359375,
            height=37.80328369140625
        )
        self.button_search.bind("<Button-1>", self.render_wait_msg)
        self.search_window.resizable(False, False)
        self.search_window.mainloop()
