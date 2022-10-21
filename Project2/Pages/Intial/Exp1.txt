from tkinter import *
import mysql.connector



class home():
    def start(self):
        root = Tk()
        root.geometry("800x480")
        root.title("Sukrit Machine Tools")
        root.wm_iconbitmap('sukrit_Logo.ico')
        root.configure(background="#b3ffe0")

        return root

    def db(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sukrit",
            database="test786"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM punchlist")
        myresult = mycursor.fetchall()
        return mydb, mycursor, myresult

