
"""This is the backbone of the App. This program creates a link between the front end and the back-end."""
import SecuriPy
from tkinter import *
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import pandas as pd
from sql_scripts import *
from numeric_queries import *
from visual_queries import *
from visuals import *
import time
import datetime

maintain_label = False
acc = False
lnlb = False
uname = False
#Function to create a Home Page
def home_window():
    global maintain_label
    maintain_label = False
    home = Tk()
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
##    x = (screen_width - 1280) // 2
##    y = (screen_height - 720) // 2

    home.title("Data Sense")
    home.attributes("-fullscreen",True)
    home.overrideredirect(True)

    img = Image.open("images/home.jpg")
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x = -2, y = -2)
    
    def maintain():
        global l, maintain_label
        if not maintain_label:
            l = Label(home, text="Feature Under Development", font="Arial 30 bold", bg="red", fg="black")
            l.pack(side = BOTTOM, anchor="s")
            maintain_label = True
    def quit():
        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
        if result == True:
            home.destroy()
            ()
    
    def switchg():
        home.destroy()
        graph_window()
    def switchn():
        home.destroy()
        numeric_window()
    def switchab():
        home.destroy()
        about_window()
    def switche():
        home.destroy()
        export_window()
    def switcha():
        home.destroy()
        add_window()
    def switchu():
        home.destroy()
        update_window()
    def switchdel():
        home.destroy()
        delete_window()
    def logout():
        home.destroy()
        welcome_window()
        
    Label(home, text = "Welcome to Data Sense", font = "Arial 40 bold", bg = "black", fg = "white").pack()
    Button(home, text = "Add Data", font = "Arial 20 bold", bg="white", command=switcha).pack(pady=20)
    Button(home, text = "Update Data", font = "Arial 20 bold", bg="white", command=maintain).pack(pady=20)
    Button(home, text = "Delete Data", font = "Arial 20 bold", bg="white", command=maintain).pack(pady=20)
    Button(home, text = 'Visual Analysis', font = 'Arial 20 bold', bg='white', command=switchg).pack(pady=20)
    Button(home, text = 'Numeric Analysis', font = 'Arial 20 bold', bg='white', command=switchn).pack(pady=20)
    Button(home, text = "Export Reports", font = "Arial 20 bold", bg = "white", command=switche).pack(pady=20)
    Button(home, text = "About", font = "Arial 20 bold",bg = "white", command=switchab).pack(pady=20)
    Button(home, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = RIGHT,anchor = "se")
    Button(home, text = 'Log Out', font = 'Arial 20 bold', bg='red', command=logout).pack(side = LEFT,anchor = "sw")
    
    home.mainloop()
    
#Function to create a Signup Page
def signup_window():
    global maintain_label
    lnlb = False
    maintain_label = False
    signup = Tk()
    signup.title("Login")
    signup.attributes('-fullscreen', True)
    
    screen_width = signup.winfo_screenwidth()
    screen_height = signup.winfo_screenheight()
    img = Image.open("images/signup.jpg")
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x = -2, y = -2)
    
    def switchlog():
        signup.destroy()
        login_window()
        
    accounts = [SecuriPy.Text.decrypt(usernm[0], "datasense") for usernm in execute_query("select username from users")]
    
    def lenlabel():
        global lnlb
        if not lnlb:
            l = Label(signup, text="Minimum 8 Characters Please", font="Arial 30 bold", bg="red", fg="black")
            l.pack(side = BOTTOM, anchor="s")
            lnlb = True
            
    def unlabel():
        global uname
        if not uname:
            l = Label(signup, text="Username Already Used", font="Arial 30 bold", bg="red", fg="black")
            l.pack(side = BOTTOM, anchor="s")
            uname = True
            
    title = Label(signup, text="Data Sense Signup", font = "Arial 40 bold",bg = "black", fg = "white").pack(pady = 50)
    username_label = Label(signup, text="Username", font = "Arial 35 bold")
    username_label.pack(anchor="center")
    username_entry = Entry(signup, font = "Arial 30 bold")
    username_entry.pack(side = TOP)

    password_label = Label(signup, text="Password", font = "Arial 35 bold")
    password_label.pack(side = TOP)
    password_entry = Entry(signup, show="*", font = "Arial 30 bold")
    password_entry.pack(side = TOP)
    
    def signup_button():
        if username_entry.get() not in accounts:
            if len(password_entry.get()) >= 8:
                u = SecuriPy.Text.encrypt(username_entry.get(), "datasense")
                p = SecuriPy.Text.encrypt(password_entry.get(), "datasense")
                q = f"insert into users (username, password) values ('{u}', '{p}')"
                r = execute_query(q)
                log("New User Registered")
                signup.destroy()
                home_window()
            else:
              lenlabel()
        else:
            unlabel()
          
    button = Button(signup, text="SignUP", font = "Arial 30 bold", command=signup_button).pack(side = TOP)
    Button(signup, text = 'Exit', font = 'Arial 20 bold', bg='red', command=signup.destroy).pack(side = RIGHT,anchor = "se")
    Button(signup, text = 'Go Back', font = 'Arial 20 bold', bg='red', command=switchlog).pack(side = LEFT,anchor = "sw")
    signup.mainloop()
 
