import mysql.connector
from tkinter import *

def daily_taasks():
    MyDb = mysql.connector.connect(user="root", password="shivang280703", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    MyDb.close()


def showbookings():
    MyDb = mysql.connector.connect(user="root", password="shivang280703", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    Show=Tk()
    Show.geometry('1080x750')
    Show.title("Hotel Management System")

    #===================================================================================================================

    mainframe=Frame(Show, bg='powder blue', padx=10, pady=10)
    mainframe.pack(fill='both', expand=1)

    heading=Frame(mainframe, bd=14, relief='ridge', bg='ghost white', height=100, width=750, padx=70, pady=5)
    heading.pack(pady=10)

    content = Frame(mainframe, bd=8, relief='ridge', bg='powder blue', height=600, width=750, padx=25, pady=30)
    content.pack(pady=10, fill='both', expand=1)

    #===================================================================================================================

    lblheading=Label(heading, text='CURRENT BOOKINGS', font='times 36 bold')
    lblheading.pack()

    h1 = Label(content, padx=10, text="Booking ID", font='times 16').grid(row=0, column=0)
    h2 = Label(content, padx=10, text="Name", font='times 16').grid(row=0, column=1)
    h3 = Label(content, padx=10, text="Surname", font='times 16').grid(row=0, column=2)
    h4 = Label(content, padx=10, text="Email", font='times 16').grid(row=0, column=3)
    h5 = Label(content, padx=10, text="Address", font='times 16').grid(row=0, column=4)
    h1 = Label(content, padx=10, text="Mobile", font='times 16').grid(row=0, column=5)
    h2 = Label(content, padx=10, text="Room No", font='times 16').grid(row=0, column=6)
    h3 = Label(content, padx=10, text="Meal", font='times 16').grid(row=0, column=7)
    h4 = Label(content, padx=10, text="Checkin Date", font='times 16').grid(row=0, column=8)
    h5 = Label(content, padx=10, text="Checkout Date", font='times 16').grid(row=0, column=9)

    MyDb.close()
    mainloop()

if __name__=='Hotel_backend':
    print('import Successfull')
showbookings()