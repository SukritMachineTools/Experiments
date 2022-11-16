from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from os import system
from pyModbusTCP.client import ModbusClient
import time
from pyModbusTCP.client import ModbusClient
from pyModbusTCP.utils import encode_ieee, decode_ieee, \
    long_list_to_word, word_list_to_long
from initialP import home


class FloatModbusClient(ModbusClient):
    """A ModbusClient class with float support."""

    def read_float(self, address, number=1):
        """Read float(s) with read holding registers."""
        reg_l = self.read_holding_registers(address, number * 2)
        if reg_l:
            return [decode_ieee(f) for f in word_list_to_long(reg_l)]
        else:
            return None

    def read_floatrev(self, address, number=1):
        """Read float(s) with read holding registers."""
        reg_l = self.read_holding_registers(address, number * 2)
        if reg_l:
            reg_l.reverse()
            return [decode_ieee(f) for f in word_list_to_long(reg_l)]
        else:
            return None

    def write_float(self, address, floats_list):
        """Write float(s) with write multiple registers."""
        b32_l = [encode_ieee(f) for f in floats_list]
        b16_l = long_list_to_word(b32_l)
        return self.write_multiple_registers(address, b16_l)

    def write_floatrev(self, address, floats_list):
        """Write float(s) with write multiple registers."""
        b32_l = [encode_ieee(f) for f in floats_list]
        b16_l = long_list_to_word(b32_l)
        b16_l.reverse()
        return self.write_multiple_registers(address, b16_l)


