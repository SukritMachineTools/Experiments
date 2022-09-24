from tkinter import *
from PIL import Image,ImageTk
from page3 import page3
from page4 import page4
from page5 import page5
class main_menu:
    def __init__(self):
                                # ---------------------Window Settings---------------------
        self.window=Tk()
        self.window.config(bg="#EBF4FA")
        self.window.state("zoomed")
        self.window.minsize(500, 500)
        self.window.title("Main Menu")
        self.lbltitle = Label(self.window, text="HOTEL MANAGMENT SYSTEM",font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4,relief=RIDGE).place(x=0, y=0, width=1367, height=60)
                                #----------------------Adding Images---------------------
        img1 = Image.open(r"my_images/Style4.png")
        img1 = img1.resize((1116, 484))
        self.photo = ImageTk.PhotoImage(img1)
        self.lblimg = Label(self.window, image=self.photo,bd=4,relief=RIDGE)
        self.lblimg.place(x=250, y=170, width=1116,height=600)
        img2 = Image.open(r"my_images/pool_view.png")
        img2 = img2.resize((1116, 170))
        self.photo2 = ImageTk.PhotoImage(img2)
        self.lblimg2 = Label(self.window, image=self.photo2,bd=4,relief=RIDGE)
        self.lblimg2.place(x=250, y=60, width=1116,height=170)
        img3 = Image.open(r"my_images/Style2.png.jpg")
        img3 = img3.resize((250, 220))
        self.photo3 = ImageTk.PhotoImage(img3)
        self.lblimg3 = Label(self.window, image=self.photo3,bd=4,relief=RIDGE)
        self.lblimg3.place(x=0, y=285, width=250,height=220)
        img4 = Image.open(r"my_images/Deluxe_Room.png")
        img4 = img4.resize((250, 220))
        self.photo4 = ImageTk.PhotoImage(img4)
        self.lblimg4 = Label(self.window, image=self.photo4,bd=4,relief=RIDGE)
        self.lblimg4.place(x=0, y=495, width=250,height=210)

                                #----------------------Frame-------------------------
        self.main_frame=Frame(self.window,bd=4,bg="grey",relief=RIDGE).place(x=0,y=60,width=250,height=224)
        self.menutitle = Label(self.window, text="MENU BAR",font=("Algerian", 20, "bold"), bg="black", fg="gold", bd=2,relief=RIDGE).place(x=0, y=60, width=248, height=80)
        self.rooms = Button(self.window, text="ROOM BOOKING",font=("Imprint MT Shadow", 15), bg="black", fg="red", bd=2,relief=RIDGE,cursor="circle",command= lambda : page3(self.window)).place(x=0, y=175, width=248, height=35)
        self.details = Button(self.window, text="ROOMS DETAIL",font=("Imprint MT Shadow", 15), bg="black", fg="red", bd=2,relief=RIDGE,cursor="circle",command= lambda : page4(self.window)).place(x=0, y=140, width=248, height=35)
        self.report = Button(self.window, text="ROOM CHECKOUT",font=("Imprint MT Shadow", 15), bg="black", fg="red", bd=2,relief=RIDGE,cursor="circle",command= lambda : page5(self.window)).place(x=0, y=210, width=248, height=35)
        self.logout = Button(self.window, text="LOG OUT",font=("Imprint MT Shadow", 15), bg="black", fg="red", bd=2,relief=RIDGE,cursor="circle",command=self.logout_window).place(x=0, y=245, width=248, height=35)
        self.window.mainloop()

    def logout_window(self):
        self.window.destroy()
        from main import Hotelmanagement
        Hotelmanagement()

if __name__ == '__main__':
    main_menu()