#Function to create a Login Page
def login_window():
    global maintain_label
    maintain_label = False
    usr = ""
    def switch():
        login.destroy()
        home_window()
    
    def switchs():
        login.destroy()
        signup_window()
    
    login = Tk()
    login.title("Login")
    login.attributes('-fullscreen', True)

    screen_width = login.winfo_screenwidth()
    screen_height = login.winfo_screenheight()
    img = Image.open("images/login.jpg")
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x = -2, y = -2)
    
    title = Label(login, text="Data Sense Login", font = "Arial 40 bold",bg = "black", fg = "white").pack(pady = 50)
    username_label = Label(login, text="Username", font = "Arial 35 bold")
    username_label.pack(anchor="center")
    username_entry = Entry(login, font = "Arial 30 bold")
    username_entry.pack(side = TOP)

    password_label = Label(login, text="Password", font = "Arial 35 bold")
    password_label.pack(side = TOP)
    password_entry = Entry(login, show="*", font = "Arial 30 bold")
    password_entry.pack(side = TOP)
           
    def login_button():
        usr = 0
        response = execute_query("select * from users")
        for i in range(len(response)):
            if username_entry.get() == SecuriPy.Text.decrypt(response[i][0], "datasense"):
                usr = i
                break
            else:
                usr = -1
        try:
            if password_entry.get() == SecuriPy.Text.decrypt(response[usr][1], "datasense"):
                user = username_entry.get()
                login.destroy() 
                home_window()
            else:
                error_label = Label(login, text="Incorrect username or password",font = "Arial 30", fg="red")
                error_label.pack()
            log(username_entry.get() + " " + "logged in")
        except IndexError:
            global a, acc
            if not acc:
                a = Label(login, text="No Account Found", font="Arial 30 bold", bg="red", fg="black")
                a.pack(side = BOTTOM, anchor="s")
                acc = True
    button = Button(login, text="Login", font = "Arial 30 bold", command=login_button).pack(side = TOP)
    Button(login, text = 'Exit', font = 'Arial 20 bold', bg='red', command=login.destroy).pack(side = BOTTOM,anchor = "se")
    sign = Button(login, text= "Sign UP Instead", font = "Arial 20 bold", bg="skyblue", command=switchs).pack(pady = 30)
    login.mainloop()

