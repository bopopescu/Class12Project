import mysql.connector
from tkinter import *
def daily_taasks():
    MyDb = mysql.connector.connect(user="root", password="shivang280703", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    cursor.execute("delete from bookings where cout <(select curdate())")
    cursor.execute("update rooms set status=0 where roomn not in (select bookings.roomno from bookings);")
    mydb.commit()
    MyDb.close()

def shwin():
    MyDb = mysql.connector.connect(user="root", password="shivang280703", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    cursor.execute("SELECT bookingid,name,roomno,cin,cout FROM bookings")
    data = cursor.fetchall()
    sh = Tk()
    sh.geometry('520x500')
    sh.title("CURRENT BOOKINGS")
    welc = Label(sh, text='Current Bookings', relief='solid', font='times 32 bold').pack()
    frame = Frame(sh, bd=10, height=600, width=450, relief=RIDGE, bg="powder blue")
    frame.place(x=20, y=100)
    h1 = Label(frame, padx=15, text="Booking ID").grid(row=0, column=0)
    h2 = Label(frame, padx=15, text="Name").grid(row=0, column=1)
    h3 = Label(frame, padx=15, text="Room No").grid(row=0, column=2)
    h4 = Label(frame, padx=15, text="Checkin Date").grid(row=0, column=3)
    h5 = Label(frame, padx=15, text="Checkout Date").grid(row=0, column=4)
    m = 2
    for i in data:
        n = 0
        for j in i:
            x = Label(frame, bg="powder blue", padx=15, text=j).grid(row=m, column=n)
            n += 1
        m += 2
    mainloop()
if __name__=='Hotel_backend':
    print('import Successfull')