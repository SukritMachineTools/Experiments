from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
class page3:
    def __init__(self,hwindow):
        self.window3=Toplevel(hwindow)
        self.window3.geometry("%dx%d+%d+%d" % (1116, 445, 242, 252))
        self.window3.config(bg="white")
        self.window3.title("Customer Booking")
        self.lbltitle=Label(self.window3, text="Customer Booking", font=("times new roman", 20, "bold"), bg ="black", fg ="gold", bd = 4, relief = RIDGE).place(x=0, y=0, width=1116, height=40)
        # ------------------ table ---------------------------------------
        self.tablearea = Frame(self.window3)
        self.scroll_y = Scrollbar(self.tablearea, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.mytable = Treeview(self.tablearea, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'], height=10, yscrollcommand=self.scroll_y.set)
        self.scroll_y.config(command=self.mytable.yview)
        self.mytable.heading("c1", text="Customer Name")
        self.mytable.heading("c2", text="Customer Phone")
        self.mytable.heading("c3", text="Customer Email")
        self.mytable.heading("c4", text="Room Number")
        self.mytable.heading("c5", text="Id Proof Type")
        self.mytable.heading("c6", text="Id Number")
        self.mytable.heading("c7", text="Nationality")
        self.mytable.heading("c8", text="Customer Address")
        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=100, anchor='center')
        self.mytable.column("#2", width=100, anchor='center')
        self.mytable.column("#3", width=100, anchor='center')
        self.mytable.column("#4", width=100, anchor='center')
        self.mytable.column("#5", width=100, anchor='center')
        self.mytable.column("#6", width=100, anchor='center')
        self.mytable.column("#7", width=100, anchor='center')
        self.mytable.column("#8", width=80, anchor='center')
        self.mytable.pack()
        self.mytable.bind("<ButtonRelease-1>", lambda e: self.getSelectedRowData())
        self.tablearea.place(x=313,y=40)

        #------------------------Frame-------------------------
        self.lblframe=LabelFrame(self.window3, bd=3, relief=RIDGE, text="Customer Details").place(x=0, y=40, width=312, height=405)

        #------------------------Labels in Frame-------------------

        #------------Name--------
        font2=("times new roman",12)
        self.cust_name=Label(self.window3, text="Customer Name :", font=font2, bg="black", fg="gold")
        self.cust_name.place(x=5,y=60)
        self.t1=Entry(self.window3)
        self.t1.place(x=130,y=65)

        #----------PHONE------------
        self.cust_phone = Label(self.window3, text="Customer Phone No. :", font=font2, bg="black", fg="gold")
        self.cust_phone.place(x=5, y=100)
        self.t2 = Entry(self.window3)
        self.t2.place(x=160, y=105)

        #---------Email-------------
        self.cust_email = Label(self.window3, text="Customer Email :", font=font2, bg="black", fg="gold")
        self.cust_email.place(x=5, y=140)
        self.t3 = Entry(self.window3)
        self.t3.place(x=130, y=145)

        #---------Gender-----------
        self.room_number = Label(self.window3, text="Room Number :", font=font2, bg="black", fg="gold")
        self.room_number.place(x=5, y=180)
        self.t34 = Entry(self.window3)
        self.t34.place(x=130, y=185)

        #--------Proof Type------
        self.cust_proof = Label(self.window3, text="Id Proof Type :", font=font2, bg="black", fg="gold")
        self.cust_proof.place(x=5, y=220)
        self.v2 = StringVar()
        self.c1=Combobox(self.window3, values=["Adhaar Card", "Pan Card", "Driving License"], textvariable=self.v2)
        self.c1.place(x=120,y=225)

        #-------ID Number------
        self.cust_proof_num = Label(self.window3, text="Id Number :", font=font2, bg="black", fg="gold")
        self.cust_proof_num.place(x=5, y=260)
        self.t4=Entry(self.window3)
        self.t4.place(x=100,y=265)

        #-------Nationality------
        self.cust_nationality = Label(self.window3, text="Customer Nationality :", font=font2, bg="black", fg="gold")
        self.cust_nationality.place(x=5, y=300)
        self.t5 = Entry(self.window3)
        self.t5.place(x=150, y=305)

        #-------Address--------
        self.cust_address = Label(self.window3, text="Customer Address:-", font=font2, bg="black", fg="gold")
        self.cust_address.place(x=5, y=340)
        self.t6 = Text(self.window3,width=37,height=4)
        self.t6.place(x=5, y=369)


        #-------------Buttons------------
        self.b1=Button(self.window3, text="SAVE", bg="black", fg="gold", font=font2, borderwidth=6, command=self.saveData).place(x=400, y=369)
        self.b2=Button(self.window3, text="UPDATE", bg="black", fg="gold", font=font2, borderwidth=6, command=self.updateData).place(x=500, y=369)
        self.b3=Button(self.window3, text="FETCH", bg="black", fg="gold", font=font2, borderwidth=6, command=self.fetchData).place(x=620, y=369)
        self.b4=Button(self.window3, text="DELETE", bg="black", fg="gold", font=font2, borderwidth=6, command=self.deleteData).place(x=720, y=369)
        self.b5=Button(self.window3, text="SEARCH", bg="black", fg="gold", font=font2, borderwidth=6, command=self.fetchAllData).place(x=840, y=369)

        self.window3.mainloop()

        # --------------------Connecting Database------------
    def databaseConnection(self):
        myhost="localhost"
        mydb="hotelmgtdb"
        myuser="root"
        mypassword=""
        try:
            self.conn=pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr=self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting database \n" + str(e), parent=self.window3)

    # --------------------Saving Data--------------------
    def saveData(self):
        if self.validate_check()==False:
            return
        self.databaseConnection()
        try:
            myqry= 'insert into hotel values (%s,%s,%s,%s,%s,%s,%s,%s)'
            rowcount=self.curr.execute(myqry,(self.t1.get(),self.t2.get(),self.t3.get(),self.t34.get(),self.v2.get(),self.t4.get(),self.t5.get(),self.t6.get("1.0",END)))
            self.conn.commit()

            myqry2 ="update rooms set roomstatus=%s where roomnumber=%s"
            rowcount2 = self.curr.execute(myqry2,("Occupied",self.t34.get()))
            self.conn.commit()


            if rowcount==1:
                messagebox.showinfo("Success","Student Data saved successfully", parent=self.window3)
            else:
                messagebox.showinfo("Failure","Check all fields carefully", parent=self.window3)
        except Exception as e:
            messagebox.showerror("Query Error","Error while insertion: " + str(e), parent=self.window3)
        self.clearPage()

    #-------------FetchingData----------------
    def fetchData(self,val=NONE):
        if val == None:
            customerphone = self.t2.get()
        else:
            customerphone = val
        self.databaseConnection()
        try:
            myqry = "select * from hotel where customerphone=%s"
            rowcount = self.curr.execute(myqry, (customerphone))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0, data[0])
                self.t2.insert(0, data[1])
                self.t3.insert(0, data[2])
                self.t34.insert(0, data[3])
                self.v2.set(data[4])
                self.t4.insert(0,data[5])
                self.t5.insert(0,data[6])
                self.t6.insert('1.0', data[7])
            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window3)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n" + str(e), parent=self.window3)

    # ---------------------Updating Data------------------
    def updateData(self):
        if self.validate_check() == False:
            return
        self.databaseConnection()
        try:
            myqry= "update hotel set customername=%s, customeremail=%s, roomnumber=%s, idproof=%s, idnumber=%s, nationality=%s, customeraddress=%s where customerphone=%s"
            rowcount=self.curr.execute(myqry,(self.t1.get(),self.t3.get(),self.t34.get(),self.v2.get(),self.t4.get(),self.t5.get(),self.t6.get("1.0",END),self.t2.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Student Data Updated successfully", parent=self.window3)
            else:
                messagebox.showinfo("Failure","Check all fields carefully", parent=self.window3)
        except Exception as e:
            messagebox.showerror("Query Error","Error while updation: " + str(e), parent=self.window3)
        self.clearPage()

    # --------------------Clearing Data------------------
    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)
        self.t34.delete(0, END)
        self.v2.set(None)
        self.t4.delete(0, END)
        self.t5.delete(0, END)
        self.t6.delete('1.0', END)
        self.c1.set("Choose Id type")

    #-----------------Delete Data------------------
    def deleteData(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to delete ??", parent=self.window3)
        if ans == "yes":
            self.databaseConnection()
            try:
                myqry = "delete from hotel where customerphone=%s"
                rowcount = self.curr.execute(myqry, (self.t2.get()))
                self.conn.commit()
                if rowcount == 1:
                    messagebox.showinfo("Success", "Student Data Deleted successfully", parent=self.window3)
                    self.clearPage()
                else:
                    messagebox.showinfo("Failure", "Check all fields carefully", parent=self.window3)
            except Exception as e:
                messagebox.showerror("Query Error", "Error while deletion \n" + str(e), parent=self.window3)

    #----------Validation Check----------------
    def validate_check(self):
        if not (self.t1.get().isalpha()) or len(self.t1.get()) < 2:
            messagebox.showwarning("Validation Check", "Invalid Name", parent=self.window3)
            return False
        elif not (self.t2.get().isdigit()) or len(self.t2.get()) < 10:
            messagebox.showwarning("Validation Check","Enter valid phone no \n10 digits only", parent=self.window3)
            return False
        elif len(self.t3.get()) <4:
            messagebox.showwarning("Validation Check", "Enter valid email", parent=self.window3)
            return False
        elif len(self.t3.get()) <2:
            messagebox.showwarning("Input Error", "Please Select Room Number ", parent=self.window3)
            return False
        elif (self.v2.get() == "Choose Id Proof") or (self.v2.get() == "No Id Proof"):
            messagebox.showwarning("Input Error", "Please Select Id Proof Type ", parent=self.window3)
            return False
        elif len(self.t4.get()) <16:
            messagebox.showwarning("Input Error", "Please enter valid id ", parent=self.window3)
            return False
        elif len(self.t5.get()) <2:
            messagebox.showwarning("Input Error", "Please enter valid nationality ", parent=self.window3)
            return False
        elif len(self.t6.get('1.0', END)) < 3:
            messagebox.showwarning("Input Error", "Please Enter Address ", parent=self.window3)
            return False
        return True

    def getSelectedRowData(self):
        id = self.mytable.focus()
        data = self.mytable.item(id)
        content = data['values']
        col1 = content[1]
        self.fetchData(col1)

    def fetchAllData(self):
        self.databaseConnection()
        try:
            myqry = "select * from hotel where customername like %s"
            rowcount = self.curr.execute(myqry, (self.t1.get() + "%"))
            data = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            if data:
                for row in data:
                    self.mytable.insert("", END, values=row)
            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window3)
        except Exception as e:
            messagebox.showerror("Query Error", "Error while insertion \n" + str(e), parent=self.window3)



if __name__=='__main__':
    dummy_homepage = Tk()
    page3(dummy_homepage)
    dummy_homepage.mainloop()