def add_window():
    global maintain_label
    maintain_label = False
    add = Tk()
    screen_width = add.winfo_screenwidth()
    screen_height = add.winfo_screenheight()
    add.title("Add/Insert data")
    add.attributes("-fullscreen", True)

    def maintain():
        global l, maintain_label
        if not maintain_label:
            l = Label(add, text="Feature Under Development", font="Arial 30 bold", bg="red", fg="black")
            l.pack(side = BOTTOM, anchor="s")
            maintain_label = True

    def ad():
        add.destroy()
        add_window()
    def switchh():
        add.destroy()
        home_window()
        
    def new_prod():
        global maintain_label
        maintain_label = False
        categ = StringVar()
        categ.set("Category")
        cats = [c[0] for c in execute_query("select distinct(category) from products")]
        def submit_data():
            r = execute_query("select productid from products")
            idl = r[-1][0]
            print(idl+1, prodname.get(), categ.get(), amt.get())
            q = "insert into products values ({}, '{}', '{}', {})".format(idl+1, prodname.get(), categ.get(), amt.get())
            resp = execute_query(q)

            pn.pack_forget()
            prodname.pack_forget()
            cat.pack_forget()
            category.pack_forget()
            at.pack_forget()
            amt.pack_forget()
            sub.pack_forget()
            success = Label(add, text = "Data Entered Successfully", font = "Arial 40 bold", bg = "#090c39", fg = "white")
            success.pack(anchor = CENTER)

        c.pack_forget()
        p.pack_forget()
        o.pack_forget()
        try:
            l.pack_forget()
        except:
            pass
        pn = Label(add, text="Product Name", font = "Arial 20 bold",bg = "#090c39", fg = "white")
        pn.pack(padx = 30, pady = 20)
        prodname = Entry(add, font = "Arial 20 bold")
        prodname.pack(padx = 0, pady= 0)
        cat = Label(add, text="Category", font = "Arial 20 bold",bg = "#090c39", fg = "white")
        cat.pack(padx = 30, pady = 20)
        category = OptionMenu(add, categ, *cats)
        category.config(font=("Arial", 22))
        category.pack(padx = 0,pady= 0)
        at = Label(add, text="Price", font = "Arial 20 bold",bg = "#090c39", fg = "white")
        at.pack(padx = 30, pady = 20)
        amt = Entry(add, font = "Arial 20 bold")
        amt.pack(padx = 0,pady= 0)
        sub = Button(add, text = "Submit", font = "Arial 20 bold", bg = "blue", fg = "white", command = submit_data)
        sub.pack(pady=5)
            
    def new_cust():
        global maintain_label
        maintain_label = False
        def submit_data():
            r = execute_query("select customerid from customers")
            idl = r[-1][0]
            print(idl+1, firstname.get(), lastname.get(), email.get(), address.get())
            q = "insert into customers values ({}, '{}', '{}', '{}', '{}')".format(idl + 1, firstname.get(), lastname.get(), email.get(), address.get())
            resp = execute_query(q)

            fn.pack_forget()
            firstname.pack_forget()
            ln.pack_forget()
            lastname.pack_forget()
            em.pack_forget()
            email.pack_forget()
            ad.pack_forget()
            address.pack_forget()
            sub.pack_forget()

            success = Label(add, text = "Data Entered Successfully", font = "Arial 40 bold", bg = "#090c39", fg = "white")
            success.pack(anchor = CENTER)
            
        c.pack_forget()
        p.pack_forget()
        o.pack_forget()
        try:
            l.pack_forget()
        except:
            pass
        fn = Label(add, text="First Name", font = "Arial 20 bold",bg = "#090c39", fg = "white")
        fn.pack(padx = 30, pady = 20)
        firstname = Entry(add, font = "Arial 20 bold")
        firstname.pack(padx = 0, pady= 0)
        ln = Label(add, text="Last Name", font = "Arial 20 bold",bg = "#090c39", fg = "white")
        ln.pack(padx = 30, pady = 20)
        lastname = Entry(add, font = "Arial 20 bold")
        lastname.pack(padx = 0,pady= 0)
        em = Label(add, text="Email Address", font = "Arial 20 bold",bg = "#090c39", fg = "white")
        em.pack(padx = 30, pady = 20)
        email = Entry(add, font = "Arial 20 bold")
        email.pack(padx = 0,pady= 0)
        ad = Label(add, text="Home Address", font = "Arial 20 bold",bg = "#090c39", fg = "white")
        ad.pack(padx = 30, pady = 20)
        address = Entry(add, font = "Arial 20 bold")
        address.pack(padx = 0,pady= 0)
        sub = Button(add, text = "Submit", font = "Arial 20 bold", bg = "blue", fg = "white", command = submit_data)
        sub.pack(pady=5)
        
    def new_order():
        global maintain_label
        maintain_label = False
        cust = StringVar()
        cust.set("Customer")
        prod = StringVar()
        prod.set("Product")
        
        customers = [ct[0] for ct in execute_query("select firstname from customers")]
        products = [pd[0] for pd in execute_query("select productname from products")]
        prodprice = [pp for pp in execute_query("select productid, price from products")]
        print(customers)
        print(products)
        
        def submit_data():
            ors = execute_query("select orderid from orders")
            lor = ors[-1][0]
            ords = execute_query("select orderdetailid from orderdetails")
            lord = ords[-1][0]
            stt = float(prodprice[products.index(prod.get()) ][1]) * float(qt.get())
            q = "insert into orders values ({}, {}, '{}', {})".format(lor+1, (customers.index(cust.get())+1), date.get(), stt)
            resp = execute_query(q)
            q = "insert into orderdetails values ({}, {}, {}, {}, {})".format(lord + 1, lor+1, (products.index(prod.get())+1), qt.get(), stt)
            resp = execute_query(q)
            cn.pack_forget()
            customer.pack_forget()
            pd.pack_forget()
            product.pack_forget()
            dt.pack_forget()
            date.pack_forget()
            q.pack_forget()
            qt.pack_forget()
            sub.pack_forget()
            success = Label(add, text = "Data Entered Successfully", font = "Arial 40 bold", bg = "#090c39", fg = "white")
            success.pack(anchor = CENTER)
            
        c.pack_forget()
        p.pack_forget()
        o.pack_forget()
        cn = Label(add, text="Customer Name", font = "Arial 20 bold",bg = "#090c39", fg = "white")
        cn.pack(padx = 30, pady = 20)
        customer = OptionMenu(add, cust, *customers)
        customer.config(font=("Arial", 22))
        customer.pack(padx = 0, pady= 0)
        pd = Label(add, text="Product Name", font = "Arial 20 bold",bg = "#090c39", fg = "white")
        pd.pack(padx = 30, pady = 20)
        product = OptionMenu(add, prod, *products)
        product.config(font=("Arial", 22))
        product.pack(padx = 0,pady= 0)
        q = Label(add, text="Quantity", font = "Arial 20 bold",bg = "#090c39", fg = "white")
        q.pack(padx = 30, pady = 20)
        qt = Entry(add, font = "Arial 20 bold")
        qt.pack(padx = 30, pady = 20)
        dt = Label(add, text="Date", font = "Arial 20 bold",bg = "#090c39", fg = "white")
        dt.pack(padx = 30, pady = 20)
        date = Entry(add, font = "Arial 20 bold")
        date.pack(padx = 0,pady= 0)
        sub = Button(add, text = "Submit", font = "Arial 20 bold", bg = "blue", fg = "white", command = submit_data)
        sub.pack(pady=5)
        
    img = Image.open("images/add.jpg")
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=-2, y=-2)

    def quit():
        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
        if result == True:
            add.destroy()
    Label(add, text="Add/Insert Data", font = "Arial 40 bold",bg = "#090c39", fg = "white").pack(pady = 50)
    c = Button(add, text = "New Customer", font = "Arial 20 bold", bg = "white", command = new_cust)
    c.pack(pady=40)
    p = Button(add, text = "New Product", font = "Arial 20 bold", bg = "white", command = new_prod)
    p.pack(pady=40)
    o = Button(add, text = "New Order", font = "Arial 20 bold", bg = "white", command = new_order)
    o.pack(pady=1)
    Button(add, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = RIGHT,anchor = "se")
    Button(add, text = 'Home', font = 'Arial 20 bold', bg='red', command=switchh).pack(side = LEFT,anchor = "sw")
    Button(add, text = "Back", font = "Arial 20 bold", bg = "red", command = ad).pack(side = LEFT,anchor = "sw")
    add.mainloop()
    
