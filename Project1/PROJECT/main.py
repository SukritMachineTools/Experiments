from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
class Hotelmanagement:
    def __init__(self):
        self.window=Tk()
        # ---------------------Window Settings---------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        self.window.config(bg="#EBF4FA")
        self.window.state("zoomed")
        self.window.minsize(500,500)
        self.window.title("HOTEL MANAGEMENT SYSTEM")
        if w>=1900:
            lbl_h=100
        elif w>=1300:
            lbl_h=60
        self.lbltitle=Label(self.window,text="HOTEL MANAGMENT SYSTEM",
        font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE).place(x=0,y=0,width=w,height=lbl_h)

        #----------------------1st Image--------------------
        img1=Image.open(r"my_images/RAMADA.png")
        img1=img1.resize((w,h-lbl_h))
        self.photo=ImageTk.PhotoImage(img1)
        self.lblimg=Label(self.window,image=self.photo).place(x=0,y=lbl_h,width=w,height=h-lbl_h)   #1367,625

        #----------------------Menubar-----------------------
        self.lblframe=LabelFrame(self.window,bd=3,relief=RIDGE,text="Login Details",bg="grey").place(x=1000,y=250,width=280,height=205)
        img2 = Image.open(r"my_images/flow2.png")
        img2 = img2.resize((250, 200))
        self.photo1 = ImageTk.PhotoImage(img2)
        self.lblimg1 = Label(self.window, image=self.photo1, bd=4, relief=RIDGE)
        self.lblimg1.place(x=1000, y=250, width=280, height=205)
        myfont = ("times new roman", 12)
        self.l1 = Label(self.window, text="Username",bg="black", fg="gold", font=myfont)
        self.l2 = Label(self.window, text="Password", bg="black", fg="gold", font=myfont)

        self.t1 = Entry(self.window)
        self.t2 = Entry(self.window, show='*')

        self.b1=Button(self.window,text="Login",bg="black", fg="gold", font=myfont,padx=20,command=self.fetchData)
        self.b2=Button(self.window,text="Create New Account",bg="black", fg="gold", font=myfont,padx=20,command=self.new_window)

        x1 = 1000
        y1 = 250
        x_diff = 80

        self.l1.place(x=x1+20, y=y1+20)
        self.t1.place(x=x1 +20+ x_diff, y=y1+20)

        self.l2.place(x=x1+20, y=y1+60)
        self.t2.place(x=x1 +20+ x_diff, y=y1+60)

        self.b1.place(x=x1+90,y=y1+100)
        self.b2.place(x=x1+50,y=y1+150)

        self.window.mainloop()

    def databaseConnection(self):
        myhost="localhost"
        mydb="hotelmgtdb"
        myuser="root"
        mypassword=""
        try:
            self.conn = pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting database \n"+str(e),parent=self.window)

    def fetchData(self):
        self.databaseConnection()
        try:
            myqry = "select * from admin where username=%s and password=%s"
            rowcount = self.curr.execute(myqry,(self.t1.get(),self.t2.get()))
            data = self.curr.fetchone()
            if data:
                uname=data[0]
                utype=data[2]
                messagebox.showinfo("Success","Welcome "+utype,parent=self.window)
                self.window.destroy()
                from page2 import main_menu
                main_menu()
            else:
                messagebox.showinfo("Failure","Wrong username or password",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window)

    def new_window(self):
        self.window.destroy()
        from account import UserClass
        UserClass()

if __name__=='__main__':
    obj=Hotelmanagement()