class pressBrake():

    def pressBrakeFrame(self):
        self.root = home.start(self)
        self.root.configure(background="orange")

        def pndata():
            # pass
            self.root.destroy()
            from punchDataP import punchData
            pd=punchData()
            pd.punchDataFrame()
            pass

        def prog():
            self.root.destroy()
            from programP import program
            pg=program()
            pg.programFrame()
            pass
        def op():
            self.root.destroy()
            from operationP import operation
            o=operation()
            o.operationframe()
            pass
        def bData():
            self.root.destroy()
            from bendataP import benddata
            o=benddata()
            o.bendframe()
            pass

        c = ModbusClient(host='192.168.1.77', port=502, auto_open=True, debug=False)
        k = FloatModbusClient(host='192.168.1.77', port=502, auto_open=True)

        global xvalue

        def xadd():
            global x1value
            x1value = x1value + 0.0100
            x1value = round(x1value, 3)
            # c.write_single_register(4676, xvalue)
            k.write_floatrev(4676, [x1value])
            xxvalue.set(x1value)
            # xyz.set(xxvalue.get())

        def radd():
            global r1value
            r1value = r1value + 0.0100
            r1value = round(r1value, 3)
            # c.write_single_register(4676, xvalue)
            k.write_floatrev(4688, [r1value])
            rrvalue.set(r1value)
            # xyz.set(xxvalue.get())

        def yadd():
            global y1value
            y1value = y1value + 0.0100
            y1value = round(y1value, 3)
            # c.write_single_register(4676, xvalue)
            k.write_floatrev(4684, [y1value])
            yyvalue.set(y1value)
            # xyz.set(xxvalue.get())

        def xsub():
            global x1value
            x1value = x1value - 0.0100
            x1value = round(x1value, 3)
            # c.write_single_register(4676, xvalue)
            k.write_floatrev(4676, [x1value])
            xxvalue.set(x1value)
            # xyz.set(xxvalue.get())

        def rsub():
            global r1value
            r1value = r1value - 0.0100
            r1value = round(r1value, 3)
            # c.write_single_register(4676, xvalue)
            k.write_floatrev(4688, [r1value])
            rrvalue.set(r1value)
            # xyz.set(xxvalue.get())

        def ysub():
            global y1value
            y1value = y1value - 0.0100
            y1value = round(y1value, 3)
            # c.write_single_register(4676, xvalue)
            k.write_floatrev(4684, [y1value])
            yyvalue.set(y1value)
            # xyz.set(xxvalue.get())

        frame1 = Frame(self.root, highlightbackground="blue", highlightthickness=0, bg="orange")
        Label(frame1, text="               ", font="Algerian 27 bold", padx=4.5, pady=4.5, bg="orange").grid(row=0,
                                                                                                             column=1,
                                                                                                             padx=10)
        logoimg = ImageTk.PhotoImage(
            Image.open('sukrit_Logo.png').resize((150, 70), Image.LANCZOS))
        Label(frame1, image=logoimg, bg="orange").grid(row=0, column=0)
        Label(frame1, text="Servo Electric PressBrake", font="Algerian 20 bold", padx=15, pady=15, bg="orange",fg="#990000").grid(
            row=0, column=2, padx=10)
        frame1.grid(row=0, sticky="w")

        frame2 = Frame(self.root, bg="blue", height=10)
        frame2.grid(row=1,sticky="we")

        frame3 = Frame(self.root, highlightbackground="blue", highlightthickness=0, bg="orange")

        # x
        xxvalue = StringVar()
        global xvalue
        global x1value
        # xlist=c.read_holding_registers(4676, 1)
        x1list = k.read_floatrev(4676, 1)
        # xvalue=xlist[0]
        x1value = round(x1list[0], 3)
        xxvalue.set(str(x1value))
        redimg = ImageTk.PhotoImage(Image.open('redd.png'))
        Label(frame3, image=redimg, bg="orange").grid(row=0, column=0, padx=10)
        Label(frame3, text="X", font="Algerian 42 bold", padx=15, pady=15, bg="orange", fg="red").grid(row=0, column=1,
                                                                                                       padx=10)
        larimg = ImageTk.PhotoImage(
            Image.open('arrow1.png').resize((150, 70), Image.LANCZOS))
        # larlabel=Label(frame3,image=larimg,bg="orange").grid(row=0,column=2,padx=10)
        Button(frame3, image=larimg, bg="orange", highlightthickness=0,borderwidth=0, command=xsub).grid(row=0, column=2,
                                                                                    padx=10)
        # xvalue= IntVar()
        Label(frame3, textvariable=xxvalue, font="Arial_Black 17 bold", bg="orange", borderwidth=1,
              relief="solid").grid(row=0, column=3, ipadx=5, padx=10)
        rarimg = ImageTk.PhotoImage(
            Image.open('arrow.png').resize((150, 70), Image.LANCZOS))
        # rarlabel=Label(frame3,image=rarimg,bg="orange").grid(row=0,column=4,padx=10)
        Button(frame3, image=rarimg, bg="orange", highlightthickness=0,borderwidth=0, command=xadd).grid(row=0, column=4,
                                                                                    padx=10)

        # R
        rrvalue = StringVar()
        global rvalue
        global r1value
        # xlist=c.read_holding_registers(4676, 1)
        r1list = k.read_floatrev(4688, 1)
        # xvalue=xlist[0]
        r1value = round(r1list[0], 3)
        rrvalue.set(str(r1value))
        blueimg = ImageTk.PhotoImage(Image.open('bluee.png'))
        Label(frame3, image=blueimg, bg="orange").grid(row=1, column=0, padx=10)
        Label(frame3, text="R", font="Algerian 42 bold", padx=15, pady=15, bg="orange", fg="red").grid(row=1, column=1,
                                                                                                       padx=10)
        # lar1label=Label(frame3,image=larimg,bg="orange").grid(row=1,column=2,padx=10)
        Button(frame3, image=larimg, bg="orange", highlightthickness=0,borderwidth=0, command=rsub).grid(row=1, column=2,
                                                                                    padx=10)
        Label(frame3, textvariable=rrvalue, font="Arial_Black 17 bold", bg="orange", borderwidth=1,
              relief="solid").grid(row=1, column=3, ipadx=5, padx=10)
        # rar1label=Label(frame3,image=rarimg,bg="orange").grid(row=1,column=4,padx=10)
        Button(frame3, image=rarimg, bg="orange", highlightthickness=0,borderwidth=0, command=radd).grid(row=1, column=4,
                                                                                    padx=10)

        # Y
        yyvalue = StringVar()
        global yvalue
        global y1value
        # xlist=c.read_holding_registers(4676, 1)
        y1list = k.read_floatrev(4684, 1)
        # xvalue=xlist[0]
        y1value = round(y1list[0], 3)
        yyvalue.set(str(y1value))
        greenimg = ImageTk.PhotoImage(Image.open('greenn.png'))
        Label(frame3, image=greenimg, bg="orange").grid(row=2, column=0, padx=10)
        Label(frame3, text="Y", font="Algerian 42 bold", padx=15, pady=15, bg="orange", fg="red").grid(row=2, column=1,
                                                                                                       padx=10)
        # lar2label=Label(frame3,image=larimg,bg="orange").grid(row=2,column=2,padx=10)
        Button(frame3, image=larimg, bg="orange", highlightthickness=0,borderwidth=0, command=ysub).grid(row=2, column=2,
                                                                                    padx=10)
        Label(frame3, textvariable=yyvalue, font="Arial_Black 17 bold", bg="orange", borderwidth=1,
              relief="solid").grid(row=2, column=3, ipadx=5, padx=10)
        Label(frame3, image=rarimg, bg="orange").grid(row=2, column=4, padx=10)
        Button(frame3, image=rarimg, bg="orange", highlightthickness=0,borderwidth=0, command=yadd).grid(row=2, column=4,
                                                                                    padx=10)
        frame3.grid(row=2, ipadx=56.3)

        frame4 = Frame(self.root, bg="blue", height=10)
        frame4.grid(row=3, sticky="we")

        frame5 = Frame(self.root, highlightbackground="blue", highlightthickness=0, bg="orange")
        loginimg = ImageTk.PhotoImage(
            Image.open('login.png').resize((130, 70), Image.LANCZOS))
        # settinglabel=Label(frame5,image=settingimg).grid(row=0,column=0,padx=50)
        Button(frame5, image=loginimg, bg="orange", highlightthickness=0,borderwidth=0).grid(row=0, column=0,padx=10,pady=10)
        primg = ImageTk.PhotoImage(
            Image.open('program.png').resize((130, 70), Image.LANCZOS))
        # pdlabel=Label(frame5,image=pdimg).grid(row=0,column=1,padx=50,columnspan=2)
        Button(frame5, image=primg,command=prog,bg="orange", highlightthickness=0,borderwidth=0).grid(row=0, column=1,padx=10,pady=10)
        bdimg = ImageTk.PhotoImage(
            Image.open('benddata.png').resize((130, 70), Image.LANCZOS))
        # pllabel=Label(frame5,image=plimg).grid(row=0,column=4,padx=50,columnspan=2)
        Button(frame5, image=bdimg, command=bData, bg="orange", highlightthickness=0,borderwidth=0).grid(row=0, column=2,padx=10,pady=10)
        pdimg = ImageTk.PhotoImage(
            Image.open('punchdata.png').resize((130, 70), Image.LANCZOS))
        # pllabel=Label(frame5,image=plimg).grid(row=0,column=4,padx=50,columnspan=2)
        Button(frame5, image=pdimg,command=pndata,bg="orange", highlightthickness=0,borderwidth=0).grid(row=0, column=3,padx=10,pady=10)
        opimg = ImageTk.PhotoImage(
            Image.open('operation.png').resize((130, 70), Image.LANCZOS))
        # pllabel=Label(frame5,image=plimg).grid(row=0,column=4,padx=50,columnspan=2)
        Button(frame5, image=opimg,command=op,bg="orange", highlightthickness=0,borderwidth=0).grid(row=0, column=4,padx=10,pady=10)
        frame5.grid(row=4)

        self.root.mainloop()

if __name__=='__main__':
    pb=pressBrake()
    pb.pressBrakeFrame()