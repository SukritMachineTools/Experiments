from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from initialP import home
from databaseP import database
import csv
import os

class benddata():

    def bendframe(self):
        self.root=home.start(self)
        mydbBD, mycursorBD, myresultBD=database.bddb(self)

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
        def pgList():
            self.root.destroy()
            from programListP import programList
            ol=programList()
            ol.pglistFrame()
            pass
        def op():
            self.root.destroy()
            from operationP import operation
            o=operation()
            o.operationframe()
            pass
        def pnData():
            self.root.destroy()
            from punchDataP import punchData
            pdt=punchData()
            pdt.punchDataFrame()
            pass

        def csvw():
            try:
                mydbBD, mycursorBD, myresultBD = database.bddb(self)
                directory = "Servo Electric PressBrake"
                # Parent Directory path
                parent_dir = "/home/pi/Desktop/dirs/"

                # Path
                path = os.path.join(parent_dir, directory)

                newpath = path
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                    print("Directory '% s' created" % directory)

                print(path)

                k = newpath + "/BendData.csv"
                with open(k, 'w', newline='') as file:
                    f = ['No.', 'Prog. No.', 'Prog. Name','Angle','Bend No.', 'Length', 'Force','Back Gauge','Y-Axis', 'Retract', 'Angle Corr.', 'Opening', 'Bend Mov.', 'R position', 'Dwell']
                    w = csv.DictWriter(file, fieldnames=f)
                    w.writeheader()

                    i = 0
                    while i < 10:
                        # print(myresultBD[i])
                        yy = myresultBD[i]
                        # print(yy)
                        bn = yy[0]
                        pgno = yy[1]
                        pgn = yy[2]
                        ag = yy[3]
                        bd1 = yy[4]
                        bd2 = yy[5]
                        bd=str(bd1)+" / "+str(bd2)
                        lgt = yy[6]
                        fc = yy[7]
                        bg = yy[8]
                        ya = yy[9]
                        rt = yy[10]
                        ac = yy[11]
                        opn = yy[12]
                        bm = yy[13]
                        rp = yy[14]
                        dw = yy[15]
                        #print(bn,pgno,pgn,ag,bd1,bd2,lgt,fc,bg,ya,rt,ac,opn,bm,rp,dw)
                        rl = [{'No.': bn, 'Prog. No.':pgno, 'Prog. Name':pgn,'Angle':ag,'Bend No.':bd, 'Length':lgt, 'Force':fc,'Back Gauge':bg,'Y-Axis':ya, 'Retract':rt, 'Angle Corr.':ac, 'Opening':opn, 'Bend Mov.': bm, 'R position':rp, 'Dwell':dw}]
                        w.writerows(rl)
                        i += 1
            except Exception as e:
                print(e)
            pass

        def enterp2(event):
            update()

        def update():
            global bn
            pgno = pnovalue.get()
            ag = anglev.get()
            lgt = lengthv.get()
            bg = bgaugev.get()
            rt = retractv.get()
            opn = openingv.get()
            rp = rpositionv.get()
            pgn = pnamev.get()
            bdn=bendnov.get()
            bdnsplit=bdn.split("/")
            bd1 = bdnsplit[0]
            bd2 = bdnsplit[1]
            fc = forcev.get()
            ya = yaxisv.get()
            ac = acorrv.get()
            bm = bendmovv.get()
            dw = dwellv.get()
            try:
                sql = """UPDATE benddata SET ProgNo= %s, ProgName= %s, Angle= %s,Bend1= %s,Bend2= %s,Lengtth= %s, Forcee= %s, BackGauge= %s, YAxis= %s, Retract= %s, AngleCorr= %s, Opening= %s,BendMove= %s, RPosition= %s, Dwell= %s WHERE BdNum = %s;"""
                result = [pgno, pgn, ag, bd1, bd2, lgt, fc, bg, ya, rt, ac, opn, bm, rp, dw, bn]
                mycursorBD.execute(sql, result)
                mydbBD.commit()

            except Exception as e:
                print(e)

            pass

        def plus():
            global bn
            bn = bdno.get()
            bn = int(bn)
            if bn < 10:
                bn = bn + 1
                try:
                    sql = """SELECT * FROM benddata WHERE BdNum= %s"""
                    val = [bn]
                    mycursorBD.execute(sql, val)
                    myresult = mycursorBD.fetchall()
                    yy = myresult[0]
                    pgno = yy[1]
                    pnovalue.set(pgno)
                    ag = yy[3]
                    anglev.set(ag)
                    lgt = yy[6]
                    lengthv.set(lgt)
                    bg = yy[8]
                    bgaugev.set(bg)
                    rt = yy[10]
                    retractv.set(rt)
                    opn = yy[12]
                    openingv.set(opn)
                    rp = yy[14]
                    rpositionv.set(rp)
                    pgn = yy[2]
                    pnamev.set(pgn)
                    bd1 = yy[4]
                    bd2 = yy[5]
                    bendnov.set(str(bd1) + " / " + str(bd2))
                    fc = yy[7]
                    forcev.set(fc)
                    ya = yy[9]
                    yaxisv.set(ya)
                    ac = yy[11]
                    acorrv.set(ac)
                    bm = yy[13]
                    bendmovv.set(bm)
                    dw = yy[15]
                    dwellv.set(dw)

                except Exception as e:
                    print(e)
                bn = str(bn)
                bdno.set(bn)

            pass

        def minus():
            global bn
            bn = bdno.get()
            bn = int(bn)
            if bn > 1:
                bn = bn - 1
                try:
                    sql = """SELECT * FROM benddata WHERE BdNum= %s"""
                    val = [bn]
                    mycursorBD.execute(sql, val)
                    myresult = mycursorBD.fetchall()
                    yy = myresult[0]
                    pgno = yy[1]
                    pnovalue.set(pgno)
                    ag = yy[3]
                    anglev.set(ag)
                    lgt = yy[6]
                    lengthv.set(lgt)
                    bg = yy[8]
                    bgaugev.set(bg)
                    rt = yy[10]
                    retractv.set(rt)
                    opn = yy[12]
                    openingv.set(opn)
                    rp = yy[14]
                    rpositionv.set(rp)
                    pgn = yy[2]
                    pnamev.set(pgn)
                    bd1 = yy[4]
                    bd2 = yy[5]
                    bendnov.set(str(bd1) + " / " + str(bd2))
                    fc = yy[7]
                    forcev.set(fc)
                    ya = yy[9]
                    yaxisv.set(ya)
                    ac = yy[11]
                    acorrv.set(ac)
                    bm = yy[13]
                    bendmovv.set(bm)
                    dw = yy[15]
                    dwellv.set(dw)

                except Exception as e:
                    print(e)
                bn = str(bn)
                bdno.set(bn)

            pass

        frame1 = Frame(self.root, highlightbackground="blue", highlightthickness=1, bg="#b3ffe0")
        logoimg = ImageTk.PhotoImage(
            Image.open('sukrit_Logo.png').resize((150, 70), Image.LANCZOS))
        Label(frame1, image=logoimg,bg="#b3ffe0").grid(row=0, column=0)
        Label(frame1, text="               ", font="Algerian 27 bold", padx=7, pady=7, bg="#b3ffe0").grid(row=0, column=1,
                                                                                                      padx=10)
        Entry(frame1,  font="Calibri 11", width=11).grid(row=0, column=2)
        Label(frame1, text="Bend Data",fg="#cc3300", font="Algerian 27 bold", padx=7, pady=7, bg="#b3ffe0").grid(row=0, column=3,
                                                                                                       padx=10)
        frame1.grid(row=0,ipadx=50,sticky="ew")
        frame2 = Frame(self.root, bg="blue", height=15)
        # wlabel=Label(frame2,text="",bg="blue",height=10).grid(row=1)
        frame2.grid(row=1,ipadx=400,sticky='ew')

        frame3 = Frame(self.root, highlightbackground="blue", width=300, height=100, highlightthickness=2, bg="#b3ffe0")

        self.root.bind('<Return>', enterp2)

        frame4 = Frame(frame3, highlightbackground="blue",width=300, height=100, highlightthickness=2, bg="#b3ffe0")

        yy = myresultBD[0]

        print(yy)
        bn = yy[0]
        bdno=StringVar()
        bdno.set(bn)


        Label(frame4, text="Prog No.", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=0, column=0)
        pnovalue = StringVar()
        pgno = yy[1]
        pnovalue.set(pgno)
        Entry(frame4, width=10, textvariable=pnovalue, font="Arial_Black 12 bold", ).grid(row=0, column=1)
        Label(frame4, text="Angle", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=1, column=0)
        anglev = StringVar()
        ag = yy[3]
        anglev.set(ag)
        Entry(frame4, width=10, textvariable=anglev, font="Arial_Black 12 bold", ).grid(row=1, column=1)
        Label(frame4, text="Length", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=2, column=0)
        lengthv = StringVar()
        lgt = yy[6]
        lengthv.set(lgt)
        Entry(frame4, width=10, textvariable=lengthv, font="Arial_Black 12 bold", ).grid(row=2, column=1)
        Label(frame4, text="Back Gauge", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=3, column=0)
        bgaugev = StringVar()
        bg = yy[8]
        bgaugev.set(bg)
        Entry(frame4, width=10, textvariable=bgaugev, font="Arial_Black 12 bold", ).grid(row=3, column=1)
        Label(frame4, text="Retract", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=4, column=0)
        retractv = StringVar()
        rt = yy[10]
        retractv.set(rt)
        Entry(frame4, width=10, textvariable=retractv, font="Arial_Black 12 bold", ).grid(row=4, column=1)
        Label(frame4, text="Opening", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=5, column=0)
        openingv = StringVar()
        opn = yy[12]
        openingv.set(opn)
        Entry(frame4, width=10, textvariable=openingv, font="Arial_Black 12 bold", ).grid(row=5, column=1)
        Label(frame4, text="R Position", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=6, column=0)
        rpositionv = StringVar()
        rp = yy[14]
        rpositionv.set(rp)
        Entry(frame4, width=10, textvariable=rpositionv, font="Arial_Black 12 bold", ).grid(row=6, column=1)
        #--------------------------------------------------------

        Label(frame4, text="P. Name", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=0, column=2)
        pnamev = StringVar()
        pgn = yy[2]
        pnamev.set(pgn)
        Entry(frame4, width=10, textvariable=pnamev, font="Arial_Black 12 bold", ).grid(row=0, column=3)
        Label(frame4, text="Bend No.", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=1, column=2)
        bendnov = StringVar()
        bd1 = yy[4]
        bd2 = yy[5]
        bendnov.set(str(bd1)+" / "+str(bd2))
        Entry(frame4, width=10, textvariable=bendnov, font="Arial_Black 12 bold", ).grid(row=1, column=3)
        Label(frame4, text="Force", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=2, column=2)
        forcev = StringVar()
        fc = yy[7]
        forcev.set(fc)
        Entry(frame4, width=10, textvariable=forcev, font="Arial_Black 12 bold", ).grid(row=2, column=3)
        Label(frame4, text="Y-axis", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=3, column=2)
        yaxisv = StringVar()
        ya = yy[9]
        yaxisv.set(ya)
        Entry(frame4, width=10, textvariable=yaxisv, font="Arial_Black 12 bold", ).grid(row=3, column=3)
        Label(frame4, text="Angle Corr.", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=4, column=2)
        acorrv = StringVar()
        ac = yy[11]
        acorrv.set(ac)
        Entry(frame4, width=10, textvariable=acorrv, font="Arial_Black 12 bold", ).grid(row=4, column=3)
        Label(frame4, text="Bend Mov.", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=5, column=2)
        bendmovv = StringVar()
        bm = yy[13]
        bendmovv.set(bm)
        Entry(frame4, width=10, textvariable=bendmovv, font="Arial_Black 12 bold", ).grid(row=5, column=3)
        Label(frame4, text="Dwell", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=6, column=2)
        dwellv = StringVar()
        dw = yy[15]
        dwellv.set(dw)
        Entry(frame4, width=10, textvariable=dwellv, font="Arial_Black 12 bold", ).grid(row=6, column=3)

        frame4.grid(row=0,column=0,ipadx=33.5,sticky="w")

        frame7 = Frame(frame3, highlightbackground="blue", width=300, height=100, highlightthickness=2, bg="#b3ffe0")
        upimg = ImageTk.PhotoImage(
            Image.open('arrow-up.png').resize((100, 60), Image.LANCZOS))
        Button(frame7, command=plus,image=upimg, highlightthickness=0, borderwidth=0,bg="#b3ffe0").grid(row=0, column=1, padx=15,pady=19.2)

        pdimg = ImageTk.PhotoImage(
            Image.open('punchdata.png').resize((100, 60), Image.LANCZOS))
        Button(frame7, command=pnData,image=pdimg, highlightthickness=0, borderwidth=0,bg="#b3ffe0").grid(row=0, column=2, padx=15, pady=19.2)

        # Button(frame7, text="+", padx=30).grid(row=0, column=1)
        Label(frame7, text=" ", fg="#b3ffe0", bg="#b3ffe0").grid(row=0, column=0)

        Label(frame7, textvariable=bdno, font="Stencil 25 bold", fg="Black", bg="#b3ffe0").grid(row=1, column=1)
        dnimg = ImageTk.PhotoImage(
            Image.open('down.png').resize((100, 60), Image.LANCZOS))
        Button(frame7, command=minus,image=dnimg, highlightthickness=0, borderwidth=0,bg="#b3ffe0").grid(row=2, column=1, padx=15,pady=19.2)
        dieimg = ImageTk.PhotoImage(
            Image.open('die.png').resize((100, 60), Image.LANCZOS))
        Button(frame7, image=dieimg, highlightthickness=0, borderwidth=0,bg="#b3ffe0").grid(row=2, column=2, padx=15, pady=19.2)
        # Button(frame7, text="-", padx=30).grid(row=2, column=1)
        Button(frame7, command=csvw,text="Export as CSV", padx=30,bg="blue",fg="white").grid(row=3, column=1)
        frame7.grid(row=0,column=1,ipadx=112, sticky="e")

        frame3.grid(row=2, column=0, ipadx=33.5, sticky="ew")

        frame5 = Frame(self.root, bg="blue", height=10)
        # wlabel=Label(frame2,text="",bg="blue",height=10).grid(row=1)
        frame5.grid(row=3,ipadx=400,sticky='ew')

        frame6 = Frame(self.root, highlightbackground="blue", highlightthickness=2, bg="#b3ffe0")
        homeimg = ImageTk.PhotoImage(
            Image.open('home.png').resize((150, 90), Image.LANCZOS))
        # settinglabel=Label(frame6,image=settingimg).grid(row=0,column=0,padx=50)
        Button(frame6, image=homeimg, command=pBrake,highlightthickness=0, borderwidth=0,bg="#b3ffe0").grid(row=0, column=0,padx=15)
        pgimg = ImageTk.PhotoImage(
            Image.open('program.png').resize((150, 90), Image.LANCZOS))
        # pdlabel=Label(frame6,image=pdimg).grid(row=0,column=1,padx=50,columnspan=2)
        Button(frame6, image=pgimg, command=prog,font="Calibri 13 bold", highlightthickness=0, borderwidth=0,bg="#b3ffe0").grid(row=0, column=1,padx=15)
        pglimg = ImageTk.PhotoImage(
            Image.open('programlist.png').resize((150, 90), Image.LANCZOS))
        # pdlabel=Label(frame6,image=pdimg).grid(row=0,column=1,padx=50,columnspan=2)
        Button(frame6, image=pglimg, command=pgList,highlightthickness=0, borderwidth=0,bg="#b3ffe0").grid(row=0, column=2,padx=15)
        plimg = ImageTk.PhotoImage(
            Image.open('operation.png').resize((150, 90), Image.LANCZOS))
        # pllabel=Label(frame6,image=plimg).grid(row=0,column=4,padx=50,columnspan=2)
        Button(frame6, image=plimg, command=op,highlightthickness=0, borderwidth=0,bg="#b3ffe0").grid(row=0, column=4,padx=15)
        frame6.grid(row=4,ipadx=20,sticky='ew')

        self.root.mainloop()

if __name__=='__main__':
    bd=benddata()
    bd.bendframe()