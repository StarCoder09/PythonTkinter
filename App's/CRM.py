'''
This App illustrates how to make a Customer Relationship Management tool with Tkinter
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import csv
from tkinter import ttk

window = Tk()
window.title("CRM")
window.iconbitmap('D:/e-Learning/Tkinter/Images/Database.ico')

#Connect to MySQL
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Harshman@my59l",
    database = "zodiac"
        )

#check to see if connection was made
#print(mydb)

#create  cursor to initialize
cur = mydb.cursor()

'''
#Create database
cur.execute("CREATE DATABASE zodiac")

#test the db
cur.execute("SHOW DATABASES")
for db in cur:    print(db)

cur.execute("DROP TABLE customer")
'''

#create table
cur.execute("CREATE TABLE IF NOT EXISTS customer (f_name VARCHAR(255), \
    l_name VARCHAR(255), \
    pincode int(10), \
    price DECIMAL(10, 2), \
    user_id INT AUTO_INCREMENT PRIMARY KEY)")

'''
#Alternate table <- do this only one time.
cur.execute("ALTER TABLE customer ADD (\
    email VARCHAR(255), \
    address_1 VARCHAR(255), \
    address_2 VARCHAR(255), \
    city VARCHAR(255), \
    state VARCHAR(255), \
    country VARCHAR(255), \
    phone VARCHAR(255))")

#show tables
cur.execute("SELECT * FROM customer")
print(cur.description)

for thing in cur.description:
    print(thing)
'''

#create clear function
def clear_cus():
    f_name_bx.delete(0, END)
    l_name_bx.delete(0, END)
    address1_bx.delete(0, END)
    address2_bx.delete(0, END)
    city_bx.delete(0, END)
    state_bx.delete(0, END)
    pincode_bx.delete(0, END)
    country_bx.delete(0, END)
    user_id_bx.delete(0, END)
    email_bx.delete(0, END)
    phone_bx.delete(0, END)
    price_bx.delete(0, END)

#create add cus function
def add_cus():
    sql_command = "INSERT INTO customer (f_name, l_name, pincode, price, user_id, email, address_1, address_2, city, state, country, phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (f_name_bx.get(), l_name_bx.get(), pincode_bx.get(), price_bx.get(), user_id_bx.get(), email_bx.get(), address1_bx.get(), address2_bx.get(), city_bx.get(), state_bx.get(), country_bx.get(), phone_bx.get())
    cur.execute(sql_command, values)

    #commit changes
    mydb.commit()
    clear_cus()
    messagebox.showinfo("Alert","Recorded your Data, Thank you!")