def welcome_window():
    welcome = Tk()
    screen_width = welcome.winfo_screenwidth()
    screen_height = welcome.winfo_screenheight()
    welcome.title("Welcome to DataSense")
    welcome.attributes("-fullscreen", True)

    img = Image.open("images/welcome.jpg")
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=-2, y=-2)

    gr = Image.open("images/fig1.png")
    grimg = gr.resize((int(screen_width/3),int(screen_height/3)), Image.LANCZOS)
    gtest = ImageTk.PhotoImage(grimg)
    bkgr = Label(image=gtest)
    bkgr.image = gtest
    bkgr.place(x=(int(screen_width/2) - int(screen_width/6)), y=420)
    
    def switchl():
        welcome.destroy()
        login_window()
    
    def switchs():
        welcome.destroy()
        signup_window()
    
    def quit():
        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
        if result == True:
            welcome.destroy()
    Label(welcome, text = "Welcome to DataSense", font = "Arial 40 bold",bg = "#0d1133", fg = "white").pack(pady = 10)
    t = Text(welcome, width = 75, height = 7, font = ("Ink Free", 26), bg = "#0d1133", fg = "white")
    t.pack()
    t.insert(INSERT, "Our Data Analysis App is a powerful tool designed to simplify and \
enhance your data-driven decision-making. With our intuitive user interface,\
you can effortlessly plot graphs and perform complex numeric analyses, \
unlocking valuable insights from your data. Whether you're a data enthusiast,\
business professional, or a researcher, our app provides a user-friendly platform\
to visualize and understand your data like never before.\n\
Start your journey towards data-driven excellence with our Data Analysis App.\n\
Create and Account today! Already have it? Then Happy Analysis!!")
    Button(welcome, text = "Create Account", font = "Arial 30 bold", command=switchs).pack(side = LEFT, anchor = "sw")
    Label(welcome, text = "OR", font = ("MV Boli", 30)).pack(pady = 10, side = LEFT, anchor = "sw")
    Button(welcome, text = "Login", font = "Arial 30 bold", command=switchl).pack(side = LEFT, anchor = "sw")
    Button(welcome, text = "Exit", font = "Arial 30 bold", bg = "red", fg = "black", command=quit).pack(side = RIGHT, anchor = "se")
    
