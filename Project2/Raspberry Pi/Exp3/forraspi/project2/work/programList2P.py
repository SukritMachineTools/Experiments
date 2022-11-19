from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import time
import threading
from initialP import home
from databaseP import database
import csv
import os

class programList2():

    def pglistFrame(self):
        self.root = home.start(self)
        mydb, mycursor, myresult = database.pgdb(self)

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
        def prog():
            self.root.destroy()
            from programP import program
            pg=program()
            pg.programFrame()
            pass

        def csvread(pno):
            f = '/home/pi/Desktop/dirs/Servo Electric PressBrake/ProgramList/Program' + str(pno) + '.csv'
            try:
                with open(f, 'r') as file:
                    reader = csv.reader(file)
                    l = list()
                    for row in reader:
                        # print(row)
                        l.append(row)
                    # print(l)
                    pgNo = l[0]
                    pgName = l[1]
                    thick = l[2]
                    noBend = l[3]
                    punchNo = l[4]
                    dieNo = l[5]
                    materialNo = l[6]
                    res = l[7]
                    # print(l)
                    # print(pgNo[1], pgName[1], thick[1], noBend[1], punchNo[1], dieNo[1],materialNo[1],res[1])

            except:
                pgNo = ['Pg No', 0]
                pgName = ['PgName', 'NaN']
                thick = ['Thick', 0]
                noBend = ['No of Bend', 0]
                punchNo = ['Punch No', 0]
                dieNo = ['Die No', 0]
                materialNo = ['Material No', 0]
                res = ['Res', 0]

            return pgNo[1], pgName[1], thick[1], noBend[1], punchNo[1], dieNo[1], materialNo[1], res[1]

        def csvw():
            try:
                mydb, mycursor, myresult = database.pgdb(self)
                x = "ProgramList"
                directory = "Servo Electric PressBrake"
                # Parent Directory path
                parent_dir = "/home/pi/Desktop/dirs"

                # Path
                path = os.path.join(parent_dir, directory,x)

                newpath = path
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                    print("Directory '% s' created" % directory)

                print(path)

                k = path + "/ProgramList.csv"
                with open(k, 'w', newline='') as file:
                    f = ['No.', 'Program Name', 'Thick', 'No. of Bend', 'Punch','Die','Material', 'Res']
                    w = csv.DictWriter(file, fieldnames=f)
                    w.writeheader()

                    i = 0
                    while i < 10:
                        # print(myresult[i])
                        yy = myresult[i]
                        # print(yy)
                        n = yy[0]
                        pn = yy[1]
                        t = yy[2]
                        nb = yy[3]
                        p = yy[4]
                        d = yy[5]
                        m = yy[6]
                        r = yy[7]
                        #print(n, pn, ph, pa, pr)
                        rl = [{'No.': n, 'Program Name': pn, 'Thick': t, 'No. of Bend': nb, 'Punch': p,'Die':d,'Material':m,'Res':r}]
                        w.writerows(rl)
                        i += 1
            except Exception as e:
                print(e)
            pass

        frame1 = Frame(self.root, highlightbackground="blue", highlightthickness=1, bg="#b3ffe0")
        logoimg = ImageTk.PhotoImage(
            Image.open('sukrit_Logo.png').resize((150, 70), Image.LANCZOS))
        Label(frame1, image=logoimg, bg="#b3ffe0").grid(row=0, column=0)
        Label(frame1, text="            ", font="Algerian 27 bold", padx=4.5, pady=4.5, bg="#b3ffe0").grid(row=0,
                                                                                                              column=1,
                                                                                                              padx=10)
        Label(frame1, text="Program List-2",fg="#cc3300", font="Algerian 27 bold", padx=4.5, pady=4.5, bg="#b3ffe0").grid(row=0, column=3,
                                                                                                        padx=10)
        Button(frame1, text="Export To CSV", bg="blue", fg="white", relief="groove", command=csvw).grid(row=0, column=4)
        frame1.grid(row=0, ipadx=50, sticky="ew")

        frame2 = Frame(self.root, bg="blue", height=10)
        frame2.grid(row=1, ipadx=400, sticky='ew')

        frame3 = Frame(self.root, highlightbackground="blue", width=300, height=100, highlightthickness=2, bg="#b3ffe0")

        try:
            mydb, mycursor, myresult = database.pgdb(self)
            rs1 = myresult[0]
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

        Label(frame3, text="No.", font="Stencil 15 bold", padx=12, pady=10, bg="#ccffff", fg="#e68a00").grid(row=0,
                                                                                                            column=0)
        Label(frame3, text="Name", font="Stencil 15 bold", padx=12, pady=10, bg="#ccffff", fg="#e68a00").grid(row=0,
                                                                                                            column=1)
        Label(frame3, text="Thick", font="Stencil 15 bold", padx=12, pady=10, bg="#ccffff", fg="#e68a00").grid(row=0,
                                                                                                            column=2)
        Label(frame3, text="No. of Bend", font="Stencil 15 bold", padx=12, pady=10, bg="#ccffff", fg="#e68a00").grid(row=0,
                                                                                                            column=3)
        Label(frame3, text="Punch", font="Stencil 15 bold", padx=12, pady=10, bg="#ccffff", fg="#e68a00").grid(row=0,
                                                                                                            column=4)
        Label(frame3, text="Die", font="Stencil 15 bold", padx=12, pady=10, bg="#ccffff", fg="#e68a00").grid(row=0,
                                                                                                            column=5)
        Label(frame3, text="Material", font="Stencil 15 bold", padx=12, pady=10, bg="#ccffff", fg="#e68a00").grid(row=0,
                                                                                                            column=6)
        Label(frame3, text="Res", font="Stencil 15 bold", padx=12, pady=10, bg="#ccffff", fg="#e68a00").grid(row=0,
                                                                                                            column=7)

        Button(frame3, text="6", font="Stencil 12 bold", padx=12, pady=10, bg="#b3ffe0",fg="#e68a00").grid(row=1, column=0)


        pgNo,pgName,thick,noBend,punchNo,dieNo,materialNo,res=csvread(6)
        pln6 = StringVar()
        pln6.set(pgName)
        th6 = StringVar()
        th6.set(thick)
        nob6 = StringVar()
        nob6.set(noBend)
        pun6 = StringVar()
        pun6.set(punchNo)
        die6 = StringVar()
        die6.set(dieNo)
        mat6 = StringVar()
        mat6.set(materialNo)
        res6 = StringVar()
        res6.set(res)

        Label(frame3, textvariable=pln6, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=1, column=1)
        Label(frame3, textvariable=th6, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=1, column=2)
        Label(frame3, textvariable=nob6, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=1, column=3)
        Label(frame3, textvariable=pun6, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=1, column=4)
        Label(frame3, textvariable=die6, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=1, column=5)
        Label(frame3, textvariable=mat6, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=1, column=6)
        Label(frame3, textvariable=res6, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=1, column=7)

        Button(frame3, text="7", font="Stencil 12 bold", padx=12, pady=10, bg="#b3ffe0",fg="#e68a00").grid(row=2, column=0)

        pgNo,pgName,thick,noBend,punchNo,dieNo,materialNo,res=csvread(7)
        pln7 = StringVar()
        pln7.set(pgName)
        th7 = StringVar()
        th7.set(thick)
        nob7 = StringVar()
        nob7.set(noBend)
        pun7 = StringVar()
        pun7.set(punchNo)
        die7 = StringVar()
        die7.set(dieNo)
        mat7 = StringVar()
        mat7.set(materialNo)
        res7 = StringVar()
        res7.set(res)
        Label(frame3, textvariable=pln7, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=2, column=1)
        Label(frame3, textvariable=th7, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=2, column=2)
        Label(frame3, textvariable=nob7, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=2, column=3)
        Label(frame3, textvariable=pun7, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=2, column=4)
        Label(frame3, textvariable=die7, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=2, column=5)
        Label(frame3, textvariable=mat7, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=2, column=6)
        Label(frame3, textvariable=res7, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=2, column=7)

        Button(frame3, text="8", font="Stencil 12 bold", padx=12, pady=10, bg="#b3ffe0",fg="#e68a00").grid(row=3, column=0)
        pgNo,pgName,thick,noBend,punchNo,dieNo,materialNo,res=csvread(8)
        pln8 = StringVar()
        pln8.set(pgName)
        th8 = StringVar()
        th8.set(thick)
        nob8 = StringVar()
        nob8.set(noBend)
        pun8 = StringVar()
        pun8.set(punchNo)
        die8 = StringVar()
        die8.set(dieNo)
        mat8 = StringVar()
        mat8.set(materialNo)
        res8 = StringVar()
        res8.set(res)
        Label(frame3, textvariable=pln8, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=3, column=1)
        Label(frame3, textvariable=th8, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=3, column=2)
        Label(frame3, textvariable=nob8, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=3, column=3)
        Label(frame3, textvariable=pun8, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=3, column=4)
        Label(frame3, textvariable=die8, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=3, column=5)
        Label(frame3, textvariable=mat8, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=3, column=6)
        Label(frame3, textvariable=res8, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=3, column=7)

        Button(frame3, text="9", font="Stencil 12 bold", padx=12, pady=10, bg="#b3ffe0",fg="#e68a00").grid(row=4, column=0)
        pgNo,pgName,thick,noBend,punchNo,dieNo,materialNo,res=csvread(9)
        pln9 = StringVar()
        pln9.set(pgName)
        th9 = StringVar()
        th9.set(thick)
        nob9 = StringVar()
        nob9.set(noBend)
        pun9 = StringVar()
        pun9.set(punchNo)
        die9 = StringVar()
        die9.set(dieNo)
        mat9 = StringVar()
        mat9.set(materialNo)
        res9 = StringVar()
        res9.set(res)
        Label(frame3, textvariable=pln9, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=4, column=1)
        Label(frame3, textvariable=th9, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=4, column=2)
        Label(frame3, textvariable=nob9, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=4, column=3)
        Label(frame3, textvariable=pun9, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=4, column=4)
        Label(frame3, textvariable=die9, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=4, column=5)
        Label(frame3, textvariable=mat9, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=4, column=6)
        Label(frame3, textvariable=res9, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=4, column=7)

        Button(frame3, text="10", font="Stencil 12 bold", padx=12, pady=10, bg="#b3ffe0",fg="#e68a00").grid(row=5, column=0)
        pgNo,pgName,thick,noBend,punchNo,dieNo,materialNo,res=csvread(10)
        pln10 = StringVar()
        pln10.set(pgName)
        th10 = StringVar()
        th10.set(thick)
        nob10 = StringVar()
        nob10.set(noBend)
        pun10 = StringVar()
        pun10.set(punchNo)
        die10 = StringVar()
        die10.set(dieNo)
        mat10 = StringVar()
        mat10.set(materialNo)
        res10 = StringVar()
        res10.set(res)
        Label(frame3, textvariable=pln10, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=5, column=1)
        Label(frame3, textvariable=th10, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=5, column=2)
        Label(frame3, textvariable=nob10, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=5, column=3)
        Label(frame3, textvariable=pun10, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=5, column=4)
        Label(frame3, textvariable=die10, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=5, column=5)
        Label(frame3, textvariable=mat10, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=5, column=6)
        Label(frame3, textvariable=res10, font="Calibri 12 bold", padx=12, pady=10, bg="#b3ffe0").grid(row=5, column=7)

        frame3.grid(row=2, column=0, ipadx=33.5, sticky="ew")

        frame5 = Frame(self.root, bg="blue", height=10)
        frame5.grid(row=3, ipadx=150, sticky='ew')

        frame6 = Frame(self.root, highlightbackground="blue", highlightthickness=0, bg="#b3ffe0")
        homeimg = ImageTk.PhotoImage(
            Image.open('home.png').resize((130, 80), Image.LANCZOS))
        # settinglabel=Label(frame6,image=settingimg).grid(row=0,column=0,padx=50)
        Button(frame6, image=homeimg, command=pBrake,highlightthickness=0,borderwidth=0, bg="#b3ffe0").grid(row=0, column=2, padx=15)


        lrimg = ImageTk.PhotoImage(
            Image.open('arrow1.png').resize((130, 80), Image.LANCZOS))
        # pdlabel=Label(frame6,image=pdimg).grid(row=0,column=1,padx=50,columnspan=2)
        Button(frame6, image=lrimg, command=pgList,highlightthickness=0,borderwidth=0, bg="#b3ffe0").grid(row=0, column=0, padx=15)
        pgimg = ImageTk.PhotoImage(
            Image.open('program.png').resize((130, 80), Image.LANCZOS))
        Button(frame6, image=pgimg, command=prog,highlightthickness=0,borderwidth=0,  bg="#b3ffe0").grid(row=0, column=4, padx=15,ipadx=5)
        frame6.grid(row=4, ipadx=20, sticky='ew')

        self.root.mainloop()

if __name__=='__main__':
    prlt=programList2()
    prlt.pglistFrame()