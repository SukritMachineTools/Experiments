from tkinter import *
from PIL import Image, ImageTk
# from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import re

##########################
#   Configuration
bgcolor="#99ff99"
winH=768
winW=1366
winS=str(winW)+"x"+str(winH)
###########################
# Default Values
job='S.R. Shaft THD'
breakTime='01:30'
start_date= '2023-06-01'
end_date= '2023-07-07'
flag=0
############################

class home:
    def __int__(self):
        pass
    def machinePage(self):
        self.root=Tk()
        self.root.geometry(winS)
        self.root.title("Sukrit Production Records")
        self.root.configure(background=bgcolor)

        #########format check#########################################
        def check_date_format(input_string):
            pattern = r'^\d{4}-\d{2}-\d{2}$'
            if re.match(pattern, input_string):
                return input_string
            else:
                err="Error"
                return err

        def check_btime_format(input_string):
            pattern = r'^\d{1}:\d{2}$'
            pattern2 = r'^$'
            if re.match(pattern, input_string):
                return input_string
            elif re.match(pattern2, input_string):
                input_string=breakTime
                return input_string
            else:
                err="Error"
                return err

        # Machine Frame
        def mpage():

            frame2 = Frame(self.root, bg="blue", height=15)
            Label(frame2, text="Production Records", fg="#ffffff", font="Algerian 20 bold", padx=7, pady=7,
                  bg="blue").grid(
                row=0,
                column=1, sticky='n')
            frame2i = Frame(frame2, highlightbackground="blue", width=300, height=100, highlightthickness=1, bg=bgcolor)
            Label(frame2i, text="Start Date:", fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=1)
            Label(frame2i, text=start_date, fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=2)
            Label(frame2i, text="End Date:", fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=3)
            Label(frame2i, text=end_date, fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=4)
            Label(frame2i, text="Job:", fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=5)
            Label(frame2i, text=job, fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=6)
            Label(frame2i, text="Break Time:", fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=7)
            Label(frame2i, text=breakTime, fg="#000000", font="Algerian 16 bold", padx=7, pady=7,
                  bg=bgcolor).grid(
                row=1,
                column=8)
            frame2i.grid(row=1, column=1, ipadx=33.5, sticky="w")
            frame2.grid(row=1, ipadx=400, sticky='ew')
            pass

        def submitD():
            global job
            global breakTime
            global start_date
            global end_date
            flag=0

            if len(jobvalue.get()) > 0:
                job=jobvalue.get()
                print(job)
            else:
                print("job error")
                messagebox.showerror("Error", "Enter the Job")
                flag=1

            if check_btime_format(bTimevalue.get()) !="Error":
                breakTime=check_btime_format(bTimevalue.get())
                print(breakTime)
            else:
                print("btime error")
                messagebox.showerror("Error", "Enter correct Break Time")
                flag=1
            if check_date_format(sDatevalue.get()) != "Error":
                start_date=check_date_format(sDatevalue.get())
                print(start_date)
            else:
                print("st date error")
                messagebox.showerror("Error", "Enter correct Start Date")
                flag=1
            if check_date_format(eDatevalue.get()) !="Error":
                end_date=check_date_format(eDatevalue.get())
                print(end_date)
            else:
                print("end date error")
                messagebox.showerror("Error", "Enter correct End Date")
                flag=1

            if flag!=1:
                frame2.destroy()
                frame3.destroy()
                mpage()
            pass
        #################################################################################################

        global job
        global breakTime
        global start_date
        global end_date

        frame1 = Frame(self.root, highlightbackground="blue", highlightthickness=1, bg=bgcolor)
        Label(frame1, text="Su", fg="#ffffff", font="Algerian 27 bold", padx=7, pady=7, bg="#000000").grid(
            row=0,
            column=1)
        Label(frame1, text="krit", fg="#000000", font="Algerian 27 bold", padx=7, pady=7, bg="#ffffff").grid(
            row=0,
            column=2)
        frame1.grid(row=0, ipadx=600, sticky="ew")
        frame2 = Frame(self.root, bg="blue", height=15)
        Label(frame2, text="Production Records", fg="#ffffff", font="Algerian 20 bold", padx=7, pady=7, bg="blue").grid(
            row=0,
            column=1,sticky='n')
        Label(frame2, text="Monthly Record", fg="#000000", font="Algerian 16 bold", padx=7, pady=7, bg=bgcolor).grid(
            row=1,
            column=1, sticky='n')
        frame2.grid(row=1, ipadx=400, sticky='ew')
        frame3 = Frame(self.root, highlightbackground="blue", width=300, height=100, highlightthickness=2, bg=bgcolor)

        frame4 = Frame(frame3, highlightbackground="blue", width=300, height=100, highlightthickness=0, bg=bgcolor)
        Label(frame4, text="ENTER THE DETAILS", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=0, column=0)
        Label(frame4, text="Start Date", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=1, column=0)
        sDatevalue = StringVar()
        Entry(frame4, width=10, textvariable=sDatevalue, font="Arial_Black 12 bold", ).grid(row=1, column=1)
        Label(frame4, text="(2023-06-01)", font="Calibri 10 bold", padx=7, pady=7, bg=bgcolor,
              fg="#000000").grid(row=2, column=0)
        Label(frame4, text="End Date", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=3, column=0)
        eDatevalue = StringVar()
        Entry(frame4, width=10, textvariable=eDatevalue, font="Arial_Black 12 bold", ).grid(row=3, column=1)
        Label(frame4, text="(2023-06-01)", font="Calibri 10 bold", padx=7, pady=7, bg=bgcolor,
              fg="#000000").grid(row=4, column=0)
        Label(frame4, text="Job", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=1, column=3)
        jobvalue = StringVar()
        Entry(frame4, width=20, textvariable=jobvalue, font="Arial_Black 12 bold", ).grid(row=1, column=4)
        Label(frame4, text="Break Time", font="Calibri 13 bold", padx=7, pady=7, bg=bgcolor,
              fg="blue").grid(row=3, column=3)
        bTimevalue = StringVar()
        Entry(frame4, width=20, textvariable=bTimevalue, font="Arial_Black 12 bold", ).grid(row=3, column=4)
        Label(frame4, text="(1:30)", font="Calibri 10 bold", padx=7, pady=7, bg=bgcolor,
              fg="#000000").grid(row=4, column=3)
        Button(frame4, command=submitD, text="SUBMIT", padx=30, bg="blue", fg="white").grid(row=5, column=1)
        frame4.grid(row=0, column=0, ipadx=33.5, sticky="w")

        frame3.grid(row=2, column=0, ipadx=33.5, sticky="ew")












        self.root.mainloop()

if __name__ == '__main__':
    pg = home()
    pg.machinePage()