from email.utils import formatdate
from pathlib import Path
from socket import timeout
from time import time
import requests
import threading
from tkinter import NW, Tk, Canvas, Entry, Text, Button, PhotoImage, Label, StringVar, FLAT
from turtle import delay


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class NewBookWindow:
    def __init__(self):    
        self.newbookwindow= Tk()
        icon = PhotoImage(file=relative_to_assets("Logo.png"))
        self.newbookwindow.iconphoto(False, icon)
        self.newbookwindow.title("Add a New Book")
        self.newbookwindow.geometry("1300x700")
        self.newbookwindow.configure(bg = "#2C0A59")
        self.framelist = []      # List to hold all the frames
        self.frame_index = 0 
        self.count = 0
        self.flag = True
        self.thread = threading.Thread(target= self.submit)

    def back_to_home(self):
        from interface.screens.HomeWindow import HomeWindow
        self.newbookwindow.destroy()
        self.novaHome = HomeWindow()
        self.novaHome.generate_home_window()

    def animate_gif(self, count=0):  
        try:
            if self.thread.is_alive() == True:
                if count == 0 and self.flag == True:
                    self.l1 = Label(self.newbookwindow, bg="#2C0A59", image='' )
                    self.l1.place(x=650, y=90)
                    self.flag=False

                count += 1
                self.l1.config(image=self.framelist[count])
                    
                if count > self.last_frame - 1:
                    count = 0  
                #recall animate_gif method    
                self.l1.after(50, lambda: self.animate_gif(count=count))
            else:
                self.l1.destroy()
                self.thread = threading.Thread(target=self.submit)
        except:
            self.thread = threading.Thread(target=self.submit)

    def submit(self):
        try:
            self.label.destroy()
        except:
            pass
        from controller.createEvent import create_event_detail
        from controller.database import Table, check_existence
        from controller.request import request 
        from datetime import date
        import smtplib
        import email.message
        from confidential.confidential import decrypt

        isbn = self.entry_isbn.get()
        var = StringVar()
        datas = request(isbn)
        check = check_existence(isbn)



        if type(datas) != str and not check:
            try:
                datas['status'] = self.status 
                self.estante = Table()
                if self.status == "read":
                    datas['start_of_reading'] = "NULL"
                    datas['end_of_reading'] = "NULL"
                    self.estante.add_data(datas)
                    var.set("book successfully inserted")
                    colorLabel = "green"
                elif self.status == "reading":
                    datas['start_of_reading'] = str(date.today())
                    datas['end_of_reading'] = "NULL"
                    self.estante.add_data(datas)
                    var.set("book successfully inserted")
                    colorLabel = "green"

                elif self.status == "I want to read":
                    try:
                        datas['start_of_reading'] = self.IWTR_window.date
                        datas['end_of_reading'] = "NULL"
                        self.event_name = 'Read Notification'
                        self.body = {
                            'ContentType': 'HTML',
                            'Content': f'''<p>you have a book to read on your virtual bookshelf.</p><p>Don't waste time, start reading the book &quot;{datas['title']}&quot; right now.</p>'''
                        }
                        self.start = {
                            'DateTime': f'{self.IWTR_window.date}T08:00:00',
                            'TimeZone': 'America/Sao_Paulo'
                        }

                        self.end = {
                            'DateTime': f'{self.IWTR_window.date}T23:00:00',
                            'TimeZone': 'America/Sao_Paulo'
                        }

                        self.attendees = [
                            {
                                'EmailAddress': {
                                    "Address":f'{self.IWTR_window.email}',
                                },
                                'Type': 'Required'
                            },
                        ]
                        create_event_detail(self.event_name, self.body, self.start, self.end, self.attendees)
                        datas_decrypted = decrypt('confidential.txt', 1)
                        username = self.IWTR_window.username
                        email_body = f'''
                        <h3>Hi {username} 👋,</h3>
                        <p>you have a book to read on your virtual bookshelf.</p>
                        <p>We created an event on your microsoft calendar on {self.IWTR_window.date} so you don't forget to read the book &quot;{datas['title']}&quot;.</p>
                        <br>
                        <p>Thanks for staying with us.</p>
                        <br>
                        <p>With best regards,</p>
                        <p>My Shelf📚.</p>
                        '''
                        msg = email.message.Message()
                        msg['Subject'] = "Read Notification"
                        msg['From'] = datas_decrypted[0]
                        msg['To'] = self.IWTR_window.email
                        code = datas_decrypted[1]
                        msg.add_header('Content-Type', 'text/html')
                        msg.set_payload(email_body)

                        s = smtplib.SMTP('smtp.outlook.com: 587')

                        s.starttls()

                        s.login(msg["From"], code)
                        s.sendmail(msg["From"], msg["To"], msg.as_string().encode('utf-8'))
                        
                        s.quit()
                        var.set("book successfully inserted")
                        colorLabel = "green"
                        self.estante.add_data(datas)
                    except:
                        var.set("Error: Invalid Email")
                        colorLabel = "red"
            except Exception as err:
                var.set("Error: select a status")
                colorLabel = "red"
        elif not check:
            var.set(datas)
            colorLabel = "red"

        elif check:
            var.set("This book already exists")
            colorLabel = "red"
        
        try: 
            self.label.destroy()
        except:
            pass 
        finally:
            self.label = Label( self.newbookwindow, textvariable=var, relief=FLAT, background="#2C0A59", foreground=colorLabel, font=("Georgia 14 bold"))
            self.label.place(x=560, y=120)

        
        del datas
        self.flag = True
    
    def select_status(self, status):
        self.status = status
        

    def clicked_button_read(self, event):
        self.status = 'read'
        self.button_read.config(image=self.newbookwindow.btn_activeRead)
        self.button_read.bind("<Leave>", lambda e: self.button_read.config(image=self.newbookwindow.btn_activeRead))
        
        self.button_reading.config(image=self.newbookwindow.btn_inactiveReading)
        self.button_reading.bind("<Leave>", lambda e: self.button_reading.config(image=self.newbookwindow.btn_inactiveReading))

        self.button_IWTR.config(image=self.newbookwindow.btn_inactiveIWTR)
        self.button_IWTR.bind("<Leave>", lambda e: self.button_IWTR.config(image=self.newbookwindow.btn_inactiveIWTR))

    def clicked_button_reading(self, event):
        self.status = 'reading'
        self.button_reading.config(image=self.newbookwindow.btn_activeReading)
        self.button_reading.bind("<Leave>", lambda e: self.button_reading.config(image=self.newbookwindow.btn_activeReading))
        
        self.button_read.config(image=self.newbookwindow.btn_inactiveRead)
        self.button_read.bind("<Leave>", lambda e: self.button_read.config(image=self.newbookwindow.btn_inactiveRead))

        self.button_IWTR.config(image=self.newbookwindow.btn_inactiveIWTR)
        self.button_IWTR.bind("<Leave>", lambda e: self.button_IWTR.config(image=self.newbookwindow.btn_inactiveIWTR))

    def clicked_button_IWTR(self, event):
        self.status = "I want to read"
        self.button_IWTR.config(image=self.newbookwindow.btn_activeIWTR)
        self.button_IWTR.bind("<Leave>", lambda e: self.button_IWTR.config(image=self.newbookwindow.btn_activeIWTR))
        
        self.button_reading.config(image=self.newbookwindow.btn_inactiveReading)
        self.button_reading.bind("<Leave>", lambda e: self.button_reading.config(image=self.newbookwindow.btn_inactiveReading))

        self.button_read.config(image=self.newbookwindow.btn_inactiveRead)
        self.button_read.bind("<Leave>", lambda e: self.button_read.config(image=self.newbookwindow.btn_inactiveRead))

    def go_to_IWTR_window(self):
        from interface.screens.IWantToReadWindow import IWantToReadWindow
        self.IWTR_window = IWantToReadWindow()
        self.IWTR_window.generate_IWTR_window()

    def generate_new_book_window(self):
        canvas = Canvas(
            self.newbookwindow,
            bg = "#2C0A59",
            height = 700,
            width = 1300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)

        image_image_readStatus = PhotoImage(
            file=relative_to_assets("image_readStatus.png"))
        image_readStatus = canvas.create_image(
            718.0,
            347.0,
            image=image_image_readStatus
        )

        image_image_ISB = PhotoImage(
            file=relative_to_assets("image_ISBN.png"))
        image_2 = canvas.create_image(
            683.0,
            180.0,
            image=image_image_ISB
        )

        image_image_AddNewBook = PhotoImage(
            file=relative_to_assets("image_AddNewBook.png"))
        image_AddNewBook = canvas.create_image(
            321.0,
            58.0,
            image=image_image_AddNewBook
        )

        entry_image_isbn = PhotoImage(
            file=relative_to_assets("entry_isbn.png"))

        entry_bg_1 = canvas.create_image(
            670.5,
            253.0,
            image=entry_image_isbn
        )

        self.entry_isbn = Entry(
            bd=0,
            bg="#93679A",
            highlightthickness=0,
            justify="center",
            font=('Georgia 20')      
        )
        self.entry_isbn.place(
            x=375.0,
            y=235.0,
            width=600.0,
            height=30.75,
        )

        self.newbookwindow.btn_inactiveRead = PhotoImage(file=relative_to_assets("button_read.png"))
        self.newbookwindow.btn_activeRead = PhotoImage(file=relative_to_assets("button_ReadActive.png"))

        self.button_image_read = PhotoImage(
            file=relative_to_assets("button_read.png"))
        self.button_read = Button(
            image=self.button_image_read,
            borderwidth=0,
            highlightthickness=0,
            relief="sunken",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A59",
            cursor="hand2",
        )
        self.button_read.place(
            x=537.0,
            y=380.0,

        )

        self.button_read.bind("<Enter>", lambda e: self.button_read.config(image=self.newbookwindow.btn_activeRead))
        self.button_read.bind("<Leave>", lambda e: self.button_read.config(image=self.newbookwindow.btn_inactiveRead))
        self.button_read.bind("<Button-1>", self.clicked_button_read)

        self.newbookwindow.btn_inactiveReading = PhotoImage(file=relative_to_assets("button_reading.png"))
        self.newbookwindow.btn_activeReading = PhotoImage(file=relative_to_assets("button_ReadingActive.png"))

        button_image_reading = PhotoImage(
            file=relative_to_assets("button_reading.png"))
        self.button_reading = Button(
            image=button_image_reading,
            borderwidth=0,
            highlightthickness=0,
            relief="sunken",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A59",
            cursor="hand2",
        )
        self.button_reading.place(
            x=537.0,
            y=480.0,
        )

        self.button_reading.bind("<Enter>", lambda e: self.button_reading.config(image=self.newbookwindow.btn_activeReading))
        self.button_reading.bind("<Leave>", lambda e: self.button_reading.config(image=self.newbookwindow.btn_inactiveReading))
        self.button_reading.bind("<Button-1>", self.clicked_button_reading)

        self.newbookwindow.btn_inactiveIWTR = PhotoImage(file=relative_to_assets("button_IWTR.png"))
        self.newbookwindow.btn_activeIWTR = PhotoImage(file=relative_to_assets("button_IWTRActive.png"))

        button_image_IWTR = PhotoImage(
            file=relative_to_assets("button_IWTR.png"))
        self.button_IWTR = Button(
            image=button_image_IWTR,
            borderwidth=0,
            highlightthickness=0,
            relief="sunken",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A59",
            command=self.go_to_IWTR_window,
            cursor="hand2",
        )
        self.button_IWTR.place(
            x=537.0,
            y=580.0,
        )
        self.button_IWTR.bind("<Enter>", lambda e: self.button_IWTR.config(image=self.newbookwindow.btn_activeIWTR))
        self.button_IWTR.bind("<Leave>", lambda e: self.button_IWTR.config(image=self.newbookwindow.btn_inactiveIWTR))
        self.button_IWTR.bind("<Button-1>",self.clicked_button_IWTR)

        button_image_plus = PhotoImage(
            file=relative_to_assets("button_plus.png"))
        button_plus = Button(
            image=button_image_plus,
            borderwidth=0,
            highlightthickness=0,
            relief="sunken",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A60",
            command=self.animate_gif,
            cursor="hand2",
        )
        button_plus.place(
            x=1087.2080078125,
            y=227.0,
        )
        button_plus.bind("<Button-1>", lambda e: self.thread.start())

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
        while True:
            try:
                # Read a frame from GIF file
                part = 'gif -index {}'.format(self.frame_index)
                frame = PhotoImage(file=relative_to_assets('loading.gif'), format=part)
            except:
                self.last_frame = self.frame_index - 1    # Save index for last frame
                break               # Will break when GIF index is reached
            self.framelist.append(frame)
            self.frame_index += 1 

        self.newbookwindow.resizable(False, False)
        self.newbookwindow.mainloop()
