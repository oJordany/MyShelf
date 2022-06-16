from pathlib import Path
# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MenuWindow: 

    def __init__(self):
        self.menu_window = Tk()

        self.menu_window.geometry("1295x700")
        self.menu_window.configure(bg = "#2C0A59")

    def back_to_home(self):
        from interface.screens.HomeWindow import HomeWindow
        self.menu_window.destroy()
        self.novaHome = HomeWindow()
        self.novaHome.generate_home_window()

    def go_to_my_books_window(self):
        from interface.screens.MyBooksWindow import Aplicattion
        self.menu_window.destroy()
        self.my_books_window = Aplicattion()
        self.my_books_window.interface()
        self.my_books_window.Frame_Table()
        self.my_books_window.MyBooks_list()        
        self.my_books_window.insert_datas()        
        self.my_books_window.generate_my_books_window()
    
    def go_to_new_book_window(self):
        from interface.screens.NewBookWindow import NewBookWindow
        self.menu_window.destroy()
        self.new_books_window = NewBookWindow()
        self.new_books_window.generate_new_book_window()
    
    def go_to_search_window(self):
        from interface.screens.Search_window import SearchWindow
        self.menu_window.destroy()
        self.search_window = SearchWindow()
        self.search_window.generate_search_window()

    def generate_menu_window(self):
        canvas = Canvas(
            self.menu_window,
            bg = "#2C0A59",
            height = 700,
            width = 1295,
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


        self.menu_window.button_MB_active = PhotoImage(
            file=relative_to_assets("button_MB.png"))
        self.menu_window.button_MB_inactive = PhotoImage(
            file=relative_to_assets("button_MB_inactive.png"))


        button_image_MB = PhotoImage(
            file=relative_to_assets("button_MB_inactive.png"))
        button_MB = Button(
            image=button_image_MB,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_to_my_books_window,
            relief="sunken",
            bd=0,
            bg="#2C0A59",
            cursor="hand2",
            activebackground="#2C0A59",
        )

        button_MB.place(
            x=485.0,
            y=112.0,
        )

        button_MB.bind("<Enter>", lambda e: button_MB.config(image=self.menu_window.button_MB_active))
        button_MB.bind("<Leave>", lambda e: button_MB.config(image=self.menu_window.button_MB_inactive))


        self.menu_window.button_ANB_active = PhotoImage(
            file=relative_to_assets("button_ANB.png"))
        self.menu_window.button_ANB_inactive = PhotoImage(
            file=relative_to_assets("button_ANB_inactive.png"))

        button_ANB_image = PhotoImage(
            file=relative_to_assets("button_ANB_inactive.png"))
        button_ANB = Button(
            image=button_ANB_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_to_new_book_window,
            relief="sunken",
            bd=0,
            bg="#2C0A59",
            cursor="hand2",
            activebackground="#2C0A59",
        )
        button_ANB.place(
            x=485.0,
            y=302.5,
        )

        button_ANB.bind("<Enter>", lambda e: button_ANB.config(image=self.menu_window.button_ANB_active))
        button_ANB.bind("<Leave>", lambda e: button_ANB.config(image=self.menu_window.button_ANB_inactive))


        self.menu_window.button_SB_active = PhotoImage(
            file=relative_to_assets("button_SB.png"))
        self.menu_window.button_SB_inactive = PhotoImage(
            file=relative_to_assets("button_SB_inactive.png"))

        button_SB_image = PhotoImage(
            file=relative_to_assets("button_SB_inactive.png"))
        button_SB = Button(
            image=button_SB_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_to_search_window,
            relief="sunken",
            bd=0,
            bg="#2C0A59",
            cursor="hand2",
            activebackground="#2C0A59",
        )

        button_SB.place(
            x=485.0,
            y=490.0,
        )

        button_SB.bind("<Enter>", lambda e: button_SB.config(image=self.menu_window.button_SB_active))
        button_SB.bind("<Leave>", lambda e: button_SB.config(image=self.menu_window.button_SB_inactive))

        self.menu_window.resizable(False, False)
        self.menu_window.mainloop()

