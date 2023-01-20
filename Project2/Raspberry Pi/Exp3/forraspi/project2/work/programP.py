from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import time
import threading
from initialP import home
from databaseP import database

class program():

    def programFrame(self):
        self.root = home.start(self)

        def pgList():
            self.root.destroy()
            from programListP import programList
            ol=programList()
            ol.pglistFrame()
            pass

        def pBrake():
            self.root.destroy()
            from pressBrakeP import pressBrake
            pb=pressBrake()
            pb.pressBrakeFrame()
            pass


        frame1 = Frame(self.root, highlightbackground="blue", highlightthickness=0, bg="#b3ffe0")
        logoimg = ImageTk.PhotoImage(
            Image.open('sukrit_Logo.png').resize((150, 70), Image.LANCZOS))
        Label(frame1, image=logoimg, bg="#b3ffe0").grid(row=0, column=0)
        Label(frame1, text="               ", font="Algerian 27 bold", padx=4.5, pady=4.5, bg="#b3ffe0").grid(row=0,
                                                                                                              column=1,
                                                                                                              padx=10)
        Label(frame1, text="Job Setup",fg="#cc3300", font="Algerian 27 bold", padx=4.5, pady=4.5, bg="#b3ffe0").grid(row=0,
                                                                                                               column=3,
                                                                                                               padx=10)
        frame1.grid(row=0, ipadx=50, sticky="ew")

        frame2 = Frame(self.root, bg="blue", height=15)
        frame2.grid(row=1, ipadx=400, sticky='ew')
        frame3 = Frame(self.root, highlightbackground="blue", width=300, height=100, highlightthickness=0, bg="#b3ffe0")
        try:
            mydb, mycursor, myresult = database.pgdb(self)
            mydbpn, mycursorpn, myresultpn =database.pndb(self)
            rs = myresult[0]
        except:
            mycursor = mydb.cursor()
            sql = """INSERT INTO programlist(PgNum,ProgName,Thick,NoOfBend,Punch,Die,Material,Res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            i = 1
            val = []
            while i < 11:
                val.append((i, "pgl", 0, 0, 0,0,0,0.0))
                i += 1

            mycursor.executemany(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            mycursor.execute("SELECT * FROM programlist")
            myresult = mycursor.fetchall()
            print(myresult)

        frame3i = Frame(frame3, highlightbackground="blue", highlightthickness=0, bg="#b3ffe0")

        Label(frame3i, text="No.", font="Calibri 10 bold", padx=12, pady=2, bg="#b3ffe0").grid(row=0, column=1)
        Label(frame3i, text="Name", font="Calibri 10 bold", padx=12, pady=2, bg="#b3ffe0").grid(row=0, column=2)
        Button(frame3i, text="Prog List", font="Calibri 10 bold", padx=12, pady=8,relief="ridge", bg="#ff9900").grid(row=1, column=0,pady=2,padx=2,ipadx=10)
        x=1
        rs = myresult[x]
        novalue1 = StringVar()
        novalue1.set(rs[0])
        Entry(frame3i, width=10, textvariable=novalue1, font="Arial_Black 12 bold", ).grid(row=1, column=1)
        namevalue1=StringVar()
        namevalue1.set(rs[1])
        Entry(frame3i, width=10, textvariable=namevalue1, font="Arial_Black 12 bold", ).grid(row=1, column=2)

        Button(frame3i, text="Punch List", font="Calibri 10 bold", padx=12, pady=8, relief="ridge", bg="#ff9900").grid(row=2, column=0,pady=2,padx=2,ipadx=6.3)
        novalue2 = StringVar()
        novalue2.set(rs[4])

        Entry(frame3i, width=10, textvariable=novalue2, font="Arial_Black 12 bold", ).grid(row=2, column=1)
        namevalue2 = StringVar()
        pnli=(rs[4],)
        mycursorpn.execute("SELECT PunchName FROM punchlist where num = %s",pnli)
        pnname = mycursorpn.fetchall()
        namevalue2.set(pnname)
        Entry(frame3i, width=10, textvariable=namevalue2, font="Arial_Black 12 bold", ).grid(row=2, column=2)

        Button(frame3i, text="Die List", font="Calibri 10 bold", padx=12, pady=8, relief="ridge", bg="#ff9900").grid(row=3, column=0,pady=2,padx=2,ipadx=14)
        novalue3 = StringVar()
        novalue3.set(rs[5])
        Entry(frame3i, width=10, textvariable=novalue3, font="Arial_Black 12 bold", ).grid(row=3, column=1)
        namevalue3 = StringVar()
        Entry(frame3i, width=10, textvariable=namevalue3, font="Arial_Black 12 bold", ).grid(row=3, column=2)

        Button(frame3i, text="Material List", font="Calibri 10 bold", padx=12, pady=8, relief="ridge", bg="#ff9900").grid(row=4, column=0,pady=2,padx=2)
        novalue4 = StringVar()
        novalue4.set(rs[6])
        Entry(frame3i, width=10, textvariable=novalue4, font="Arial_Black 12 bold", ).grid(row=4, column=1)
        namevalue4 = StringVar()
        Entry(frame3i, width=10, textvariable=namevalue4, font="Arial_Black 12 bold", ).grid(row=4, column=2)

        Button(frame3i, text="Sheet Thick", font="Calibri 10 bold", padx=12, pady=8, relief="ridge", bg="#ff9900").grid(row=5, column=0,pady=2,padx=2,ipadx=3)
        novalue5 = StringVar()
        novalue5.set(rs[2])
        Entry(frame3i, width=10, textvariable=novalue5, font="Arial_Black 12 bold", ).grid(row=5, column=1)
        namevalue5 = StringVar()
        Label(frame3i, width=10, text="mm", font="Arial_Black 12 bold",bg="#b3ffe0" ).grid(row=5, column=2)

        Button(frame3i, text="Bend Data", font="Calibri 10 bold", padx=12, pady=8, relief="ridge", bg="#ff9900").grid(row=6, column=0,pady=2,padx=2,ipadx=6)
        novalue6 = StringVar()
        novalue6.set(rs[3])
        Entry(frame3i, width=10, textvariable=novalue6, font="Arial_Black 12 bold", ).grid(row=6, column=1)
        namevalue6 = StringVar()
        Label(frame3i, width=10, text="Bend No.s", font="Arial_Black 12 bold", bg="#b3ffe0").grid(row=6, column=2)

        frame3i.grid(row=0, column=0, ipadx=33.5, sticky="w")
        frame3ii = Frame(frame3, highlightbackground="blue", highlightthickness=0, bg="#b3ffe0")
        dieimg = ImageTk.PhotoImage(
            Image.open('die.png').resize((170, 100), Image.LANCZOS))
        Label(frame3ii, image=dieimg, bg="#b3ffe0").grid()
        frame3ii.grid(row=0, column=1,sticky="n")

        frame3iii = Frame(frame3, highlightbackground="blue", highlightthickness=0, bg="#b3ffe0")
        lrimg = ImageTk.PhotoImage(
            Image.open('arrow1.png').resize((130, 80), Image.LANCZOS))
        Button(frame3iii, text="Save",font="Arial_Black 12 bold",borderwidth=5, bg="blue",fg="white").grid(row=0,padx=15, pady=15, ipadx=5)
        lrimg = ImageTk.PhotoImage(
            Image.open('arrow1.png').resize((130, 80), Image.LANCZOS))
        Button(frame3iii, text="Edit",font="Arial_Black 12 bold",borderwidth=5, bg="blue",fg="white").grid(row=1,padx=15, pady=15, ipadx=5)
        frame3iii.grid(row=0, column=2,sticky="n")
        frame3.grid(row=2, column=0, ipadx=33.5, sticky="ew")

        frame5 = Frame(self.root, bg="blue", height=15)
        frame5.grid(row=3, ipadx=150, sticky='ew')

        frame6 = Frame(self.root, highlightbackground="blue", highlightthickness=0, bg="#b3ffe0")

        pglimg = ImageTk.PhotoImage(
            Image.open('programlist.png').resize((130, 80), Image.LANCZOS))
        # settinglabel=Label(frame6,image=settingimg).grid(row=0,column=0,padx=50)
        Button(frame6, image=pglimg, command=pgList,highlightthickness=0,borderwidth=0, bg="#b3ffe0").grid(row=0, column=0, padx=15,sticky="e")
        Label(frame6,text="                                       ",bg="#b3ffe0").grid(row=0,column=1)
        Label(frame6,text="                                       ",bg="#b3ffe0").grid(row=0,column=2)
        Label(frame6,text="                                       ",bg="#b3ffe0").grid(row=0,column=3)


        homeimg = ImageTk.PhotoImage(
            Image.open('home.png').resize((130, 80), Image.LANCZOS))
        # pdlabel=Label(frame6,image=pdimg).grid(row=0,column=1,padx=50,columnspan=2)
        Button(frame6, image=homeimg, command=pBrake,highlightthickness=0,borderwidth=0, bg="#b3ffe0").grid(row=0, column=4, padx=15,sticky="w")
        frame6.grid(row=4, ipadx=20, sticky='ew')

        self.root.mainloop()

if __name__=='__main__':
    prg=program()
    prg.programFrame()