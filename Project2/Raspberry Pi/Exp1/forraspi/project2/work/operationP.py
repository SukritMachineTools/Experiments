from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import time
import threading
from initialP import home
from databaseP import database


class operation():

    def operationframe(self):
        self.root = home.start(self)
        mydbOP, mycursorOP, myresultOP = database.opdb(self)

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

        def clock():
            hour = time.strftime("%I")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            am_pm = time.strftime("%p")

            timeLable.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
            timeLable.after(1000, clock)

        def enterp2(event):
            update()

        def update():
            global opnumber
            #opn = yy[0]
            opnumber=opno.get()
            ag = anglev.get()
            lgt = lengthv.get()
            bg = bgaugev.get()
            rt = retractv.get()
            opn = openingv.get()
            rp = rpositionv.get()
            th = thickv.get()
            fc = forcev.get()
            pgno = prgno.get()
            lfc = lastforcev.get()
            afc = actforcev.get()
            pnch = pinchv.get()
            bd1 = bendv.get()
            bd2 = bend2v.get()
            dw = dwellv.get()
            xv = xvv.get()
            rv = rvv.get()
            yv = yvv.get()
            ct = countv.get()
            sp = spv.get()

            try:
                sql = """UPDATE operationList SET Angle= %s, Lengtth= %s, BackGauge= %s, Retract= %s, Opening= %s, RPosition= %s, Thick= %s, Forcee= %s, ProgNo= %s, LastForce= %s, ActForce= %s,Pinch= %s, Bend1= %s, Bend2= %s, Dwell= %s, Xv= %s, Rv= %s, Yv= %s, Countt= %s, speed= %s WHERE OpNum = %s;"""
                result = [ag,lgt,bg,rt, opn,rp,th,fc,pgno,lfc,afc,pnch,bd1,bd2,dw,xv,rv,yv,ct,sp,opnumber]
                mycursorOP.execute(sql, result)
                mydbOP.commit()

            except Exception as e:
                print(e)

            pass

        def plus():
            global opnumber
            opnumber = opno.get()
            opnumber = int(opnumber)
            if opnumber < 10:
                opnumber = opnumber + 1
                try:
                    sql = """SELECT * FROM operationList WHERE OpNum= %s"""
                    val = [opnumber]
                    mycursorOP.execute(sql, val)
                    myresult = mycursorOP.fetchall()
                    yy = myresult[0]
                    ag = yy[1]
                    anglev.set(ag)
                    lgt = yy[2]
                    lengthv.set(lgt)
                    bg = yy[3]
                    bgaugev.set(bg)
                    rt = yy[4]
                    retractv.set(rt)
                    opn = yy[5]
                    openingv.set(opn)
                    rp = yy[6]
                    rpositionv.set(rp)
                    th = yy[7]
                    thickv.set(th)
                    fc = yy[8]
                    forcev.set(fc)
                    pgno = yy[9]
                    prgno.set(pgno)
                    lfc = yy[10]
                    lastforcev.set(lfc)
                    afc = yy[11]
                    actforcev.set(afc)
                    pnch = yy[12]
                    pinchv.set(pnch)
                    bd1 = yy[13]
                    bendv.set(bd1)
                    bd2 = yy[14]
                    bend2v.set(bd2)
                    dw = yy[15]
                    dwellv.set(dw)
                    xv = yy[16]
                    xvv.set(xv)
                    rv = yy[17]
                    rvv.set(rv)
                    yv = yy[18]
                    yvv.set(yv)
                    ct = yy[19]
                    countv.set(ct)
                    sp = yy[20]
                    spv.set(sp)


                except Exception as e:
                    print(e)
                opnumber = str(opnumber)
                opno.set(opnumber)

            pass

        def minus():
            global opnumber
            opnumber = opno.get()
            opnumber = int(opnumber)
            if opnumber > 1:
                opnumber = opnumber - 1
                try:
                    sql = """SELECT * FROM operationList WHERE OpNum= %s"""
                    val = [opnumber]
                    mycursorOP.execute(sql, val)
                    myresult = mycursorOP.fetchall()
                    yy = myresult[0]
                    ag = yy[1]
                    anglev.set(ag)
                    lgt = yy[2]
                    lengthv.set(lgt)
                    bg = yy[3]
                    bgaugev.set(bg)
                    rt = yy[4]
                    retractv.set(rt)
                    opn = yy[5]
                    openingv.set(opn)
                    rp = yy[6]
                    rpositionv.set(rp)
                    th = yy[7]
                    thickv.set(th)
                    fc = yy[8]
                    forcev.set(fc)
                    pgno = yy[9]
                    prgno.set(pgno)
                    lfc = yy[10]
                    lastforcev.set(lfc)
                    afc = yy[11]
                    actforcev.set(afc)
                    pnch = yy[12]
                    pinchv.set(pnch)
                    bd1 = yy[13]
                    bendv.set(bd1)
                    bd2 = yy[14]
                    bend2v.set(bd2)
                    dw = yy[15]
                    dwellv.set(dw)
                    xv = yy[16]
                    xvv.set(xv)
                    rv = yy[17]
                    rvv.set(rv)
                    yv = yy[18]
                    yvv.set(yv)
                    ct = yy[19]
                    countv.set(ct)
                    sp = yy[20]
                    spv.set(sp)


                except Exception as e:
                    print(e)
                opnumber = str(opnumber)
                opno.set(opnumber)

            pass




        frame1 = Frame(self.root, highlightbackground="blue", highlightthickness=1, bg="#b3ffe0")
        logoimg = ImageTk.PhotoImage(
            Image.open('sukrit_Logo.png').resize((150, 70), Image.LANCZOS))
        Label(frame1, image=logoimg,bg="#b3ffe0").grid(row=0, column=0)
        Label(frame1, text="               ", font="Algerian 27 bold", padx=4.5,pady=4.5, bg="#b3ffe0").grid(row=0,
                                                                                                          column=1,
                                                                                                          padx=10)
        # currTime= time.strftime("%H:%M:%S", time.localtime())

        timeLable = Label(frame1,text="", font="Calibri 18",bg="#b3ffe0", width=11)
        timeLable.grid(row=0, column=2)
        Label(frame1, text="Operation",fg="#cc3300", font="Algerian 27 bold", padx=4.5,pady=4.5, bg="#b3ffe0").grid(row=0, column=3,
                                                                                                    padx=10)
        frame1.grid(row=0, ipadx=50, sticky="ew")
        frame2 = Frame(self.root, bg="blue", height=5)
        frame2.grid(row=1, ipadx=400, sticky='ew')

        frame3 = Frame(self.root, highlightbackground="blue", width=300, height=100,    highlightthickness=2, bg="#b3ffe0")
        self.root.bind('<Return>', enterp2)
        framei1 = Frame(frame3, bg="#b3ffe0")
        yy = myresultOP[0]
        opnumber = yy[0]
        opno= StringVar()
        opno.set(opnumber)

        Label(framei1, text="Angle", font="Calibri 13 bold", padx=4.5,pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=0, column=0)
        anglev = StringVar()
        ag = yy[1]
        anglev.set(ag)
        Entry(framei1, width=10, textvariable=anglev, font="Arial_Black 12 bold", ).grid(row=0, column=1)

        Label(framei1, text="Length", font="Calibri 13 bold", padx=4.5,pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=1, column=0)
        lengthv = StringVar()
        lgt = yy[2]
        lengthv.set(lgt)
        Entry(framei1, width=10, textvariable=lengthv, font="Arial_Black 12 bold", ).grid(row=1, column=1)
        Label(framei1, text="B.Gauge", font="Calibri 13 bold", padx=4.5,pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=2, column=0)
        bgaugev = StringVar()
        bg = yy[3]
        bgaugev.set(bg)
        Entry(framei1, width=10, textvariable=bgaugev, font="Arial_Black 12 bold", ).grid(row=2, column=1)
        Label(framei1, text="Retract", font="Calibri 13 bold", padx=4.5,pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=3, column=0)
        retractv = StringVar()
        rt = yy[4]
        retractv.set(rt)
        Entry(framei1, width=10, textvariable=retractv, font="Arial_Black 12 bold", ).grid(row=3, column=1)
        Label(framei1, text="Opening", font="Calibri 13 bold", padx=4.5,pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=4, column=0)
        openingv = StringVar()
        opn = yy[5]
        openingv.set(opn)
        Entry(framei1, width=10, textvariable=openingv, font="Arial_Black 12 bold", ).grid(row=4, column=1)
        Label(framei1, text="R Position", font="Calibri 13 bold", padx=4.5,pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=5, column=0)
        rpositionv = StringVar()
        rp = yy[6]
        rpositionv.set(rp)
        Entry(framei1, width=10, textvariable=rpositionv, font="Arial_Black 12 bold", ).grid(row=5, column=1)
        Label(framei1, text="Thick", font="Calibri 13 bold", padx=4.5,pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=6, column=0)
        thickv = StringVar()
        th = yy[7]
        thickv.set(th)
        Entry(framei1, width=10, textvariable=thickv, font="Arial_Black 12 bold", ).grid(row=6, column=1)
        Label(framei1, text="Force", font="Calibri 13 bold", padx=4.5,pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=7, column=0)
        forcev = StringVar()
        fc = yy[8]
        forcev.set(fc)
        Entry(framei1, width=10, textvariable=forcev, font="Arial_Black 12 bold", ).grid(row=7, column=1)
        framei1.grid(row=0, column=0, sticky="e",ipadx=5,ipady=6)
        #-------Framei2---------------------
        framei2 = Frame(frame3, highlightbackground="blue",    highlightthickness=2, bg="#b3ffe0",width=50)
        #frameA
        frameA = Frame(framei2, bg="#b3ffe0")
        Label(frameA, text="Programme", font="Calibri 13 bold", padx=4.5, pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=0, column=0)
        prgno = StringVar()
        pgno = yy[9]
        prgno.set(pgno)
        Label(frameA, textvariable=prgno, font="Calibri 13 bold", padx=4.5, pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=0, column=1)
        frameA.grid(row=0)
        #FrameB
        frameB = Frame(framei2, bg="#b3ffe0")
        #FrameB1
        frameB1 = Frame(frameB,  bg="#b3ffe0")
        frameB1i = Frame(frameB1,  bg="#b3ffe0")
        Label(frameB1i, text="Last Force", font="Calibri 13 bold", padx=4.5, pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=0, column=0)
        lastforcev = StringVar()
        lfc = yy[10]
        lastforcev.set(lfc)
        Entry(frameB1i, width=10, textvariable=lastforcev, font="Arial_Black 12 bold", ).grid(row=0, column=1)

        Label(frameB1i, text="Pinch", font="Calibri 13 bold", padx=4.5, pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=1, column=0)
        pinchv = StringVar()
        pnch = yy[12]
        pinchv.set(pnch)
        Entry(frameB1i, width=10, textvariable=pinchv, font="Arial_Black 12 bold", ).grid(row=1, column=1)
        frameB1i.grid(row=0)
        frameBend = Frame(frameB1, bg="#b3ffe0")
        Label(frameBend, text="Bend", font="Calibri 13 bold", padx=4.5, pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=0, column=0)
        bendv = StringVar()
        bd1 = yy[13]
        bendv.set(bd1)

        Entry(frameBend, width=3, textvariable=bendv, font="Arial_Black 12 bold", ).grid(row=0, column=1)
        Label(frameBend, text="/", font="Calibri 8 bold", padx=4.5, pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=0, column=2)
        bend2v = StringVar()
        bd2 = yy[14]
        bend2v.set(bd2)
        Entry(frameBend, width=3, textvariable=bend2v, font="Arial_Black 12 bold", ).grid(row=0, column=3)
        frameBend.grid(row=2)
        frameB1ii = Frame(frameB1, bg="#b3ffe0")
        Label(frameB1ii, text="Dwell", font="Calibri 13 bold", padx=4.5, pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=0, column=0)
        dwellv = StringVar()
        dw = yy[15]
        dwellv.set(dw)
        Entry(frameB1ii, width=10, textvariable=dwellv, font="Arial_Black 12 bold", ).grid(row=0, column=1)
        frameB1ii.grid(row=3)
        frameB1iii = Frame(frameB1, bg="#b3ffe0")
        Label(frameB1iii, text="X", font="Calibri 13 bold", padx=4.5, pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=0, column=0)
        ximg = ImageTk.PhotoImage(
            Image.open('redd.png').resize((10, 15), Image.LANCZOS))
        Label(frameB1iii, image=ximg,bg="#b3ffe0").grid(row=0,column=1)
        xvv = StringVar()
        xv = yy[16]
        xvv.set(xv)
        Entry(frameB1iii, width=10, textvariable=xvv, font="Arial_Black 12 bold", ).grid(row=0, column=2)
        Label(frameB1iii, text="R", font="Calibri 13 bold", padx=4.5, pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=1, column=0)
        rimg = ImageTk.PhotoImage(
            Image.open('bluee.png').resize((10, 15), Image.LANCZOS))
        Label(frameB1iii, image=rimg,bg="#b3ffe0").grid(row=1,column=1)
        rvv = StringVar()
        rv = yy[17]
        rvv.set(rv)
        Entry(frameB1iii, width=10, textvariable=rvv, font="Arial_Black 12 bold", ).grid(row=1, column=2)
        Label(frameB1iii, text="Y", font="Calibri 13 bold", padx=4.5, pady=4.5, bg="#b3ffe0",
              fg="blue").grid(row=2, column=0)
        yimg = ImageTk.PhotoImage(
            Image.open('greenn.png').resize((10, 15), Image.LANCZOS))
        Label(frameB1iii, image=yimg,bg="#b3ffe0").grid(row=2,column=1)
        yvv = StringVar()
        yv = yy[18]
        yvv.set(yv)
        Entry(frameB1iii, width=10, textvariable=yvv, font="Arial_Black 12 bold", ).grid(row=2, column=2)
        frameB1iii.grid(row=4)
        frameB1.grid(row=0,column=0, sticky="ws")
        #FrameB2
        frameB2 = Frame(frameB, bg="#b3ffe0")
        frameB2i = Frame(frameB2, bg="#b3ffe0")
        Label(frameB2i, text="Act Force", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=0, column=0)
        actforcev = StringVar()
        afc = yy[11]
        actforcev.set(afc)
        Entry(frameB2i, width=10, textvariable=actforcev, font="Arial_Black 12 bold", ).grid(row=0, column=1)
        Label(frameB2i, text="(Ton)", font="Calibri 8 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=0, column=2)
        frameB2i.grid(row=0 )

        frameB2ii = Frame(frameB2, bg="#b3ffe0")
        splimg = ImageTk.PhotoImage(
            Image.open('spb machine.png').resize((100, 150), Image.LANCZOS))
        Label(frameB2ii,image=splimg).grid()
        frameB2ii.grid(row=1)

        frameB2iii = Frame(frameB2, bg="#b3ffe0")
        Label(frameB2iii, text="55.57", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=0, column=0)
        Button(frameB2iii,text="Ok",font="Calibri 13 bold",bg="yellow").grid(row=0,column=1)
        frameB2iii.grid(row=2, sticky="s")
        frameB2.grid(row=0, column=1 ,sticky="es")

        frameB.grid(row=1, sticky="s")
        framei2.grid(row=0, column=1)
        #--------------Framei3-------------
        framei3 = Frame(frame3, bg="#b3ffe0")
        Button(framei3,text="EMG PRESSSED",fg="white",bg="Red").grid(row=0,sticky="w",pady=5,padx=5)
        Button(framei3,text="Count",bg="#4db8ff").grid(row=1,sticky="w",pady=5,padx=5)
        countv=StringVar()
        ct = yy[19]
        countv.set(ct)
        Entry(framei3, width=10, textvariable=countv, font="Arial_Black 12 bold", ).grid(row=2,sticky="w",pady=5,padx=5)
        handimg = ImageTk.PhotoImage(
            Image.open('hand.png').resize((150, 90), Image.LANCZOS))
        Button(framei3,image=handimg,borderwidth=0,bg="#9999ff",relief="ridge").grid(row=3,sticky="w",pady=5,padx=5)
        framesp=Frame(framei3,  bg="#b3ffe0")
        Label(framesp, text="Speed", font="Calibri 13 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=0, column=0)
        spv = StringVar()
        sp = yy[20]
        spv.set(sp)
        Entry(framesp, width=7, textvariable=spv, font="Arial_Black 12 bold").grid(row=0, column=1)
        Label(framesp, text="(mm/s)", font="Calibri 8 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=0, column=2)
        framesp.grid(row=4,sticky="w",pady=5)
        framei3.grid(row=0, column=2)

        frame3.grid(row=2, column=0, ipadx=33.5, sticky="ew")

        frame5 = Frame(self.root, bg="blue", height=10)
        Label(frame5, text="Emergency Swtich Pressed...", font="Calibri 8 bold", padx=7, pady=7, bg="#b3ffe0",
              fg="blue").grid(row=0, column=0)
        frame5.grid(row=3, ipadx=150, sticky='ew')

        frame6 = Frame(self.root, highlightbackground="blue",    highlightthickness=2, bg="#b3ffe0")
        homeimg = ImageTk.PhotoImage(
            Image.open('home.png').resize((100, 70), Image.LANCZOS))
        # settinglabel=Label(frame6,image=settingimg).grid(row=0,column=0,padx=50)
        Button(frame6, image=homeimg, command=pBrake,borderwidth=0, bg="#b3ffe0").grid(row=0, column=0, padx=15)
        lrimg = ImageTk.PhotoImage(
            Image.open('arrow1.png').resize((100, 70), Image.LANCZOS))
        # pdlabel=Label(frame6,image=pdimg).grid(row=0,column=1,padx=50,columnspan=2)
        Button(frame6, image=lrimg, command=minus,font="Calibri 13 bold", borderwidth=0, bg="#b3ffe0").grid(row=0, column=1, padx=15)
        Label(frame6, textvariable=opno,font="Calibri 13 bold",bg="#b3ffe0",fg="blue").grid(row=0, column=2, padx=50)
        rrimg = ImageTk.PhotoImage(
            Image.open('arrow.png').resize((100, 70), Image.LANCZOS))
        # pdlabel=Label(frame6,image=pdimg).grid(row=0,column=1,padx=50,columnspan=2)
        Button(frame6, image=rrimg,  command=plus,borderwidth=0, bg="#b3ffe0").grid(row=0, column=3, padx=15)
        pgimg = ImageTk.PhotoImage(
            Image.open('program.png').resize((100, 70), Image.LANCZOS))
        Button(frame6, image=pgimg, command=prog,borderwidth=0, bg="#b3ffe0").grid(row=0, column=4, padx=15)
        frame6.grid(row=4, ipadx=20, sticky='ew')



        clock()

        self.root.mainloop()

if __name__=='__main__':
    op=operation()
    op.operationframe()