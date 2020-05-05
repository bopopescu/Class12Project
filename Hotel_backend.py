from tkinter import *
import mysql.connector
import tkinter.messagebox

def daily_taasks():
    """Removes bookings that have ended and set room status unoccupied which aren't booked currently"""

    MyDb = mysql.connector.connect(user="root", password="", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    cursor.execute("DELETE FROM hotelbookings WHERE cout <(SELECT curdate())")
    cursor.execute("UPDATE rooms SET status=0 WHERE roomn NOT IN (SELECT hotelbookings.roomno FROM hotelbookings);")
    MyDb.commit()
    MyDb.close()

def showbookings():
    """Function to show the bookings currently active in a tabular form"""

    MyDb = mysql.connector.connect(user="root", password="", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    cursor.execute('SELECT * FROM hotelbookings')
    Data = cursor.fetchall()
    MyDb.close()

    # ===================================================================================================================
    Show = Tk()
    Show.state('zoomed')
    Show.title("Hotel Management System")

    def quitwin():
        Show.destroy()

    # ===================================================================================================================

    mainframe = Frame(Show, bg='powder blue', padx=10, pady=10)
    mainframe.pack(fill='both', expand=1)

    topframe = Frame(mainframe, bd=14, relief='ridge', bg='ghost white', height=100, width=750, padx=70, pady=5)
    topframe.pack(pady=10)

    heading = Frame(topframe, bg='ghost white')
    heading.pack(side=LEFT)

    content = Frame(mainframe, bd=8, relief='ridge', bg='powder blue', height=600, width=750, padx=80, pady=30)
    content.pack(pady=10, fill='both', expand=1)

    # ===================================================================================================================

    lblheading = Label(heading, text='CURRENT BOOKINGS', font='times 36 bold', bg='ghost white')
    lblheading.pack(padx=50)

    btnquit = Button(topframe, bd=4, text='Quit', height=1, width=13, font='arial 16', bg='cadet blue',
                     activeforeground="dark blue", command=quitwin)
    btnquit.pack(side=RIGHT)

    h1 = Label(content, padx=10, text="Booking ID", font='times 16').grid(row=0, column=0)
    h2 = Label(content, padx=20, text="Name", font='times 16').grid(row=0, column=1)
    h3 = Label(content, padx=20, text="Surname", font='times 16').grid(row=0, column=2)
    h4 = Label(content, padx=50, text="Email", font='times 16').grid(row=0, column=3)
    h5 = Label(content, padx=50, text="Address", font='times 16').grid(row=0, column=4)
    h1 = Label(content, padx=60, text="Mobile", font='times 16').grid(row=0, column=5)
    h2 = Label(content, padx=15, text="Room No", font='times 16').grid(row=0, column=6)
    h3 = Label(content, padx=15, text="Meal", font='times 16').grid(row=0, column=7)
    h4 = Label(content, padx=15, text="Checkin Date", font='times 16').grid(row=0, column=8)
    h5 = Label(content, padx=15, text="Checkout Date", font='times 16').grid(row=0, column=9)

    row = 1
    for i in Data:
        column = 0
        for j in i:
            lbldata = Label(content, bg="powder blue", padx=15, text=j, pady=8)
            lbldata.grid(row=row, column=column)
            column += 1
        row += 1

def addnew(name,surname,email,address,mobile,rtype,meal,cin,cout):
    """The add new function used to insert recordsof data in bookings able"""

    MyDb = mysql.connector.connect(user="root", password="", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    cursor.execute("SELECT roomn FROM rooms WHERE status=0 and type = %s", (rtype,))
    nolist = cursor.fetchall()

    if len(nolist) == 0:
        tkinter.messagebox.showerror("Error", "No Rooms Available")
    else:
        roomno = nolist[0][0]
        sql = "INSERT INTO hotelbookings (name,surname,email,address,mobile,roomno,meal,cin,cout) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (name, surname, email, address, mobile, roomno, meal, cin, cout )
        cursor.execute(sql, val)

    cursor.execute("SELECT bookingid,roomno FROM hotelbookings WHERE roomno=%s", (roomno,))
    showdata = cursor.fetchall()
    tkinter.messagebox.showinfo("ID & Room No.","Your Booking ID is: " + str(showdata[0][0]) + " and Room No is: " + str(showdata[0][1]))
    cursor.execute("UPDATE rooms SET status=1 WHERE roomn=%s", (roomno,))

    MyDb.commit()
    MyDb.close()

def cancel(id):
    """Cancel function to delete a currently active booking"""

    MyDb = mysql.connector.connect(user="root", password="", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    response=tkinter.messagebox.askquestion("Confirm", "Are you sure?")
    if response=='yes':
        cursor.execute("SELECT bookingid FROM hotelbookings WHERE bookingid=%s", (id,))
        if len(cursor.fetchall())==0:
            tkinter.messagebox.showerror("Error", "No Such Booking")
        else:
            cursor.execute("DELETE FROM hotelbookings WHERE bookingid=%s", (id,))
            tkinter.messagebox.showinfo("Message", "Booking Has been Canceled")
            MyDb.commit()
    MyDb.close()

if __name__ == 'Hotel_backend':
    daily_taasks()
