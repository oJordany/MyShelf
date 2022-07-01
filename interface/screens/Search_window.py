from email.mime import image
from itertools import count
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scrollbar, font, Label, ttk, LEFT, BOTTOM, RIGHT, TOP, X, Y, StringVar, FLAT
import tkinter
import webbrowser
import asyncio
from controller.request import request, request_google_books
from PIL import Image, ImageTk
from urllib.request import urlopen
import threading
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SearchWindow:

    def __init__(self):
        # Assets to LoadingGif
        self.framelist = []      # List to hold all the frames
        self.frame_index = 0 
        self.count = 0
        self.flag = True

        self.search_window = Tk()
        self.thread = threading.Thread(target= self.search_keyword)
        self.var = StringVar()
        icon = PhotoImage(file=relative_to_assets("Logo.png"))
        self.search_window.iconphoto(False, icon)
        self.search_window.title("Search")
        self.search_window.geometry("1300x700")
        self.search_window.configure(bg = "#2C0A59")
    

    def animate_gif(self, count=0):  
        try:
            if self.thread.is_alive() == True:
                if count == 0 and self.flag == True:
                    self.l1 = tkinter.Label(self.search_window, bg="#2C0A59", image='' )
                    self.l1.place(x=650, y=150)
                    self.flag=False

                
                count += 1
                self.l1.config(image=self.framelist[count])
                print('ta vivo')
                    
                if count > self.last_frame - 1:
                    count = 0  
                #recall animate_gif method    
                print(count)
                self.l1.after(50, lambda: self.animate_gif(count=count))
            else:
                print('ta morto')
                self.l1.destroy()
                self.thread = threading.Thread(target=self.search_keyword)
        except:
            self.thread = threading.Thread(target=self.search_keyword)
        
    def back_to_home(self):
        from interface.screens.HomeWindow import HomeWindow
        self.search_window.destroy()
        self.novaHome = HomeWindow()
        self.novaHome.generate_home_window()

    def open_url(self, url):
        webbrowser.open_new(url)
        #lambda url="google.com": self.open_url(url)

    async def renders_infos_book(self, books):
        try:
            for i in range(0, len(self.listCanvas)):
                self.listCanvas[i].destroy()
        except:
            pass

        self.listCanvas = list()
        for i in range(0,len(books)):
            self.listCanvas.append(None)
        counter = 1
        for book in books:
            if counter == 1:
                frame = ttk.LabelFrame(self.search_window, width=180, height=180)
                frame.place(x=160, y=230)

                #scrollbar in frame
                self.listCanvas[counter - 1] = mycanvas=Canvas(frame,height=168, width=170)
                self.listCanvas[counter - 1].pack(side=TOP,ipadx=0,ipady=0)
                xscrollbar = ttk.Scrollbar(frame, orient=HORIZONTAL,command=self.listCanvas[counter - 1].xview)
                xscrollbar.pack(side=BOTTOM,fill=X)#ipadx=76,ipady=76,pady=0,padx=0
                self.listCanvas[counter - 1].configure(xscrollcommand=xscrollbar.set)
                xscrollbar.config(command=self.listCanvas[counter - 1].xview)
                try:
                    
                    teste=Label(self.listCanvas[counter - 1],width=10,height=2,text="know more",font=("Georgia 10 bold"),foreground="purple")
                    teste.pack(side=TOP, ipadx=10,ipady=10,fill='x')
                   

                    self.labelTitle = Label(self.listCanvas[counter - 1], text=book["title"], relief=FLAT, foreground="purple", font=("Georgia 10 bold"))
                    self.labelTitle.pack(side=TOP,pady=10,padx=10)
                except:
                    pass
                try:
                    self.labelSubtitle = Label(self.listCanvas[counter - 1], text=book["subtitle"], relief=FLAT, foreground="purple", font=("Georgia 12 bold"))
                    self.labelSubtitle.pack(pady=10,padx=10)
                except:
                    pass

            elif counter == 5:
                frame = ttk.LabelFrame(self.search_window, width=180, height=180)
                frame.place(x=160, y=450)
                #scrollbar in frame
                self.listCanvas[counter - 1]=Canvas(frame,height=168, width=170)
                self.listCanvas[counter - 1].pack(side=TOP,ipadx=0,ipady=0)
                xscrollbar = ttk.Scrollbar(frame, orient=HORIZONTAL,command=self.listCanvas[counter - 1].xview)
                self.listCanvas[counter - 1].configure(xscrollcommand=xscrollbar.set)
                xscrollbar.pack(side=BOTTOM,fill=X)#ipadx=76,ipady=76,pady=0,padx=0
                xscrollbar.config(command=self.listCanvas[counter - 1].xview)
                try:
                    
                    teste=Label(self.listCanvas[counter - 1],width=10,height=2,text="know more",font=("Georgia 10 bold"),foreground="purple")
                    teste.pack(side=TOP,pady=10,padx=10)
                   

                    self.labelTitle = Label(self.listCanvas[counter - 1], text=book["title"], relief=FLAT, foreground="purple", font=("Georgia 10 bold"))
                    self.labelTitle.pack(side=TOP,pady=10,padx=10)
                except:
                    pass
                try:
                    self.labelSubtitle = Label(self.listCanvas[counter - 1], text=book["subtitle"], relief=FLAT, foreground="purple", font=("Georgia 12 bold"))
                    self.labelSubtitle.pack()
                except:
                    pass


            else:
                if counter > 1 and counter < 5:
                    x = 160 + ((counter-1) * 320)
                    y = 230
                else:
                    x = 160 + ((counter - 5) * 320)
                    y = 450
                frame = ttk.LabelFrame(self.search_window, width=180, height=180)
                frame.place(x=x, y=y)

                #scrollbar in frame
                self.listCanvas[counter - 1]=Canvas(frame,height=168, width=170)
                self.listCanvas[counter - 1].pack(side=TOP,ipadx=0,ipady=0)
                xscrollbar = ttk.Scrollbar(frame, orient=HORIZONTAL,command=self.listCanvas[counter - 1].xview)
                self.listCanvas[counter - 1].configure(xscrollcommand=xscrollbar.set)
                xscrollbar.pack(side=BOTTOM,fill=X)#ipadx=76,ipady=76,pady=0,padx=0
                xscrollbar.config(command=self.listCanvas[counter - 1].xview)
                
                try:
                    
                    teste=Label(self.listCanvas[counter - 1],width=10,height=2,text="know more",font=("Georgia 10 bold"),foreground="purple")
                    teste.pack(side=TOP)
                   

                    self.labelTitle = Label(self.listCanvas[counter - 1], text=book["title"], relief=FLAT, foreground="purple", font=("Georgia 10 bold"))
                    self.labelTitle.pack(side=TOP)
                except:
                    pass
                try:
                    self.labelSubtitle = Label(self.listCanvas[counter - 1], text=book["subtitle"], relief=FLAT, foreground="purple", font=("Georgia 12 bold"))
                    self.labelSubtitle.pack(side=TOP)
                except:
                    pass
    
            counter += 1 
        # try:

        #     teste=Label(mycanvas,width=10,height=2,text="teste",font=("Georgia 6 bold"),foreground="purple",background="#2C0A59")
        #     teste.pack()

        #     self.labelTitle = Label(frame, text=book["title"], relief=FLAT, background="#2C0A59", foreground="purple", font=("Georgia 6 bold"))
        #     self.labelTitle.pack(side=TOP)
        # except:
        #     pass
        # try:
        #     self.labelSubtitle = Label(mycanvas, text=book["subtitle"], relief=FLAT, background="#2C0A59", foreground="white", font=("Georgia 6 bold"))
        #     self.labelSubtitle.pack(side=TOP)
        # except:
        #     pass

    async def renders_image_book(self, books):
        try:
            for i in range(0, len(self.listLabels)):
                self.listLabels[i].destroy()
        except:
            pass

        counter = 1
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
        self.flag = True

    # def render_wait_msg(self, event):
    #     try:
    #         self.label.destroy()
    #     except:
    #         pass
    #     finally:
    #         self.var = StringVar()
    #         self.var.set("Wait a moment")
    #         self.label = Label( self.search_window, textvariable=self.var, relief=FLAT, background="#2C0A59", foreground="white", font=("Georgia 14 bold"))
    #         self.label.pack()


    def search_keyword(self):
        keyword = self.entry_search.get()
        books = asyncio.run(request_google_books(keyword))
        try: 
            self.label.destroy()
        except:
            pass
        if type(books) != list:
            try:
                for i in range(0, len(self.listLabels)):
                    self.listLabels[i].destroy()
            except:
                pass
            try: 
                self.label.destroy()
            except:
                pass
            finally:
                self.var.set(f"Error: {books}")
                self.label = Label( self.search_window, textvariable=self.var, relief=FLAT, background="#2C0A59", foreground="red", font=("Georgia 14 bold"))
                self.label.pack()
                self.flag = True
        else:
            asyncio.run(self.renders_image_book(books))
            asyncio.run(self.renders_infos_book(books))


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
            command=self.animate_gif,
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
        self.button_search.bind("<Button-1>", lambda e: self.thread.start())
        
        while True:
            try:
                # Read a frame from GIF file
                part = 'gif -index {}'.format(self.frame_index)
                frame = PhotoImage(file=relative_to_assets('loading.gif'), format=part)
            except:
                print("break")
                self.last_frame = self.frame_index - 1    # Save index for last frame
                break               # Will break when GIF index is reached
            self.framelist.append(frame)
            print(len(self.framelist))
            self.frame_index += 1 

        self.search_window.resizable(False, False)

        self.search_window.mainloop()