def numeric_window():
    numeric = Tk()
    global ct
    screen_width = numeric.winfo_screenwidth()
    screen_height = numeric.winfo_screenheight()
    x = (screen_width) // 2
    y = (screen_height) // 2

    numeric.title("Numeric Analysis")
    numeric.attributes("-fullscreen",True)
    numeric.overrideredirect(True)

    def quit():
        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
        if result == True:
            numeric.destroy()

    def display(text):
        disp.insert(INSERT, text)
        disp.insert(INSERT, "\n")
        
    def switchh():
        numeric.destroy()
        home_window()

    def prod_cats():
        product_categories = get_product_categories()
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print("\nProduct Categories:")
        display("\nProduct Categories:")
        for category in product_categories:
            print(category[0])
            display(category[0])

    def custordet():
        custid = simpledialog.askstring(title="Enter Values",prompt="Customer ID")
        customer_orders = get_customer_orders(custid)
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print("\nCustomer Orders:")
        display("\nCustomer Orders:")
        for order in customer_orders:
            print(f"OrderID: {order[0]}, Date: {order[1]}, Total Amount: {order[2]}")
            display(f"OrderID: {order[0]}, Date: {order[1]}, Total Amount: {order[2]}")

    def highpprod():
        min_price = simpledialog.askstring(title="Enter Values",prompt="Minimun Price")
        high_priced_products = get_high_priced_products(min_price)
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print(f"\nProducts with a price greater than or equal to {min_price}:")
        display(f"\nProducts with a price greater than or equal to {min_price}:")
        for product in high_priced_products:
            print(f"Product Name: {product[0]}, Price: {product[1]}")
            display(f"Product Name: {product[0]}, Price: {product[1]}")

    def custorcnt():
        customer_order_counts = get_order_count_by_customer()
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print("\nOrder Counts by Customer:")
        display("\nOrder Counts by Customer:")
        for customer in customer_order_counts:
            print(f"Customer: {customer[0]}, Order Count: {customer[1]}")
            display(f"Customer: {customer[0]}, Order Count: {customer[1]}")
                    
    def ordrng():
        start_date = simpledialog.askstring(title="Enter Values",prompt="Start Date (YYYY-MM-DD)")
        end_date = simpledialog.askstring(title="Enter Values",prompt="End Date (YYYY-MM-DD)")
        orders_in_date_range = get_orders_in_date_range(start_date, end_date)
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print("\nOrders in Date Range:")
        display("\nOrders in Date Range:")
        for order in orders_in_date_range:
            print(f"OrderID: {order[0]}, Date: {order[1]}, Total Amount: {order[2]}")
            display(f"OrderID: {order[0]}, Date: {order[1]}, Total Amount: {order[2]}")

    def revcat():
        total_revenue_by_category = get_total_revenue_by_category()
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print("\nTotal Revenue by Category:")
        display("\nTotal Revenue by Category:")
        for category, total_revenue in total_revenue_by_category:
            print(f"{category}: {total_revenue}")
            display(f"{category}: {total_revenue}")

    def custs():
        custid = simpledialog.askstring(title="Enter Values",prompt="Customer ID")
        customer_details = get_customer_details(custid)
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print("\nCustomer Details:")
        display("\nCustomer Details:")
        for idn, fname, lname, eml, addr in customer_details:
            print(f"Name: {fname} {lname}\nEmail: {eml}\nAddress: {addr}\n")
            display(f"Name: {fname} {lname}\nEmail: {eml}\nAddress: {addr}\n")
            
    def custtspent():
        customer_total_spent = get_customer_total_spent()
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print("\nCustomer Total Spent:")
        display("\nCustomer Total Spent:")
        for customer, total_spent in customer_total_spent:
            print(f"Customer: {customer}, \nTotal Spent: {total_spent}\n")
            display(f"Customer: {customer}, \nTotal Spent: {total_spent}\n")

    def avgpricat():
        avg_product_price_by_category = get_average_product_price_by_category()
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print("\nAverage Product Price by Category:")
        display("\nAverage Product Price by Category:")
        for category, avg_price in avg_product_price_by_category:
            print(f"{category}: {avg_price}")
            display(f"{category}: {avg_price}")

    def ordet():
        order_id = simpledialog.askstring(title="Enter Values",prompt="Order ID")
        order_details = get_order_details(order_id)
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print("\nOrder Details:")
        display("\nOrder Details:")
        for detail in order_details:
            print(f"ProductID: {detail[0]}, \nProductName: {detail[1]}, \nQuantity: {detail[2]}, \nSubtotal: {detail[3]}")
            display(f"ProductID: {detail[0]}, \nProductName: {detail[1]}, \nQuantity: {detail[2]}, \nSubtotal: {detail[3]}")

    def cat_prods_cat():
        category = simpledialog.askstring(title="Enter Values",prompt="Category")
        products_in_category = get_products_in_category_cat(category)
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print(f"\nProducts in Category '{category}':")
        display(f"\nProducts in Category '{category}':")
        for product in products_in_category:
            print(f"Product Name: {product[0]}, Price: {product[1]}")
            display(f"Product Name: {product[0]}, Price: {product[1]}")

    def cat_prods():
        products_in_category = get_products_in_category()
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print(f"\nProducts:")
        display(f"\nProducts:")
        for product in products_in_category:
            print(f"{product[0]}, Price: {product[1]}")
            display(f"{product[0]}, Price: {product[1]}")

    def hspentcust():
        top_customers = get_customers_with_highest_spending()
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print("\nTop Customers by Spending:")
        display("\nTop Customers by Spending:")
        for customer in top_customers:
            print(f"Customer: {customer[0]}, Total Spent: {customer[1]}")
            display(f"Customer: {customer[0]}, Total Spent: {customer[1]}")

    def dtcatord():
        date = simpledialog.askstring(title="Enter Values",prompt="Date")
        category = simpledialog.askstring(title="Enter Values",prompt="Category")
        orders_by_date_category = get_orders_by_date_and_category(date, category)
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print(f"\nOrders on '{date}' in Category '{category}':")
        display(f"\nOrders on '{date}' in Category '{category}':")
        for order in orders_by_date_category:
            print(f"Product Name: {order[0]}, \nOrder Date: {order[1]}, \nQuantity: {order[2]}, \nSubtotal: {order[3]}")
            display(f"Product Name: {order[0]}, \nOrder Date: {order[1]}, \nQuantity: {order[2]}, \nSubtotal: {order[3]}")

    def dtord():
        date = simpledialog.askstring(title="Enter Values",prompt="Date")
        orders_by_date = get_orders_by_date(date)
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print(f"\nOrders on '{date}':")
        display(f"\nOrders on '{date}':")
        for order in orders_by_date:
            print(f"Product Name: {order[0]}, \nOrder Date: {order[1]}, \nQuantity: {order[2]}, \nSubtotal: {order[3]}")
            display(f"Product Name: {order[0]}, \nOrder Date: {order[1]}, \nQuantity: {order[2]}, \nSubtotal: {order[3]}")
            
    def treveprod():
        total_revenue_by_product = get_total_revenue_by_product()
        log("Analytical Data Extracted")
        disp.delete("1.0", "end")
        print("\nTotal Revenue by Product:")
        display("\nTotal Revenue by Product:")
        for product, total_revenue in total_revenue_by_product:
            print(f"Product Name: {product}, Total Revenue: {total_revenue}")
            display(f"Product Name: {product}, Total Revenue: {total_revenue}")
    
    img = Image.open("images/numeric.jpg")
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=-2, y=-2)

    

    Label(numeric, text='Numeric Analysis', font='Arial 35 bold', bg='#7676EE').pack(pady = 20)

    bts = ["Customer Details", "Customer Total Spent", "Customer Highest Spent", "Order Details", "Orders by Date", "Orders between Dates", "Orders by Date and Category",
           "Customer Orders", "Customer Orders Count", "Products", "Categories", "Products in a Category",
           "Revenue by Product", "High Priced Product", "Average Product Price", "Revenue by Category"]
    
    coms = [custs, custtspent, hspentcust, ordet, dtord, ordrng, dtcatord, custordet, custorcnt, cat_prods, prod_cats, cat_prods_cat, treveprod,
            highpprod, avgpricat, revcat]
    buttons = [Button(numeric, text=text, command=func) for text, func in zip(bts, coms)]
    for button in buttons:
        button.pack()
    Button(numeric, text='Exit', font='Arial 20 bold', bg='red', command=quit).pack(side = RIGHT, anchor = "se")
    Button(numeric, text='Home', font='Arial 20 bold', bg='red', command=switchh).pack(side = LEFT, anchor = "sw")
    disp = Text(numeric, width = 50, height = 11, font = ("Ink Free", 20), bg = "black", fg = "white")
    disp.pack(side = BOTTOM, anchor= "s",pady = 30)
    
    numeric.mainloop()
    