#write csv
def wrt_csv(result):
    with open('customers.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)
    messagebox.showinfo("CSV Alert","Record saved into Excel, check your Directory...")

#list customers
def list_cus():
    lst_cus = Tk()
    lst_cus.title("List of our Customers")
    lst_cus.iconbitmap('D:/e-Learning/Tkinter/Images/Database.ico')
    lst_cus.geometry("900x400")

    #query the Database
    cur.execute("SELECT * FROM customer")
    result = cur.fetchall()
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_lbl = Label(lst_cus, text=y)
            lookup_lbl.grid(row=index, column=num, padx=5, pady=5, sticky=W)
            num += 1
    csv_btn = Button(lst_cus, text="Save to Excel", command=lambda: wrt_csv(result), fg="green")
    csv_btn.grid(row=index+1, column=0, padx=5, pady=5)

    #delete function
    def delete():
        dlt_cus = Tk()
        dlt_cus.title("List of our Customers")
        dlt_cus.iconbitmap('D:/e-Learning/Tkinter/Images/Delete.ico')
        dlt_cus.geometry("1000x300")

        def delete_now(id, index):
            sql = "DELETE FROM customer WHERE user_id = %s"
            name = (id, )
            result = cur.execute(sql, name)
            mydb.commit()
            messagebox.showinfo("Delete Alert","Record has been Deleted!")
            dlt_cus.destroy()
            lst_cus.destroy()

        def dropp():
            selected = drop.get()
            sql = ""
            if selected == "Delete by...":
                messagebox.showinfo("Alert","Hey! Select an option in drop down box")
            if selected == "First name":
                sql = "SELECT * FROM customer WHERE f_name = %s"
            if selected == "Last name":
                sql = "SELECT * FROM customer WHERE l_name = %s"
            if selected == "Address":
                sql = "SELECT * FROM customer WHERE address_1 = %s"
            if selected == "City":
                sql = "SELECT * FROM customer WHERE city = %s"
            if selected == "State":
                sql = "SELECT * FROM customer WHERE state = %s"
            if selected == "Pincode":
                sql = "SELECT * FROM customer WHERE pincode = %s"
            if selected == "Email Id":
                sql = "SELECT * FROM customer WHERE email = %s"
            if selected == "User Id":
                sql = "SELECT * FROM customer WHERE user_id = %s"
            if selected == "Country":
                sql = "SELECT * FROM customer WHERE country = %s"
            if selected == "Phone":
                sql = "SELECT * FROM customer WHERE phone = %s"

        
            s = delete_box.get()
            name = (s, )
            result = cur.execute(sql, name)
            result = cur.fetchall()

            if not result:
                result = "Record not found..."
                s_lbl = Label(dlt_cus, text=result)
                s_lbl.grid(row=2, column=0)
            else:
                for index, x in enumerate(result):
                    num = 0
                    index += 2
                    id_ref = str(x[4])
                    dlt_btn = Button(dlt_cus, text="Delete Customer", command=lambda: delete_now(id_ref, index))
                    dlt_btn.grid(row=index, column=num)
                    for y in x:
                        s_lbl = Label(dlt_cus, text=y)
                        s_lbl.grid(row=index, column=num+1)
                        num += 1

        delete_box = Entry(dlt_cus)
        delete_box.grid(row=0, column=1, padx=10, pady=10)
    
        delete_lbl = Label(dlt_cus, text="Delete Customer :")
        delete_lbl.grid(row=0, column=0, padx=10, pady=10)
    
        delete_btn = Button(dlt_cus, text="Search", command=dropp)
        delete_btn.grid(row=0, column=2, padx=10, pady=10)
    
        #drop down box
        drop = ttk.Combobox(dlt_cus, value=["Delete by...", "First name", "Last name", "Address", "City", "State", "Pincode", "Email Id", "User Id", "Phone", "Country"])
        drop.current(0)
        drop.grid(row=0, column=3)

    dlt_btn = Button(lst_cus, text="Delete Customers", command=delete)
    dlt_btn.grid(row=index+1, column=10, columnspan=6, padx=5, pady=5)

#define search button
def search_cus():
    srch_cus = Tk()
    srch_cus.title("Search for Customers")
    srch_cus.iconbitmap('D:/e-Learning/Tkinter/Images/find.ico')
    srch_cus.geometry("1100x600")

    def update():
        sql_command = """UPDATE customer SET f_name = %s, \
                        l_name = %s, \
                        pincode = %s, \
                        price = %s, \
                        user_id = %s, \
                        email = %s, \
                        address_1 = %s, \
                        address_2 = %s, \
                        city = %s, \
                        state = %s, \
                        country = %s, \
                        phone = %s \
                        WHERE user_id = %s"""
        f_name = f_name_bx1.get()
        l_name = l_name_bx1.get()
        address_1 = address1_bx1.get()
        address_2 = address2_bx1.get()
        city = city_bx1.get()
        state = state_bx1.get()
        pincode = pincode_bx1.get()
        country = country_bx1.get()
        user_id = user_id_bx1.get()
        email = email_bx1.get()
        phone = phone_bx1.get()
        price = price_bx1.get()

        id_value = id_bx1.get()
        inputs = (f_name, l_name, pincode, price, user_id, email, address_1, address_2, city, state, country, phone, id_value)

        cur.execute(sql_command, inputs)
        mydb.commit()
        messagebox.showinfo("Update Alert","Record Updated, Thank you!!!")
        srch_cus.destroy()

    def edit_now(id, index):
        sql2 = "SELECT * FROM customer WHERE user_id = %s"
        name2 = (id, )
        result2 = cur.execute(sql2, name2)
        result2 = cur.fetchall()
        #print(result2)
        
        index += 1
        #create main form
        f_name_lbl = Label(srch_cus, text="First Name :").grid(row=index+1, column=0, sticky=W, padx=10)
        l_name_lbl = Label(srch_cus, text="Last Name :").grid(row=index+2, column=0, sticky=W, padx=10)
        address1_lbl = Label(srch_cus, text="Address 1 :").grid(row=index+3, column=0, sticky=W, padx=10)
        address2_lbl = Label(srch_cus, text="Address 2 :").grid(row=index+4, column=0, sticky=W, padx=10)
        city_lbl = Label(srch_cus, text="City :").grid(row=index+5, column=0, sticky=W, padx=10)
        state_lbl = Label(srch_cus, text="State :").grid(row=index+6, column=0, sticky=W, padx=10)
        pincode_lbl = Label(srch_cus, text="Pincode :").grid(row=index+7, column=0, sticky=W, padx=10)
        country_lbl = Label(srch_cus, text="Country :").grid(row=index+8, column=0, sticky=W, padx=10)
        user_id_lbl = Label(srch_cus, text="Username :").grid(row=index+9, column=0, sticky=W, padx=10)
        email_lbl = Label(srch_cus, text="Email ID :").grid(row=index+10, column=0, sticky=W, padx=10)
        phone_lbl = Label(srch_cus, text="Phone Number :").grid(row=index+11, column=0, sticky=W, padx=10)
        price_lbl = Label(srch_cus, text="Price Paid :").grid(row=index+12, column=0, sticky=W, padx=10)
        id_lbl = Label(srch_cus, text="User ID").grid(row=index+13, column=0, sticky=W, padx=10)
        
        #Entry boxes
        global f_name_bx1
        f_name_bx1 = Entry(srch_cus)
        f_name_bx1.grid(row=index+1, column=1, pady=5, padx=5)
        f_name_bx1.insert(0, result2[0][0])
        
        global l_name_bx1
        l_name_bx1 = Entry(srch_cus)
        l_name_bx1.grid(row=index+2, column=1, pady=5, padx=5)
        l_name_bx1.insert(0, result2[0][1])
        
        global address1_bx1
        address1_bx1 = Entry(srch_cus)
        address1_bx1.grid(row=index+3, column=1, pady=5, padx=5)
        address1_bx1.insert(0, result2[0][6])
        
        global address2_bx1
        address2_bx1 = Entry(srch_cus)
        address2_bx1.grid(row=index+4, column=1, pady=5, padx=5)
        address2_bx1.insert(0, result2[0][7])
        
        global city_bx1
        city_bx1 = Entry(srch_cus)
        city_bx1.grid(row=index+5, column=1, pady=5, padx=5)
        city_bx1.insert(0, result2[0][8])
        
        global state_bx1
        state_bx1 = Entry(srch_cus)
        state_bx1.grid(row=index+6, column=1, pady=5, padx=5)
        state_bx1.insert(0, result2[0][9])
        
        global pincode_bx1
        pincode_bx1 = Entry(srch_cus)
        pincode_bx1.grid(row=index+7, column=1, pady=5, padx=5)
        pincode_bx1.insert(0, result2[0][2])
        
        global country_bx1
        country_bx1 = Entry(srch_cus)
        country_bx1.grid(row=index+8, column=1, pady=5, padx=5)
        country_bx1.insert(0, result2[0][10])
        
        global user_id_bx1
        user_id_bx1 = Entry(srch_cus)
        user_id_bx1.grid(row=index+9, column=1, pady=5, padx=5)
        user_id_bx1.insert(0, result2[0][4])
        
        global email_bx1
        email_bx1 = Entry(srch_cus)
        email_bx1.grid(row=index+10, column=1, pady=5, padx=5)
        email_bx1.insert(0, result2[0][5])
        
        global phone_bx1
        phone_bx1 = Entry(srch_cus)
        phone_bx1.grid(row=index+11, column=1, pady=5, padx=5)
        phone_bx1.insert(0, result2[0][11])
        
        global price_bx1
        price_bx1 = Entry(srch_cus)
        price_bx1.grid(row=index+12, column=1, pady=5, padx=5)
        price_bx1.insert(0, result2[0][3])
        
        global id_bx1
        id_bx1 = Entry(srch_cus)
        id_bx1.grid(row=index+13, column=1, pady=5, padx=5)
        id_bx1.insert(0, result2[0][4])

        save_btn = Button(srch_cus, text="Update Record", command=update)
        save_btn.grid(row=index+14, column=0, padx=10, pady=10)

    def search_now():
        selected = drop.get()
        sql = ""
        if selected == "Search by...":
            messagebox.showinfo("Alert","Hey! Select an option in drop down box")
        if selected == "First name":
            sql = "SELECT * FROM customer WHERE f_name = %s"
        if selected == "Last name":
            sql = "SELECT * FROM customer WHERE l_name = %s"
        if selected == "Address":
            sql = "SELECT * FROM customer WHERE address_1 = %s"
        if selected == "City":
            sql = "SELECT * FROM customer WHERE city = %s"
        if selected == "State":
            sql = "SELECT * FROM customer WHERE state = %s"
        if selected == "Pincode":
            sql = "SELECT * FROM customer WHERE pincode = %s"
        if selected == "Email Id":
            sql = "SELECT * FROM customer WHERE email = %s"
        if selected == "User Id":
            sql = "SELECT * FROM customer WHERE user_id = %s"
        if selected == "Country":
            sql = "SELECT * FROM customer WHERE country = %s"
        if selected == "Phone":
            sql = "SELECT * FROM customer WHERE phone = %s"

        
        s = search_box.get()
        name = (s, )
        result = cur.execute(sql, name)
        result = cur.fetchall()

        if not result:
            result = "Record not found..."
            s_lbl = Label(srch_cus, text=result)
            s_lbl.grid(row=2, column=0)
        else:
            for index, x in enumerate(result):
                num = 0
                index += 2
                id_ref = str(x[4])
                edit_btn = Button(srch_cus, text="Edit Customer", command=lambda: edit_now(id_ref, index))
                edit_btn.grid(row=index, column=num)
                for y in x:
                    s_lbl = Label(srch_cus, text=y)
                    s_lbl.grid(row=index, column=num+1)
                    num += 1
            csv_btn = Button(srch_cus, text="Save to Excel", command=lambda: wrt_csv(result))
            csv_btn.grid(row=index+1, column=0, padx=5, pady=5)
        
    search_box = Entry(srch_cus)
    search_box.grid(row=0, column=1, padx=10, pady=10)
    
    search_lbl = Label(srch_cus, text="Search Customer :")
    search_lbl.grid(row=0, column=0, padx=10, pady=10)
    
    search_btn = Button(srch_cus, text="Search", command=search_now)
    search_btn.grid(row=0, column=2, padx=10, pady=10)
    
    #drop down box
    drop = ttk.Combobox(srch_cus, value=["Search by...", "First name", "Last name", "Address", "City", "State", "Pincode", "Email Id", "User Id", "Phone", "Country"])
    drop.current(0)
    drop.grid(row=0, column=3)
    
#create label - Layout Section
title_lbl = Label(window, text="Zodiac Syndicate Database", font=("helvetica", 16))
title_lbl.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

#create main form
f_name_lbl = Label(window, text="First Name :").grid(row=1, column=0, sticky=W, padx=10)
l_name_lbl = Label(window, text="Last Name :").grid(row=2, column=0, sticky=W, padx=10)
address1_lbl = Label(window, text="Address 1 :").grid(row=3, column=0, sticky=W, padx=10)
address2_lbl = Label(window, text="Address 2 :").grid(row=4, column=0, sticky=W, padx=10)
city_lbl = Label(window, text="City :").grid(row=5, column=0, sticky=W, padx=10)
state_lbl = Label(window, text="State :").grid(row=6, column=0, sticky=W, padx=10)
pincode_lbl = Label(window, text="Pincode :").grid(row=7, column=0, sticky=W, padx=10)
country_lbl = Label(window, text="Country :").grid(row=8, column=0, sticky=W, padx=10)
user_id_lbl = Label(window, text="Username :").grid(row=9, column=0, sticky=W, padx=10)
email_lbl = Label(window, text="Email ID :").grid(row=10, column=0, sticky=W, padx=10)
phone_lbl = Label(window, text="Phone Number :").grid(row=11, column=0, sticky=W, padx=10)
price_lbl = Label(window, text="Price Paid :").grid(row=12, column=0, sticky=W, padx=10)

#Entry boxes
f_name_bx = Entry(window)
f_name_bx.grid(row=1, column=1, pady=5, padx=5)
l_name_bx = Entry(window)
l_name_bx.grid(row=2, column=1, pady=5, padx=5)
address1_bx = Entry(window)
address1_bx.grid(row=3, column=1, pady=5, padx=5)
address2_bx = Entry(window)
address2_bx.grid(row=4, column=1, pady=5, padx=5)
city_bx = Entry(window)
city_bx.grid(row=5, column=1, pady=5, padx=5)
state_bx = Entry(window)
state_bx.grid(row=6, column=1, pady=5, padx=5)
pincode_bx = Entry(window)
pincode_bx.grid(row=7, column=1, pady=5, padx=5)
country_bx = Entry(window)
country_bx.grid(row=8, column=1, pady=5, padx=5)
user_id_bx = Entry(window)
user_id_bx.grid(row=9, column=1, pady=5, padx=5)
email_bx = Entry(window)
email_bx.grid(row=10, column=1, pady=5, padx=5)
phone_bx = Entry(window)
phone_bx.grid(row=11, column=1, pady=5, padx=5)
price_bx = Entry(window)
price_bx.grid(row=12, column=1, pady=5, padx=5)

#create buttons
add_cus_btn = Button(window, text="Add Customer to Database", command=add_cus)
add_cus_btn.grid(row=13, column=0, padx=10, pady=10)
clear_cus_btn = Button(window, text="Clear Feilds", command=clear_cus)
clear_cus_btn.grid(row=13, column=1, padx=10, pady=10)

# list cus button
list_cus_btn = Button(window, text="List our Customers", command=list_cus)
list_cus_btn.grid(row=14, column=0, sticky=W, padx=10, pady=10)

#search customers
srh_cus_btn = Button(window, text="Search and Edit Customers", command=search_cus)
srh_cus_btn.grid(row=14, column=1, sticky=W, padx=10, pady=10)

#event handler
window.mainloop()
