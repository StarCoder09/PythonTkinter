'''
This App is to illustrate simple CRUD operations using Tkinter.
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

window = Tk()
window.title("Database")
window.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')
window.geometry("400x400")

#----- Run the below commented code one time only for just to create database. ----#
'''
#Databases
conn = sqlite3.connect('address_book.db')
c = conn.cursor()

#create table

c.execute("""CREATE TABLE address (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )""")

conn.commit()
conn.close()
'''
#---------------------------------------------------------------------------------#

# create function to delete records
def delete():
    #Create a DB or connect
    conn = sqlite3.connect('address_book.db')
    #Create cursor
    c = conn.cursor()

    #delete records
    c.execute("DELETE from address WHERE oid = " + dlt_box.get())
    dlt_box.delete(0, END)
    
    #commit changes
    conn.commit()
    #close connection
    conn.close()

# create edit function
def edit():
    #Create a DB or connect
    conn = sqlite3.connect('address_book.db')
    #Create cursor
    c = conn.cursor()
    
    record_id = dlt_box.get()
    
    c.execute("""UPDATE address SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode

            WHERE oid = :oid""",
              {'first': f_name_updator.get(),
               'last': l_name_updator.get(),
               'address': address_updator.get(),
               'city': city_updator.get(),
               'state': state_updator.get(),
               'zipcode': zipcode_updator.get(),
               'oid': record_id
              })

    #commit changes
    conn.commit()
    #close connection
    conn.close()

    messagebox.showinfo("Alert!", "Records saved!!!")
    updator.destroy()

# create function to update
def update():
    global updator
    updator = Tk()
    updator.title("Update Database")
    updator.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')
    #updator.geometry("400x200")
    
    #Create a DB or connect
    conn = sqlite3.connect('address_book.db')
    #Create cursor
    c = conn.cursor()
    
    record_id = dlt_box.get()
    #Query DB
    c.execute("SELECT * from address WHERE oid = " + record_id)
    records = c.fetchall()#it can be fetchone(), fetchmany(value), fetchall()
    # print(records)
    
    #loping results
    #print_records = ''
    #for record in records:
        #print_records += str(record) + "\n"
        #print_records += str(record[0]) + " " + str(record[1]) + "\n"
        #print_records += str(record[0]) + " " + str(record[1]) + " " + "\t\t" + str(record[6]) + "\n"
    
    #commit changes
    conn.commit()
    #close connection
    conn.close()

    #create global
    global f_name_updator
    global l_name_updator
    global address_updator
    global city_updator
    global state_updator
    global zipcode_updator

    # Create text boxes
    f_name_updator = Entry(updator, width=30)
    f_name_updator.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_updator = Entry(updator, width=30)
    l_name_updator.grid(row=1, column=1)

    address_updator = Entry(updator, width=30)
    address_updator.grid(row=2, column=1)

    city_updator = Entry(updator, width=30)
    city_updator.grid(row=3, column=1)

    state_updator = Entry(updator, width=30)
    state_updator.grid(row=4, column=1)

    zipcode_updator = Entry(updator, width=30)
    zipcode_updator.grid(row=5, column=1)

    #create text box labels
    f_name_lbl = Label(updator, text="First Name:")
    f_name_lbl.grid(row=0, column=0, pady=(10, 0))

    l_name_lbl = Label(updator, text="Last Name:")
    l_name_lbl.grid(row=1, column=0)

    address_lbl = Label(updator, text="Address:")
    address_lbl.grid(row=2, column=0)

    city_lbl = Label(updator, text="City:")
    city_lbl.grid(row=3, column=0)

    state_lbl = Label(updator, text="State:")
    state_lbl.grid(row=4, column=0)

    zipcode_lbl = Label(updator, text="Zipcode:")
    zipcode_lbl.grid(row=5, column=0)

    #looping results
    for record in records:
        f_name_updator.insert(0, record[0])
        l_name_updator.insert(0, record[1])
        address_updator.insert(0, record[2])
        city_updator.insert(0, record[3])
        state_updator.insert(0, record[4])
        zipcode_updator.insert(0, record[5])

    #create an update button
    save_btn = Button(updator, text="Save Records", command=edit)
    save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=105)

#Create submit function
def submit():
    #Create a DB or connect
    conn = sqlite3.connect('address_book.db')
    #Create cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO address VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            })

    #commit changes
    conn.commit()
    #close connection
    conn.close()
    #Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#Create query function
def query():
    #Create a DB or connect
    conn = sqlite3.connect('address_book.db')
    #Create cursor
    c = conn.cursor()

    #Query DB
    c.execute("SELECT *, oid FROM address")
    records = c.fetchall()#it can be fetchone(), fetchmany(value), fetchall()
    # print(records)
    
    #loping results
    #print_records = ''
    f=open('Records.txt','w')
    for record in records:
        f.write(str(record) + "\n")
    f.close()
        #print_records += str(record[0]) + " " + str(record[1]) + "\n"
        #print_records += str(record[0]) + " " + str(record[1]) + " " + "\t\t" + str(record[6]) + "\n"

    #query_lbl = Label(window, text=print_records)
    #query_lbl.grid(row=12, column=0, columnspan=2)
    
    #commit changes
    conn.commit()
    #close connection
    conn.close()
    #Clear the text boxes

    import subprocess as sp
    pName='notepad.exe'
    fName='Records.txt'
    sp.Popen([pName,fName])

# Create text boxes
f_name = Entry(window, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(window, width=30)
l_name.grid(row=1, column=1)

address = Entry(window, width=30)
address.grid(row=2, column=1)

city = Entry(window, width=30)
city.grid(row=3, column=1)

state = Entry(window, width=30)
state.grid(row=4, column=1)

zipcode = Entry(window, width=30)
zipcode.grid(row=5, column=1)

dlt_box = Entry(window, width=30)
dlt_box.grid(row=9, column=1, pady=5)

#create text box labels
f_name_lbl = Label(window, text="First Name:")
f_name_lbl.grid(row=0, column=0, pady=(10, 0))

l_name_lbl = Label(window, text="Last Name:")
l_name_lbl.grid(row=1, column=0)

address_lbl = Label(window, text="Address:")
address_lbl.grid(row=2, column=0)

city_lbl = Label(window, text="City:")
city_lbl.grid(row=3, column=0)

state_lbl = Label(window, text="State:")
state_lbl.grid(row=4, column=0)

zipcode_lbl = Label(window, text="Zipcode:")
zipcode_lbl.grid(row=5, column=0)

dlt_box_lbl = Label(window, text="ID Number:")
dlt_box_lbl.grid(row=9, column=0, pady=5)

#Create submit button
sb_btn = Button(window, text="Submit UR Data", command=submit)
sb_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

#Create a query btn
query_btn = Button(window, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=105)

#create delete btn
delete_btn = Button(window, text="Delete Records", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=105)

#create an update button
update_btn = Button(window, text="Update Records", command=update)
update_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=105)

#event handler
window.mainloop()