def plot(xvals=None, yvals=None, t=""):
    if xvals is not None and yvals is not None:
        x = xvals
        y = yvals
    else:
        x = []
        y = []

        g = gra.get()
        t = typ.get()

        if g == "total_sales_cat":
            d = total_sales_cat()
        elif g == "total_sales_date":
            d = total_sales_date()
        elif g == "percent_total_sales_cat":
            d = percent_total_sales_cat()
        elif g == "prod_qty":
            d = prod_qty()

        for i in d:
            x.append(i[0])
            y.append(float(i[1]))

    if t == "horizontal bar graph":
        bar_chart(x, y, "X-Axis", "Y-Axis", "Visual Analysis\nHorizontal Chart", "horizontal")
    elif t == "vertical bar graph":
        bar_chart(x, y, "X-Axis", "Y-Axis", "Visual Analysis\nVertical Chart", "vertical")
    elif t == "pie chart":
        pie_chart(x, y, "Visual Analysis\nPie Chart")

#Function to create a Visual Analysis Page
def graph_window():
    global gra
    global typ
    
    tps = ["horizontal bar graph", "vertical bar graph", "pie chart"]   
        
    graph = Tk()
        
    screen_width = graph.winfo_screenwidth()
    screen_height = graph.winfo_screenheight()
