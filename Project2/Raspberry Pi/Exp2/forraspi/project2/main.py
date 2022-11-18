from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector


class benddata():
    def bendframe(self):
        root = Tk()
        root.geometry("800x480")
        root.title("Sukrit Machine Tools")
        root.wm_iconbitmap('sukrit_Logo.ico')
        root.configure(background="#b3ffe0")



        root.mainloop()

bd=benddata()
bd.bendframe()