from pathlib import Path
# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def generate_menu_window():

    menu_window = Tk()

    menu_window.geometry("1295x700")
    menu_window.configure(bg = "#2C0A59")

    def back_to_home():
        from interface.screens.homeWindow import HomeWindow
        menu_window.destroy()
        novaHome = HomeWindow()
        novaHome.generate_home_window()

    canvas = Canvas(
        menu_window,
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
        command=back_to_home,
        relief="flat",
        bd=0,
        bg="#2C0A59",
        cursor="hand2",
        activebackground="#2C0A59",
    )
    button_icon.place(
        x=1197.0,
        y=19.0,
    )


    menu_window.button_MB_active = PhotoImage(
        file=relative_to_assets("button_MB.png"))
    menu_window.button_MB_inactive = PhotoImage(
        file=relative_to_assets("button_MB_inactive.png"))


    button_image_MB = PhotoImage(
        file=relative_to_assets("button_MB_inactive.png"))
    button_MB = Button(
        image=button_image_MB,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_MB_inactive clicked"),
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

    button_MB.bind("<Enter>", lambda e: button_MB.config(image=menu_window.button_MB_active))
    button_MB.bind("<Leave>", lambda e: button_MB.config(image=menu_window.button_MB_inactive))


    menu_window.button_ANB_active = PhotoImage(
        file=relative_to_assets("button_ANB.png"))
    menu_window.button_ANB_inactive = PhotoImage(
        file=relative_to_assets("button_ANB_inactive.png"))

    button_ANB_image = PhotoImage(
        file=relative_to_assets("button_ANB_inactive.png"))
    button_ANB = Button(
        image=button_ANB_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_ANB clicked"),
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

    button_ANB.bind("<Enter>", lambda e: button_ANB.config(image=menu_window.button_ANB_active))
    button_ANB.bind("<Leave>", lambda e: button_ANB.config(image=menu_window.button_ANB_inactive))


    menu_window.button_SB_active = PhotoImage(
        file=relative_to_assets("button_SB.png"))
    menu_window.button_SB_inactive = PhotoImage(
        file=relative_to_assets("button_SB_inactive.png"))

    button_SB_image = PhotoImage(
        file=relative_to_assets("button_SB_inactive.png"))
    button_SB = Button(
        image=button_SB_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_SB clicked"),
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

    button_SB.bind("<Enter>", lambda e: button_SB.config(image=menu_window.button_SB_active))
    button_SB.bind("<Leave>", lambda e: button_SB.config(image=menu_window.button_SB_inactive))

    menu_window.resizable(False, False)
    menu_window.mainloop()

