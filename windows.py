"""This is the backbone of the App. This program creates a link between the front end and the back-end."""
import SecuriPy
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
from sql_scripts import *


#Function to give values of the input to the graph plotter to plot the graph
def pt():
    if l1v.get() != None and l2v.get() != None and typ.get() == "vertical bar graph":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]), t = "bv")
    if l1v.get() != None and l2v.get() != None and typ.get() == "horizontal bar graph":
        plotb(data(sales, col[l1v.get().lower()]), data(sales, col[l2v.get().lower()]), t = "bh")

#Function to create a Home Page
def home_window():
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
        login_window()
        
    Label(home, text = "Welcome to Data Sense", font = "Arial 40 bold", bg = "black", fg = "white").pack()
    Button(home, text = "Add Data", font = "Arial 20 bold", bg="white", command=switcha).pack(pady=20)
    Button(home, text = "Update Data", font = "Arial 20 bold", bg="white", command=switcha).pack(pady=20)
    Button(home, text = "Delete Data", font = "Arial 20 bold", bg="white", command=switcha).pack(pady=20)
    Button(home, text = 'Visual Analysis', font = 'Arial 20 bold', bg='white', command=switchg).pack(pady=20)
    Button(home, text = 'Numeric Analysis', font = 'Arial 20 bold', bg='white', command=switchn).pack(pady=20)
    Button(home, text = "Export Reports", font = "Arial 20 bold", bg = "white", command=switche).pack(pady=20)
    Button(home, text = "Help", font = "Arial 20 bold",bg = "white", command=switchn).pack(pady=20)
    Button(home, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = RIGHT,anchor = "se")
    Button(home, text = 'Log Out', font = 'Arial 20 bold', bg='red', command=logout).pack(side = LEFT,anchor = "sw")
    
    home.mainloop()

##def home_window():
##    add = Tk()
##    
##    screen_width = home.winfo_screenwidth()
##    screen_height = home.winfo_screenheight()
####    x = (screen_width - 1280) // 2
####    y = (screen_height - 720) // 2
##
##    home.title("Add/Insert Data")
##    home.attributes("-fullscreen",True)
##    home.overrideredirect(True)
##
##    img = Image.open("images/home.jpg")
##    img = img.resize((screen_width,screen_height), Image.LANCZOS)
##    test = ImageTk.PhotoImage(img)
##    bk = Label(image=test)
##    bk.image = test
##    bk.place(x = -2, y = -2)
##    
##    def quit():
##        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
##        if result == True:
##            home.destroy()
##            ()
##    
##    def switchg():
##        home.destroy()
##        graph_window()
##    def switchn():
##        home.destroy()
##        numeric_window()
##    def switche():
##        home.destroy()
##        export_window()
##    def switcha():
##        home.destroy()
##        add_window()
##    def switchu():
##        home.destroy()
##        update_window()
##    def switchdel():
##        home.destroy()
##        delete_window()
##    def logout():
##        home.destroy()
##        login_window()
##        
##    Label(home, text = "Welcome to Data Sense", font = "Arial 40 bold", bg = "black", fg = "white").pack()
##    Button(home, text = "Add Data", font = "Arial 20 bold", bg="white", command=switcha).pack(pady=20)
##    Button(home, text = "Update Data", font = "Arial 20 bold", bg="white", command=switcha).pack(pady=20)
##    Button(home, text = "Delete Data", font = "Arial 20 bold", bg="white", command=switcha).pack(pady=20)
##    Button(home, text = 'Visual Analysis', font = 'Arial 20 bold', bg='white', command=switchg).pack(pady=20)
##    Button(home, text = 'Numeric Analysis', font = 'Arial 20 bold', bg='white', command=switchn).pack(pady=20)
##    Button(home, text = "Export Reports", font = "Arial 20 bold", bg = "white", command=switche).pack(pady=20)
##    Button(home, text = "Help", font = "Arial 20 bold",bg = "white", command=switchn).pack(pady=20)
##    Button(home, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = RIGHT,anchor = "se")
##    Button(home, text = 'Log Out', font = 'Arial 20 bold', bg='red', command=logout).pack(side = LEFT,anchor = "sw")
##    
##    home.mainloop()
##    
#Function to create a Signup Page
def signup_window():
    signup = Tk()
    signup.title("Login")
    signup.attributes('-fullscreen', True)

    def switchlog():
        signup.destroy()
        login_window()
    
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
        q = f"insert into users (username, password) values ('{username_entry.get()}', '{password_entry.get()}')"
        r = execute_query(q)
        signup.destroy()
        home_window()
        
    button = Button(signup, text="SignUP", font = "Arial 30 bold", command=signup_button).pack(side = TOP)
    Button(signup, text = 'Exit', font = 'Arial 20 bold', bg='red', command=signup.destroy).pack(side = RIGHT,anchor = "se")
    Button(signup, text = 'Go Back', font = 'Arial 20 bold', bg='red', command=switchlog).pack(side = LEFT,anchor = "sw")
    signup.mainloop()
 