##    x = (screen_width - 1280) // 2
##    y = (screen_height - 720) // 2
    graph.title("Visual Analysis")
    graph.attributes("-fullscreen",True)
    graph.overrideredirect(True)
    
    img = Image.open("images/visual.jpg")
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=-2, y=-2)
    
    def switch():
        graph.destroy()
        home_window()
    
    def quit():
        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
        if result == True:
            graph.destroy()

    gra = StringVar()
    gra.set("total_sales_cat")
    typ = StringVar()
    typ.set("horizontal bar graph")
    
    graph.title("Visual Analysis")
    title = Label(graph, text= 'Visual Analysis', font= 'Arial 35 bold',bg='#7676EE').pack(pady = 10)
    Radiobutton(graph, text = "Total Sales by Category", font = "Arial 25 bold", value = "total_sales_cat").pack()    
    Radiobutton(graph, text = "Percentage of Total Sales", font = "Arial 25 bold", value = "percent_total_sales_cat").pack()    
    Radiobutton(graph, text = "Total Sales by Date", font = "Arial 25 bold", value = "total_sales_date").pack()    
    Radiobutton(graph, text = "Sales by Product", font = "Arial 25 bold", value = "prod_qty").pack()    
    t = Label(graph, text="Type of Graph", font= "Arial 30", fg = "black").pack()
    tinp = OptionMenu(graph, typ, *tps).pack(expand = True)
    Button(graph, text= "Plot", font = "Arial 20 bold", bg="skyblue", command=plot).pack()
    Button(graph, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = RIGHT,anchor = "se")    
    Button(graph, text = 'Home', font = 'Arial 20 bold', bg='red', command=switch).pack(side = LEFT,anchor = "sw")    
    graph.mainloop()

