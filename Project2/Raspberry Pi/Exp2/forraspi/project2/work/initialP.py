from tkinter import *
import mysql.connector
import mariadb


class home():
    def start(self):
        root = Tk()
        root.geometry("800x480")
        root.title("Sukrit Machine Tools")
        #root.wm_iconbitmap('sukrit_Logo.ico')
        root.configure(background="#b3ffe0")

        return root

    def db(self):
        #mydb = mysql.connector.connect(
            #host="localhost",
            #user="root",
            #password="sukrit",
            #database="test786"
        #)
        
        try:
            mydb = mariadb.connect(
                user="root",
                password="sukrit",
                host="localhost",
                port=3306,
                database="test786"
                )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

        mycursor = mydb.cursor()
        return mydb, mycursor