#Function to create a Login Page
def login_window():
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
            if username_entry.get() == response[i][0]:
                usr = i
                break
            else:
                usr = -1
        if password_entry.get() == response[usr][1]:
            user = username_entry.get()
            welcome = Label(login, text=f"Welcome back {username_entry.get()}", font="Arial 30", fg = "blue").pack()
            login.destroy() 
            home_window()
        else:
            error_label = Label(login, text="Incorrect username or password",font = "Arial 30", fg="red")
            error_label.pack()

    button = Button(login, text="Login", font = "Arial 30 bold", command=login_button).pack(side = TOP)
    Button(login, text = 'Exit', font = 'Arial 20 bold', bg='red', command=login.destroy).pack(side = BOTTOM,anchor = "se")
    sign = Button(login, text= "Sign UP Instead", font = "Arial 20 bold", bg="skyblue", command=switchs).pack(pady = 30)
    login.mainloop()

def numeric_window():
    numeric = Tk()
    global ct
    screen_width = numeric.winfo_screenwidth()
    screen_height = numeric.winfo_screenheight()
    #x = (screen_width - 1280) // 2
    #y = (screen_height - 720) // 2

    numeric.title("Numeric Analysis")
    numeric.attributes("-fullscreen",True)
    numeric.overrideredirect(True)

    def quit():
        result = messagebox.askyesno("Confirmation", "Are you sure you want to quit?")
        if result == True:
            numeric.destroy()
            
    
    def empty_home():
        tren.pack_forget()
        pop.pack_forget()
        most.pack_forget()

    def show_home():
        tren.pack(pady = 10)
        pop.pack(pady = 10)
        most.pack(pady = 10)
        
    def switchh():
        numeric.destroy()
        home_window()
    
    def trend_win():
            empty_home()

            def untrend():
                utrend()
                show_home()
                
            def utrend():
                l.pack_forget()
                c.pack_forget()
                r.pack_forget()
                b.pack_forget()

            def city():
                    utrend()

                    dt = {}
                    cityu = []
                    produ = []
                    mxp = ""
                    mx = 0
                    cities = data(sales, colno = col["city"])
                    products = data(sales, colno = col["product"])

                    for city in cities:
                        while city not in cityu:
                            cityu.append(city)
                    cityu.remove(cityu[-1])
                    cities = cityu
                    cityu = None

                    for product in products:
                        while product not in produ:
                            produ.append(product)
                    produ.remove(produ[-1])
                    products = produ
                    produ = None

                    ct = Frame(numeric, bg = "white")
                    wait = Label(ct, text = "Analyzing Data....\nWe appreciate your patience", font = "Arial 30 bold")
                    wait.pack(pady = 10)

                    for city in cities:
                        mx = 0
                        mxp = ""
                        dt = {}
                        dt[city] = []
                        
                        for product in products:
                            formula = f'=COUNTIFS(D2:D245, "{city}", F2:F245, "{product}")'
                            sales.update_cell(1, 10, formula)
                            result = int(sales.cell(1, 10).value)
                            dt[city].append([product, result])
                            print(city, product, type(result), result)
                        print(dt)
                        for value in dt[city]:
                            if value[1] >= mx:
                                    mx = value[1]
                                    mxp = value[0]
                        Label(numeric, text=f"Trending Product in {city} is {mxp}", font="Arial 30 bold").pack()
                            
                    back = Button(numeric, text = "Back", font = "Arial 20 bold", bg = "skyblue", command = trend_win)
                    back.pack(pady = 10)

            l = Label(numeric, text="Trending Product on Basis of :", font="Arial 30 bold")
            l.pack(pady=10)
            c = Button(numeric, text="City", font="Arial 20 bold", bg="skyblue", command=city)
            c.pack(pady=10)
            r = Button(numeric, text="Region", font="Arial 20 bold", bg="skyblue")
            r.pack(pady=10)
            b = Button(numeric, text="Back", font="Arial 20 bold", bg="skyblue", command=untrend)
            b.pack(pady=10)


    def most_sold_win():
            empty_home()

            def unmost():
                l.pack_forget()
                c.pack_forget()
                ct.pack_forget()
                r.pack_forget()
                b.pack_forget()
                show_home()
            
            l = Label(numeric, text="Most Sold Product on Basis of :", font="Arial 30 bold")
            l.pack(pady=10)
            c = Button(numeric, text="City", font="Arial 20 bold", bg="skyblue")
            c.pack(pady=10)
            r = Button(numeric, text="Region", font="Arial 20 bold", bg="skyblue")
            r.pack(pady=10)
            b = Button(numeric, text="Back", font="Arial 20 bold", bg="skyblue", command=unmost)
            b.pack(pady=10)
            
    def pop_win():
            empty_home()

            def unpop():
                l.pack_forget()
                c.pack_forget()
                ct.pack_forget()
                r.pack_forget()
                b.pack_forget()
                show_home()
                
            l = Label(numeric, text="Popular Product on Basis of :", font="Arial 30 bold")
            l.pack(pady=10)
            c = Button(numeric, text="City", font="Arial 20 bold", bg="skyblue")
            c.pack(pady=10)
            r = Button(numeric, text="Region", font="Arial 20 bold", bg="skyblue")
            r.pack(pady=10)
            b = Button(numeric, text="Back", font="Arial 20 bold", bg="skyblue", command=unpop)
            b.pack(pady=10)
            
    img = Image.open("images/numeric.jpg")
    img = img.resize((screen_width,screen_height), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = Label(image=test)
    bk.image = test
    bk.place(x=-2, y=-2)

    Label(numeric, text='Numeric Analysis', font='Arial 35 bold', bg='#7676EE').pack(pady = 20)
    tren = Button(numeric, text="Trending", font="Arial 20 bold", bg="skyblue", command=trend_win)
    tren.pack(pady = 10)
    pop  = Button(numeric, text="Popular", font="Arial 20 bold", bg="skyblue", command=pop_win)
    pop.pack(pady = 10)
    most  = Button(numeric, text="Most Sold", font="Arial 20 bold", bg="skyblue", command=most_sold_win)
    most.pack(pady = 10)
    Button(numeric, text='Exit', font='Arial 20 bold', bg='red', command=quit).pack(side = RIGHT, anchor = "se")
    Button(numeric, text='Home', font='Arial 20 bold', bg='red', command=switchh).pack(side = LEFT, anchor = "sw")
    
    numeric.mainloop()
    
#Function to create a Visual Analysis Page
def graph_window():
    global l1v
    global l2v
    global typ
    
    tps = ["horizontal bar graph", "vertical bar graph", "pie chart"]   
        
    graph = Tk()
    
    screen_width = graph.winfo_screenwidth()
    screen_height = graph.winfo_screenheight()
##    x = (screen_width - 1280) // 2
##    y = (screen_height - 720) // 2

    graph.title("Numeric Analysis")
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
            
      
    l1v = StringVar()
    l1v.set("product")
    l2v = StringVar()
    l2v.set("total price")
    typ = StringVar()
    typ.set("horizontal bar graph")
    
    graph.title("Visual Analysis")
    title = Label(graph, text= 'Visual Analysis', font= 'Arial 35 bold',bg='#7676EE').pack(pady = 10)
    l1 = Label(graph, text="Data List 1", font= "Arial 30", fg = "black").pack()
    l1inp = OptionMenu(graph, l1v, *col.keys()).pack(expand = True)
    l2 = Label(graph, text="Data List 2", font= "Arial 30", fg = "black").pack()
    l2inp = OptionMenu(graph, l2v, *col.keys()).pack(expand = True)
    l4 = Label(graph, text="Type of Graph", font= "Arial 30", fg = "black").pack()
    l4inp = OptionMenu(graph, typ, *tps).pack(expand = True)
    Button(graph, text= "Plot", font = "Arial 20 bold", bg="skyblue", command=pt).pack()
    Button(graph, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = RIGHT,anchor = "se")    
    Button(graph, text = 'Home', font = 'Arial 20 bold', bg='red', command=switch).pack(side = LEFT,anchor = "sw")    
    graph.mainloop()

def export_window():
    export  = Tk()
    rows = IntVar()
    rowe = IntVar()
    cols = IntVar()
    cole = IntVar()
    screen_width = export.winfo_screenwidth()
    screen_height = export.winfo_screenheight()
##    x = (screen_width - 1280) // 2
##    y = (screen_height - 720) // 2
##    
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

    def switchg():
        export.destroy()
        graph_window()
        
    def returnn():
        n.pack(pady = 10)
        v.pack(pady = 10)
    
    def num():
        n.pack_forget()
        v.pack_forget()

        def switchh():
            export.destroy()
            export_window()
            
        def concsv():
##           query = "select * from " + table
##           data = pd.read_sql(query
##           df.to_csv("NumericAnalysis_Row{rows}Column{cole}.csv", index=False)
            pass       
        def conexcel():
           dt = data(sales, alldata = True)
           selected_rows = dt[(rows.get()-1):rowe.get()]
           selected_columns = [row[(cols.get()-1):(cole.get()+1)] for row in selected_rows]
           df = pd.DataFrame(selected_columns)
           df.to_excel("NumericAnalysis_Row{rows}Column{cole}.xlsx", index=False)

        rsl = Label(export, text = "Starting Row", font = "Arial 20 bold", bg = "skyblue")
        rsl.pack(pady = 10)
        rs = Entry(export, textvariable = rows, font  = "Arial 20 bold")
        rs.pack(pady = 10)
        rel = Label(export, text = "Ending Row", font = "Arial 20 bold", bg = "skyblue")
        rel.pack(pady = 10)
        re = Entry(export, textvariable = rowe, font  = "Arial 20 bold")
        re.pack(pady = 10)
        
        csl = Label(export, text = "Starting Column", font = "Arial 20 bold", bg = "skyblue")
        csl.pack(pady = 10)
        cs = Entry(export, textvariable = cols, font  = "Arial 20 bold")
        cs.pack(pady = 10)
        cel = Label(export, text = "Ending Column", font = "Arial 20 bold", bg = "skyblue")
        cel.pack(pady = 10)
        ce = Entry(export, textvariable = cole, font  = "Arial 20 bold")
        ce.pack(pady = 10)
        
        csvexp = Button(export, text = "Export as CSV", font = "Arial 20 bold", bg = "skyblue", command = concsv())
        csvexp.pack(pady = 10)
        excelexp = Button(export, text = "Export as Spreadsheet", font = "Arial 20 bold", bg = "skyblue", command = conexcel())
        excelexp.pack(pady = 10)
        
    n = Button(export, text = "Numeric Export", font = "Arial 20 bold", bg = "skyblue", command=num)
    n.pack(pady = 10)
    v = Button(export, text = "Visual Export", font = "Arial 20 bold", bg = "skyblue", command=switchg)
    v.pack(pady = 10)
    Button(export, text = 'Exit', font = 'Arial 20 bold', bg='red', command=quit).pack(side = RIGHT,anchor = "se")    
    Button(export, text = 'Home', font = 'Arial 20 bold', bg='red', command=switch).pack(side = LEFT,anchor = "sw")