def export_window():
    export  = Tk()
    screen_width = export.winfo_screenwidth()
    screen_height = export.winfo_screenheight()
##    x = (screen_width - 1280) // 2
##    y = (screen_height - 720) // 2
    tabs = []
    for i in execute_query("show tables"):
        tabs.append(i[0])
    export.attributes("-fullscreen",True)
    export.overrideredirect(True)
    export.title("Data Export")
    
    img = Image.open("images/export.jpg")
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=-2, y=-2)
    
    title = Label(export, text= 'Data Export', font= 'Arial 35 bold',bg='#7676EE').pack(pady = 10)
    
    def quit():
        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
        if result == True:
            export.destroy()
            
    def switch():
        export.destroy()
        home_window()

    
    def switchh():
        export.destroy()
        export_window()

    csvexp = Button(export, text = "Export as CSV", font = "Arial 20 bold", bg = "skyblue",
                    command = lambda : save_csv(simpledialog.askstring(title="Enter Values",prompt="Table Name")))
    csvexp.pack(pady = 10)
    excelexp = Button(export, text = "Export as Spreadsheet", font = "Arial 20 bold", bg = "skyblue",
                      command = lambda : save_excel(simpledialog.askstring(title="Enter Values",prompt="Table Name")))
    excelexp.pack(pady = 10)
    custc = Button(export, text = "Custom Query (CSV)", font = "Arial 20 bold", bg = "skyblue",
                   command = lambda : custom_query_save_csv(simpledialog.askstring(title="Enter Values",prompt="Enter Your Query")))
    custc.pack(pady = 10)
    custe = Button(export, text = "Custom Query (Spreadsheet)", font = "Arial 20 bold", bg = "skyblue",
                   command = lambda : custom_query_save_excel(simpledialog.askstring(title="Enter Values",prompt="Enter Your Query")))
    custe.pack(pady = 10)
                      
    Button(export, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = RIGHT,anchor = "se")    
    Button(export, text = 'Home', font = 'Arial 20 bold', bg='red', command=switch).pack(side = LEFT,anchor = "sw")
    Button(export, text = "Refresh", font = "Arial 20 bold", bg = "red", command = switchh).pack(side = LEFT, anchor = "sw")

def about_window():
    about = Tk()
    about.attributes('-fullscreen', True)
    about.overrideredirect(True)

    frame = Frame(about)
    frame.pack(padx=40, pady=40, fill=BOTH, expand=True)

    monospaced_font = ("Courier", 20)

    about_text = Text(frame, wrap=WORD, font=monospaced_font)
    about_text.pack(fill=BOTH, expand=True)

    about_content = """
    About DataSense

    DataSense is a project I developed as part of my class XII coursework.
    It's a Python application designed to help with data analysis, database management,
    and data security.

    Key Features

    - Data Analysis: This feature allows you to analyze data and create simple visualizations.
    - Database Management: You can interact with SQL databases, exporting and modifying data.
    - Security: I've included basic security measures to protect data using a custom library called SecuriPy.

    Developer

    I am the sole developer behind this project.

    Conclusion

    Thank you for taking the time to explore DataSense.
    I hope it reflects my dedication to learning and my passion for programming.
    """

    about_text.insert(END, about_content)

    def switchh():
        about.destroy()
        home_window()
        
    def quit():
        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
        if result == True:
            about.destroy()

    Button(about, text="Back", font="Arial 20 bold", bg="red", command=switchh).pack(side=LEFT, anchor="sw")
    Button(about, text="Exit", font="Arial 20 bold", bg="red", command=quit).pack(side=RIGHT, anchor="se")

    about.mainloop()
