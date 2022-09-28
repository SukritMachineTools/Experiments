import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
from PIL import Image,ImageTk


class page5:
    def __init__(self,hwindow):
        self.window5=Toplevel(hwindow)
        self.window5.geometry("%dx%d+%d+%d" % (1116, 445, 242, 252))
        self.window5.config(bg="white")
        self.window5.title("Room Adding")
        self.lbltitle = Label(self.window5, text="Room Check-Out Department", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE).place(x=0, y=0, width=1116, height=40)


        # ------------------------Frame-------------------------
        self.lblframe = LabelFrame(self.window5, bd=3, relief=RIDGE, text="Bill Details").place(x=0, y=40, width=350, height=405)


        # ------------------------Labels in Frame-------------------
        # ------------phone no.--------
        font2 = ("times new roman", 10)
        self.cust_phone = Label(self.window5, text="Customer Phone No. :", font=font2, bg="black", fg="gold")
        self.cust_phone.place(x=5, y=60)
        self.t1 = Entry(self.window5)
        self.t1.place(x=140, y=60)

        # ----------check_in------------
        self.check_in = Label(self.window5, text="Check in Date:", font=font2, bg="black", fg="gold")
        self.check_in.place(x=5, y=90)
        self.t2 = Entry(self.window5)
        self.t2.place(x=120, y=90)

        #___________check_out----------
        self.check_out = Label(self.window5, text="Check out Date:", font=font2, bg="black", fg="gold")
        self.check_out.place(x=5, y=120)
        self.t3 = Entry(self.window5)
        self.t3.place(x=120, y=120)

        # ___________room_type----------
        self.room_type = Label(self.window5, text="Room Type:", font=font2, bg="black", fg="gold")
        self.room_type.place(x=5, y=150)
        self.v1 = StringVar()
        self.c1 = Combobox(self.window5, values=["Single Bed Room", "Double Bed Room", "Luxury Bed Room"], textvariable=self.v1)
        self.c1.place(x=120, y=150)


        # --------room_number------
        self.room_number = Label(self.window5, text="Room Number :", font=font2, bg="black", fg="gold")
        self.room_number.place(x=5, y=180)
        self.t4 = Entry(self.window5)
        self.t4.place(x=120, y=180)


        # ___________no.of days----------
        self.days = Label(self.window5, text="No. of Days:", font=font2, bg="black", fg="gold")
        self.days.place(x=5, y=210)
        self.t5 = Entry(self.window5)
        self.t5.place(x=120, y=210)


        # -------tax------
        self.tax = Label(self.window5, text="Paid Tax:", font=font2, bg="black", fg="gold")
        self.tax.place(x=5, y=240)
        self.t6 = Entry(self.window5)
        self.t6.place(x=120, y=240)


        # -------sub_total--------
        self.total = Label(self.window5, text="Sub Total:", font=font2, bg="black", fg="gold")
        self.total.place(x=5, y=270)
        self.t7 = Entry(self.window5)
        self.t7.place(x=120, y=270)


        # ___________bill----------
        self.total_bill = Label(self.window5, text="Total Bill:", font=font2, bg="black", fg="gold")
        self.total_bill.place(x=5, y=300)
        self.t8=Entry(self.window5)
        self.t8.place(x=120, y=300)

        # -------------Buttons------------
        self.b1 = Button(self.window5, text="SAVE", bg="black", fg="gold", font=font2, borderwidth=6, command=self.saveData).place(x=20, y=390)
        self.b2 = Button(self.window5, text="UPDATE", bg="black", fg="gold", font=font2, borderwidth=6, ).place(x=85, y=390)
        self.b3 = Button(self.window5, text="FETCH", bg="black", fg="gold", font=font2, borderwidth=6, command=self.fetch_contact).place(x=280, y=60)
        self.b4 = Button(self.window5, text="DELETE", bg="black", fg="gold", font=font2, borderwidth=6, command=self.deleteData).place(x=165, y=390)
        self.b5 = Button(self.window5, text="SEARCH", bg="black", fg="gold", font=font2, borderwidth=6, command=self.fetchAllData).place(x=245, y=390)
        self.b6 = Button(self.window5, text="BILL", bg="black", fg="gold", font=font2, borderwidth=6, padx=20,command=self.bill).place(x=60, y=340)
        self.b7 = Button(self.window5, text="PRINT BILL", bg="black", fg="gold", font=font2, borderwidth=6, padx=20,command=self.printdata).place(x=180, y=340)

        self.tablearea = LabelFrame(self.window5, bd=3, relief=RIDGE, text="View Details")
        self.scroll_y=Scrollbar(self.tablearea,orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.mytable = Treeview(self.tablearea, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'], height=8,yscrollcommand=self.scroll_y.set)
        self.scroll_y.config(command=self.mytable.yview)
        self.mytable.heading("c1", text="Contact")
        self.mytable.heading("c2", text="Check-in")
        self.mytable.heading("c3", text="Check-out")
        self.mytable.heading("c4", text="Room Type")
        self.mytable.heading("c5", text="No. of Days")
        self.mytable.heading("c6", text="Paid Tax")
        self.mytable.heading("c7", text="Total Bill")
        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=110, anchor='center')
        self.mytable.column("#2", width=110, anchor='center')
        self.mytable.column("#3", width=110, anchor='center')
        self.mytable.column("#4", width=110, anchor='center')
        self.mytable.column("#5", width=100, anchor='center')
        self.mytable.column("#6", width=100, anchor='center')
        self.mytable.column("#7", width=100, anchor='center')
        self.mytable.bind("<ButtonRelease-1>", lambda e: self.getSelectedRowData())

        self.mytable.pack()
        self.tablearea.place(x=350, y=240)

        self.lblframe=LabelFrame(self.window5, bd=3, relief=RIDGE, text="Customer Details").place(x=350, y=40, width=300, height=198)

        self.img1 = Image.open(r"my_images/Ramadamain.png")
        self.img1 = self.img1.resize((350, 200))
        self.photo = ImageTk.PhotoImage(self.img1)
        self.lblimg = Label(self.window5, image=self.photo, bd=4, relief=RIDGE)
        self.lblimg.place(x=700, y=40, width=350, height=200)

        self.window5.mainloop()

    def databaseConnection(self):
        myhost = "localhost"
        mydb = "hotelmgtdb"
        myuser = "root"
        mypassword = ""
        self.conn = pymysql.connect(host=myhost, db=mydb, user=myuser, password=mypassword)
        self.curr = self.conn.cursor()


    def fetch_contact(self):
        if self.t1.get()=="":
            messagebox.showerror("Error","Please Enter Valid Contact Number", parent=self.window5)
        else:
            self.databaseConnection()
            query=("select * from hotel where customerphone=%s")
            value=(self.t1.get(),)
            self.curr.execute(query,value)
            row=self.curr.fetchone()

            if row==None:
                messagebox.showerror("Error","Number Not Found", parent=self.window5)
            else:
                self.conn.commit()
                self.conn.close()

                self.lablname=Label(self.window5,text="Name:",font=("arial",10,"bold"))
                self.lablname.place(x=370,y=60)
                self.lbl1 = Label(self.window5, text=row[0], font=("arial", 10, "bold"))
                self.lbl1.place(x=450, y=60)

                self.lablemail = Label(self.window5, text="Email:", font=("arial", 10, "bold"))
                self.lablemail.place(x=370, y=90)
                self.lbl2 = Label(self.window5, text=row[2], font=("arial", 10, "bold"))
                self.lbl2.place(x=450, y=90)

                self.t4.insert(0, row[3])

                self.lablnation = Label(self.window5, text="Nationality:", font=("arial", 10, "bold"))
                self.lablnation.place(x=370, y=120)
                self.lbl4 = Label(self.window5, text=row[6], font=("arial", 10, "bold"))
                self.lbl4.place(x=450, y=120)

                self.labladdress = Label(self.window5, text="ID proof:", font=("arial", 10, "bold"))
                self.labladdress.place(x=370, y=150)
                self.lbl5 = Label(self.window5, text=row[4], font=("arial", 10, "bold"))
                self.lbl5.place(x=450, y=150)


    def saveData(self):
        self.databaseConnection()
        try:
            myqry= 'insert into bill values (%s,%s,%s,%s,%s,%s,%s)'
            rowcount=self.curr.execute(myqry,(self.t1.get(),self.t2.get(),self.t3.get(),self.v1.get(),self.t5.get(),self.t6.get(),self.t8.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Data saved successfully", parent=self.window5)
            else:
                messagebox.showinfo("Failure","Check all fields carefully", parent=self.window5)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion: " + str(e), parent=self.window5)

    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)
        self.t4.delete(0, END)
        self.v1.set(None)
        self.t5.delete(0, END)
        self.t6.delete(0, END)
        self.t7.delete(0, END)
        self.t8.delete(0, END)

    def fetchAllData(self):
        self.databaseConnection()
        try:
            myqry = "select * from bill where contact like %s"
            rowcount = self.curr.execute(myqry, (self.t1.get() + "%"))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            if data:
                for row in data:
                    r1 = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
                    self.mytable.insert("", END, values=r1)
            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window5)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n" + str(e), parent=self.window5)

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to delete ??", parent=self.window5)
        if ans == "yes":
            self.databaseConnection()
            try:
                myqry = "delete from hotel where customerphone=%s"
                rowcount = self.curr.execute(myqry, (self.t1.get()))
                self.conn.commit()

                myqry2 = "update rooms set roomstatus=%s where roomnumber=%s"
                rowcount2 = self.curr.execute(myqry2, ("Available", self.t4.get()))
                self.conn.commit()

                if rowcount == 1:
                    messagebox.showinfo("Success", "Data Deleted successfully", parent=self.window5)
                    self.clearPage()
                else:
                    messagebox.showinfo("Failure", "Check all fields carefully", parent=self.window5)
            except Exception as e:
                messagebox.showerror("Query Error", "Error while deletion \n" + str(e), parent=self.window5)

    def printdata(self):
        from printout import my_cust_PDF
        pdf=my_cust_PDF()
        items_name=[[self.t1.get(),self.t2.get(),self.t3.get(),self.v1.get(),self.t5.get(),self.t6.get(),self.t8.get()]]
        quantity=['Contact', 'Check_in', 'Check_out', 'Room Type', 'Days Spent', 'PaidTax', 'Totalbill']
        pdf.print_chapter(items_name,quantity)

        pdf.output('pdf_file2.pdf')
        os.system('explorer.exe "pdf_file2.pdf"')

    def getSelectedRowData(self):
        id = self.mytable.focus()
        data = self.mytable.item(id)
        content = data['values']
        col1 = content[0]
        self.fetchData(col1)

    def fetchData(self,val=None):
        if val==None:
            un=self.t1.get()
        else:
            un=val
        self.databaseConnection()
        try:
            myqry = "select * from bill where contact=%s"
            rowcount = self.curr.execute(myqry,(un))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0, data[0])
                self.t2.insert(0, data[1])
                self.t3.insert(0, data[2])
                self.v1.set(data[3])
                self.t5.insert(0, data[4])
                self.t6.insert(0, data[5])
                self.t8.insert(0, data[6])
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window5)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion \n"+str(e),parent=self.window5)

    def bill(self):
        bill=int(self.t5.get())*1500
        tax=int(self.t5.get())*375
        total_bill=bill+tax
        self.t6.insert(0, (tax))
        self.t7.insert(0, (bill))
        self.t8.insert(0, total_bill)

if __name__=='__main__':
    dummy_homepage = Tk()
    page5(dummy_homepage)
    dummy_homepage.mainloop()