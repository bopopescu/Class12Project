from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from Hotel_backend import *

class MainWindow:
    def __init__(self, master):
        self.master=master
        self.master.geometry('1330x750')
        self.master.title("Hotel Management System")
        self.master.config(bg='powder blue')

        #======================================Frames============================================================

        frame=Frame(self.master)
        frame.grid()

        mainframe=Frame(frame)
        mainframe.pack(side=LEFT,fill='both',expand=1)

        sideframe=Frame(frame)
        sideframe.pack(side=RIGHT)

        topframe=Frame(mainframe, bd=14, bg='powder blue', relief='ridge', height=120, width=1100, padx=400, pady=5)
        topframe.pack(side=TOP)

        midframe = Frame(mainframe, bd=14, bg='cadet blue', relief='ridge', height=100, width=1080, pady=10, padx=10)
        midframe.pack(side=BOTTOM,fill='both',expand=1)

        leftframe = Frame(midframe, bd=14, bg='powder blue', relief='ridge', height=590, width=680, padx=40, pady=30)
        leftframe.pack(side=LEFT)

        rightframe = Frame(midframe, bd=14, bg='cadet blue', relief='ridge', height=590, width=380, pady=20)
        rightframe.pack(side=RIGHT,fill='both',expand=1)

        buttonframe=Frame(sideframe, bd=14, bg='powder blue', relief='ridge', height=740, width=240, padx=10, pady=150)
        buttonframe.pack(side=RIGHT)

        Name = StringVar()
        surname = StringVar()
        email = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        Room = StringVar()
        Meal = StringVar()
        Chin = StringVar()
        Chout = StringVar()
        Cid = StringVar()

        #=======================================Widgits============================================================

        self.lblwelcome = Label(topframe, text='WELCOME', bg='powder blue', font='times 36 bold').pack()
        self.lblnew = Label(midframe, text='  New Bookings  ', bg='cadet blue', font='times 25 bold', relief='solid').place(x=230,y=10)

        self.lblname = Label(leftframe, text='Name: ', bg='powder blue', font='times 16 bold').grid(row=0, column=0, pady=5)
        self.txtname = Entry(leftframe, font='times 16 bold', textvariable=Name, width=35).grid(row=0, column=1)

        self.lblsurname = Label(leftframe, text='Surname: ', bg='powder blue', font='times 16 bold').grid(row=1, column=0, pady=5)
        self.txtsurn = Entry(leftframe, font='times 16 bold', textvariable=surname, width=35).grid(row=1, column=1)

        self.lblemail = Label(leftframe, text='Email: ', bg='powder blue', font='times 16 bold').grid(row=2, column=0, pady=5)
        self.txtemail = Entry(leftframe, font='times 16 bold', textvariable=email, width=35).grid(row=2, column=1)

        self.lbladdress = Label(leftframe, text='Address: ', bg='powder blue', font='times 16 bold').grid(row=3, column=0, pady=5)
        self.txtaddress = Entry(leftframe, font='times 16 bold', textvariable=Address, width=35).grid(row=3, column=1)

        self.lblmobile = Label(leftframe, text='Mobile No.', bg='powder blue', font='times 16 bold').grid(row=4, column=0, pady=5)
        self.txtmobile = Entry(leftframe, font='times 16 bold', textvariable=Mobile, width=35).grid(row=4, column=1)

        self.lblroom = Label(leftframe, text='Room Type: ', bg='powder blue', font='times 16 bold').grid(row=5, column=0, pady=5)
        self.cboroom = ttk.Combobox(leftframe, textvariable=Room, state='readonly', font='times 15', width=35,
                                    value=('Single Deluxe', 'Double Deluxe', 'Executive', 'Family Suit')).grid(row=5, column=1)

        self.lblmeal = Label(leftframe, text='Meal Type: ', bg='powder blue', font='times 16 bold').grid(row=6, column=0, pady=5)
        self.cbomeal = ttk.Combobox(leftframe, textvariable=Meal, state='readonly', font='times 15', width=35,
                                    value=('Breakfast', 'Dinner', 'Combo', 'All three')).grid(row=6, column=1)

        self.lblcheckin = Label(leftframe, text='Check In Date: ', bg='powder blue', font='times 16 bold').grid(row=7, column=0, pady=5)
        self.txtchecin = Entry(leftframe, font='times 16 bold', textvariable=Chin, width=25).grid(row=7, column=1)

        self.lblcheckout = Label(leftframe, text='Check Out Date: ', bg='powder blue', font='times 16 bold').grid(row=8, column=0, pady=5)
        self.txtcheckout = Entry(leftframe, font='times 16 bold', textvariable=Chout, width=25).grid(row=8, column=1)

        self.lblcancel = Label(rightframe, text='  Cancel Bookings  ', bg='cadet blue', font='times 25 bold', relief='solid').pack()
        self.lblid = Label(rightframe, text='Booking ID ', bg='powder blue', font='times 16 bold').pack(pady=20)
        self.txtid = Entry(rightframe, font='times 16 bold', textvariable=Cid, width=25).pack()

        #=======================================Functions=========================================================

        def exit():
            iexit= tkinter.messagebox.askyesno('Hotel System','Confirm, If you Want to exit?')
            if iexit>0:
                root.destroy()
                return

        def reset():
            Name.set('')
            surname.set('')
            email.set('')
            Address.set('')
            Mobile.set('')
            Room.set('')
            Meal.set('')
            Chin.set('')
            Chout.set('')
            Cid.set('')

        #======================================Buttons============================================================

        self.btn1 = Button(buttonframe, bd=4, text='Show Bookings', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue", command=showbookings).grid(row=0, column=0, pady=6)

        self.btn2 = Button(buttonframe, bd=4, text='Submit', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue").grid(row=1, column=0, pady=6)

        self.btn3 = Button(buttonframe, bd=4, text='Clear', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue", command=reset).grid(row=2, column=0, pady=6)

        self.btn4 = Button(buttonframe, bd=4, text='Cancel', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue").grid(row=3, column=0, pady=6)

        self.btn5 = Button(buttonframe, bd=4, text='Exit', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue", command=exit).grid(row=4, column=0, pady=6)



if __name__ == '__main__':
    root=Tk()
    root.iconbitmap('favicon.ico')
    application=MainWindow(root)
    root.mainloop()