from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox,Treeview
import pymysql
from PIL import Image,ImageTk

class page4:
    def __init__(self,hwindow):
        self.window4=Toplevel(hwindow)
        self.window4.geometry("%dx%d+%d+%d" % (1116, 445, 242, 252))
        self.window4.config(bg="white")
        self.window4.title("Room Adding")
        self.lbltitle = Label(self.window4, text="Room Adding Department", font=("times new roman", 20, "bold"), bg="black",
                              fg="gold", bd=4, relief=RIDGE).place(x=0, y=0, width=1116, height=40)

        # ------------------ table ---------------------------------------
        self.tablearea = LabelFrame(self.window4, bd=3, relief=RIDGE, text="Room Details")
        self.scroll_y = Scrollbar(self.tablearea, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.mytable = Treeview(self.tablearea, columns=['c1', 'c2', 'c3', 'c4'], height=15,yscrollcommand=self.scroll_y.set)
        self.scroll_y.config(command=self.mytable.yview)
        self.mytable.heading("c1", text="Floor")
        self.mytable.heading("c2", text="Room Number")
        self.mytable.heading("c3", text="Room Type")
        self.mytable.heading("c4", text="Status")
        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=90, anchor='center')
        self.mytable.column("#2", width=110, anchor='center')
        self.mytable.column("#3", width=120, anchor='center')
        self.mytable.column("#4", width=120, anchor='center')
        self.mytable.bind("<ButtonRelease-1>", lambda e: self.getSelectedRowData())

        self.mytable.pack()
        self.tablearea.place(x=630, y=60)

#-------------Labels and Entries------------
        font2 = ("times new roman", 12)
        self.lblframe=LabelFrame(self.window4, bd=3, relief=RIDGE, text="New Rooms Add").place(x=10, y=60, width=580, height=345)

        self.cust_name = Label(self.window4, text="Floor :", font=font2, bg="black", fg="gold")
        self.cust_name.place(x=30, y=100)
        self.t1 = Entry(self.window4)
        self.t1.place(x=120, y=105)

        self.room_no = Label(self.window4, text="Room No. :", font=font2, bg="black", fg="gold")
        self.room_no.place(x=30, y=160)
        self.t2 = Entry(self.window4)
        self.t2.place(x=140, y=165)

        self.room_type = Label(self.window4, text="Room Type :", font=font2, bg="black", fg="gold")
        self.room_type.place(x=30, y=220)
        self.v1 = StringVar()
        self.c1 = Combobox(self.window4, values=["Single Bedroom", "Double Bedroom", "Deluxe Bedroom"], textvariable=self.v1)
        self.c1.place(x=140, y=223)

        self.room_status = Label(self.window4, text="Room Status :", font=font2, bg="black", fg="gold")
        self.room_status.place(x=30, y=280)
        self.v2 = StringVar()
        self.c2 = Combobox(self.window4, values=["Available", "Occupied"],
                           textvariable=self.v2)
        self.c2.place(x=140, y=283)

        self.b1=Button(self.window4, text="SAVE", bg="black", fg="gold", font=font2, borderwidth=6, command=self.saveData).place(x=100, y=340)
        self.b2=Button(self.window4, text="UPDATE", bg="black", fg="gold", font=font2, borderwidth=6, command=self.updateData).place(x=200, y=340)
        self.b3=Button(self.window4, text="DELETE", bg="black", fg="gold", font=font2, borderwidth=6, command=self.deleteData).place(x=320, y=340)
        self.b4=Button(self.window4, text="FETCH", bg="black", fg="gold", font=font2, borderwidth=6, command=self.fetchData).place(x=435, y=340)
        self.fetchAllData()

        self.img1 = Image.open(r"my_images/Double.png")
        self.img1 = self.img1.resize((280, 240))
        self.photo = ImageTk.PhotoImage(self.img1)
        self.lblimg = Label(self.window4, image=self.photo, bd=4, relief=RIDGE)
        self.lblimg.place(x=300, y=80, width=280, height=240)

        self.window4.mainloop()

                       #--------------------Connecting Database------------
    def databaseConnection(self):
        myhost="localhost"
        mydb="hotelmgtdb"
        myuser="root"
        mypassword=""
        try:
            self.conn=pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr=self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting database \n" + str(e), parent=self.window4)

                     #--------------------Saving Data--------------------
    def saveData(self):
        self.databaseConnection()
        try:
            myqry= 'insert into rooms values (%s,%s,%s,%s)'
            rowcount=self.curr.execute(myqry,(self.t1.get(),self.t2.get(),self.v1.get(),self.v2.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","New Room Added successfully", parent=self.window4)
            else:
                messagebox.showinfo("Failure","Check all fields carefully", parent=self.window4)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion: " + str(e), parent=self.window4)
        self.clearPage()
        self.fetchAllData()

    #           #--------------------Fetching Data----------------------
    def fetchData(self,val=NONE):
        if val == None:
            roomnumber = self.t2.get()
        else:
            roomnumber = val
        self.databaseConnection()
        try:
            myqry = "select * from rooms where roomnumber=%s"
            rowcount = self.curr.execute(myqry, (roomnumber))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0, data[0])
                self.t2.insert(0, data[1])
                self.v1.set(data[2])
                self.v2.set(data[3])
            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window4)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n" + str(e), parent=self.window4)

                    #--------------------Clearing Page------------------
    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.v1.set(None)
        self.v2.set(None)
        self.c1.set("Choose Room Type")
        self.c2.set("Choose Room Status")
                    #---------------------Updating Data------------------
    def updateData(self):
        self.databaseConnection()
        try:
            myqry= "update rooms set floor=%s, roomtype=%s, roomstatus=%s where roomnumber=%s"
            rowcount=self.curr.execute(myqry,(self.t1.get(),self.v1.get(),self.v2.get(),self.t2.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Room Data Updated successfully", parent=self.window4)
            else:
                messagebox.showinfo("Failure","Check all fields carefully", parent=self.window4)
        except Exception as e:
            messagebox.showerror("Query Error","Error while updation: " + str(e), parent=self.window4)
        self.clearPage()
        self.fetchAllData()

    #---------------Deleting Data-----------
    def deleteData(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to delete ??", parent=self.window4)
        if ans == "yes":
            self.databaseConnection()
            try:
                myqry = "delete from rooms where roomnumber=%s"
                rowcount = self.curr.execute(myqry, (self.t2.get()))
                self.conn.commit()
                if rowcount == 1:
                    messagebox.showinfo("Success", "Room Data Deleted successfully", parent=self.window4)
                    self.clearPage()
                else:
                    messagebox.showinfo("Failure", "Check all fields carefully", parent=self.window4)
            except Exception as e:
                messagebox.showerror("Query Error", "Error while deletion \n" + str(e), parent=self.window4)
        self.fetchAllData()

    def getSelectedRowData(self):
        id = self.mytable.focus()
        data = self.mytable.item(id)
        content = data['values']
        col1 = content[1]
        self.fetchData(col1)

    def fetchAllData(self):
        self.databaseConnection()
        try:
            myqry = "select * from rooms where floor like %s"
            rowcount = self.curr.execute(myqry, (self.t1.get() + "%"))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            if data:
                for row in data:
                    self.mytable.insert("", END, values=row)
            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window4)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n" + str(e), parent=self.window4)


if __name__=='__main__':
    dummy_homepage = Tk()
    page4(dummy_homepage)
    dummy_homepage.mainloop()