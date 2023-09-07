##### ANNUAL PROJECT ON BUS REDERVATION SYSTEM   ########

####   BY AISHWARYA KUMAR SINGH     ######

           #GRADE-12TH "D"#
        #HOUSE NO.- "T-12008"#

#### MADE UNDER THE GUIDANCE OF MR. RAJESH NANDWAL ####
           ## H.O.D  COMPUTER SCIENCE ##


###########################################################################################################################


import tkinter as tk            ##
from PIL import Image,ImageTk    ###
from io import BytesIO           ###  LIBRARY USED..
import requests                 ##

def welcome():

    #Creation of Welcome Window
    welcome_window = tk.Tk()
    welcome_window.title("Welcome to Bus Reservation System")
    welcome_window.attributes('-fullscreen', True)
    welcome_window.geometry(f"{welcome_window.winfo_screenwidth()}x{welcome_window.winfo_screenheight()}")
    
    #Applying background Image
    response = requests.get("https://edunext-main-storage-cf.edunexttechnologies.com/dalycollege/school___static/1677579944412_final_logo.jpg")
    img = Image.open(BytesIO(response.content))
    img = img.resize((welcome_window.winfo_screenwidth(),welcome_window.winfo_screenheight()), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = tk.Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)

    
    #putting text in Welcom window
    welcome_label = tk.Label(welcome_window,bg="White", text="Welcome to Bus Reservation System!\n \n By-Aishwarya Kumar Singh\n \n XII-D\n \n Click on Start to Continue", font=("Arial", 20))
    welcome_label.pack(pady=0)
    
    def enter():
        welcome_window.destroy()    #defining function to switch windows
        home()
    def feedback():
        welcome_window.destroy()
        feedbackform()
    
    enter_button = tk.Button(welcome_window,font="arial 25",text="Start",fg="orange",padx=70,pady=16,bg="blue" ,command=enter)
##    enter_button.pack(pady=20)
    enter_button.place(relx=0.5,rely=0.95,anchor=tk.CENTER)
    

    feedback_button=tk.Button(welcome_window,text="Feedback Form",font="arial 20",bg="green",fg="red",padx=50,pady=15,command=feedback)
##    feedback_button.pack(pady=25)
    feedback_button.place(relx=0.3,rely=0.95,anchor=tk.CENTER)


    exit_button=tk.Button(welcome_window,text="EXIT",font="arial 20",bg="red",padx=90,pady=16,command=welcome_window.destroy)
##    exit_button.pack(padx=50,pady
    exit_button.place(relx=0.69,rely=0.95,anchor=tk.CENTER)
    welcome_window.mainloop()

def feedbackform():
        feed = tk.Tk()
        feed.title("Feedback Form")
        feed.attributes('-fullscreen', True)
        feed.geometry(f"{feed.winfo_screenwidth()}x{feed.winfo_screenheight()}")
        
        feedback_title = tk.Label(feed, text="We'd love to hear your feedback!",bg="#F8F8E5")
        feedback_title.pack(pady=10)

        img = Image.open("home_new.png")
##        img = img.resize((1350,800), Image.LANCZOS)
        img = img.resize((feed.winfo_screenwidth(),feed.winfo_screenheight()), Image.LANCZOS)

        test = ImageTk.PhotoImage(img)
        bk = tk.Label(image=test)
        bk.image = test
        bk.place(x=0, y=0)

        # Bus rating
        bus_rating_label = tk.Label(feed, text="Bus Rating (1-5):")
        bus_rating_label.pack()
        feed.busrating_entry = tk.Entry(feed)
        feed.busrating_entry.pack(pady=5)

        # Driver rating
        driver_rating_label = tk.Label(feed, text="Driver Rating (1-5):")
        driver_rating_label.pack()
        feed.driver_rating_entry = tk.Entry(feed)
        feed.driver_rating_entry.pack(pady=5)

        # Overall rating
        overall_rating_label = tk.Label(feed, text="Overall Rating (1-5):")
        overall_rating_label.pack()
        feed.overall_rating_entry = tk.Entry(feed)
        feed.overall_rating_entry.pack(pady=5)

        # Feedback comments
        feedback_comments_label = tk.Label(feed, text="Comments:")
        feedback_comments_label.pack()
        feed.feedback_comments_entry = tk.Text(feed, width=50, height=5)
        feed.feedback_comments_entry.pack(pady=5)
        def feedb():
            feed.destroy()
            feedsuccusful()


        def back():
            feed.destroy()
            welcome()
            
        back_button=tk.Button (feed,text= "Back",bg= "blue" ,fg="orange",padx=70,pady=10,command=back)
        back_button.place(relx=0.5,rely=0.6,anchor=tk.CENTER)
        
        submit_button = tk.Button(feed, text="Submit Feedback", command=feedb)
        submit_button.pack(pady=10)

def feedsuccusful():
    feeds = tk.Tk()
    feeds.geometry(f"{feeds.winfo_screenwidth()}x{feeds.winfo_screenheight()}")
    feeds.config(bg="white")
    feeds.title("AK TRAVEL AGENCY ")
    feeds.attributes('-fullscreen', True)
    
##    response = requests.get("https://www.dalycollege.org/images/slider-1.jpg")
    img = Image.open("home_new.png")
    img = img.resize((feeds.winfo_screenwidth(),feeds.winfo_screenheight()), Image.LANCZOS)
##    img = img.resize((1350,800), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = tk.Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)
    
    feed_label= tk.Label(feeds,bg="#F8F8E5", text="Thank You For Giving Your Valuable FeedBack ", font=("Arial", 30))
    feed_label.pack(pady=10)
    def back():
            feeds.destroy()
            welcome()
            
    back_button=tk.Button (feeds,text= "Back",bg= "#F8F8E5" ,fg="orange",padx=70,pady=10,command=back)
    back_button.place(relx=0.5,rely=0.17,anchor=tk.CENTER)

    
##    exit_button=tk.Button(feeds,text="EXIT",bg="red",padx=60,pady=20,command=feeds.destroy)
##    exit_button.pack(pady=50)
    

def home():
    
    
    #Creating New Window For inputting Ticket Details
    home = tk.Tk()
    home.geometry(f"{home.winfo_screenwidth()}x{home.winfo_screenheight()}")
    home.config(bg="white")
    home.title("AK TRAVEL AGENCY ")
    home.attributes('-fullscreen', True)
    
##    response = requests.get("https://www.dalycollege.org/images/slider-1.jpg")
    img = Image.open("home_new.png")
    img = img.resize((home.winfo_screenwidth(),home.winfo_screenheight()), Image.LANCZOS)
##    img = img.resize((1350,800), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = tk.Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)
    
##    label=tk.Label(home , text="WELCOME TO AK AGENCY",bg="red",font=("Arial",18))
##    label.grid(row=0,column=7)
    
    global name
    global age
    global gender
    global frm
    global to
    global date
    global month
    global year
    global company
    global mobile
    global email
    global seat
    
    name=tk.StringVar()
    age=tk.StringVar()
    gender=tk.StringVar()
    frm=tk.StringVar()
    to=tk.StringVar()
    date=tk.StringVar()
    month=tk.StringVar()
    year=tk.StringVar()
    company=tk.StringVar()
    mobile=tk.StringVar()
    email=tk.StringVar()
    seat=tk.StringVar()

    
    
    def switch():
        home.destroy()
        payment()


    name_label = tk.Label(home, text="Name",bg="#F8F8E5",font="arial 17")
    name_label.place(relx=0.4,rely=0.05,anchor=tk.CENTER)
    name_entry = tk.Entry(home,textvariable=name)
    name_entry.place(relx=0.5,rely=0.05,anchor=tk.CENTER)

    age_label = tk.Label(home, text="Age",bg="#F8F8E5",font="Arial 17")
    age_label.place(relx=0.4,rely=0.10,anchor=tk.CENTER)
    age_entry = tk.Entry(home,textvariable=age)
    age_entry.place(relx=0.5,rely=0.10,anchor=tk.CENTER)

    gender_label = tk.Label(home, text="Gender",bg="#F8F8E5",font="Arial 17")
    gender_label.place(relx=0.4,rely=0.15,anchor=tk.CENTER)
    
    male_radio = tk.Radiobutton(home, text="Male",bg="#F8F8E5", variable=gender, value="Male")
    male_radio.place(relx=0.5,rely=0.15,anchor=tk.CENTER)
    female_radio = tk.Radiobutton(home, text="Female",bg="#F8F8E5", variable=gender, value="Female")
    female_radio.place(relx=0.6,rely=0.15,anchor=tk.CENTER)

    frm_label = tk.Label(home, text="Boarding City",bg="#F8F8E5",font="Arial 17")
    
    frm_label.place(relx=0.4,rely=0.19,anchor=tk.CENTER)    

    From_dropdown = tk.OptionMenu(home, frm ,"DELHI","MUMBAI","JAIPUR","NAGPUR","AGRA","INDORE")
    frm.set("Select A Boarding City")
    From_dropdown.place(relx=0.5,rely=0.19,anchor=tk.CENTER)    

    to_label = tk.Label(home, text="Destination",bg="#F8F8E5",font="arial 17")
    to_label.place(relx=0.4,rely=0.23,anchor=tk.CENTER)

    to_dropdown = tk.OptionMenu(home, to ,"DELHI","MUMBAI","JAIPUR","NAGPUR","AGRA","INDORE")
    to.set("Select Your Destination")
    to_dropdown.place(relx=0.5,rely=0.23,anchor=tk.CENTER)

    date_label = tk.Label(home, text="Date",bg="#F8F8E5",font="Arial 17")
    date_label.place(relx=0.2,rely=0.28,anchor=tk.CENTER)
    date_dropdown = tk.OptionMenu(home,date,"1","4","5","8","15","16","18","22","25","29","30")
    date.set("Select Date")
    date_dropdown.place(relx=0.3,rely=0.28,anchor=tk.CENTER)


    month_label = tk.Label(home, text="Month",bg="#F8F8E5",font="Arial 17")
    month_label.place(relx=0.4,rely=0.28,anchor=tk.CENTER)
    month_dropdown = tk.OptionMenu(home,month,"January","February","March","April","May","June","July","August","September","October","November","December")
    month.set("Select Month")
    month_dropdown.place(relx=0.5,rely=0.28,anchor=tk.CENTER)
    

    year_label = tk.Label(home, text="Year",bg="#F8F8E5",font="Arial 17")
    year_label.place(relx=0.6,rely=0.28,anchor=tk.CENTER)
    year_dropdown = tk.OptionMenu(home,year,"2023")
    year.set("Select Year")
    year_dropdown.place(relx=0.7,rely=0.28,anchor=tk.CENTER)
    

    company_label = tk.Label(home, text="Travel Company",bg="#F8F8E5",font="Arial 17")
    company_label.place(relx=0.4,rely=0.32,anchor=tk.CENTER)
    
    company_dropdown = tk.OptionMenu(home, company, "Hans Travels", "Sharma Travels", "Verma Travels", "Chartered", "Patel Tours and Travels")
    company_dropdown.place(relx=0.5,rely=0.32,anchor=tk.CENTER)

    mobile_label = tk.Label(home, text="Mobile Number",bg="#F8F8E5",font="Arial 17")
    mobile_label.place(relx=0.4,rely=0.36,anchor=tk.CENTER)
    mobile_entry = tk.Entry(home,textvariable=mobile)
    mobile_entry.place(relx=0.5,rely=0.36,anchor=tk.CENTER)
    mobile.set("+91")

    email_label = tk.Label(home, text="Email",bg="#F8F8E5",font="Arial 17")
    email_label.place(relx=0.4,rely=0.40,anchor=tk.CENTER)
    email_entry = tk.Entry(home,bg="white",textvariable=email)
    email_entry.place(relx=0.5,rely=0.40,anchor=tk.CENTER)
    email.set("abc@dalycollege.org")

    seat_label = tk.Label(home, text="Seat Number",bg="#F8F8E5",font="Arial 17")
    seat_label.place(relx=0.4,rely=0.44,anchor=tk.CENTER)
    seat_entry = tk.Entry(home,textvariable=seat)
    seat_entry.place(relx=0.5,rely=0.44,anchor=tk.CENTER)
    info=tk.Label(home,text="*Please Fill your seat number in the Box*",font="Arial 20 bold", bg="#F8F8E5")
    info.place(relx=0.2,rely=0.8,anchor=tk.CENTER)
    
    seats = []
    for i in range(1, 49):
        seats.append(i)
    
    for row in range(12):
        for column in range(4):
            index = (row * 4) + column
            label = tk.Label(home, text=seats[index], width=4, height=2)
            label.grid(row=row, column=column, padx=5, pady=5)
    

   
    def back():
        home.destroy()
        welcome()
        

    
    exithome_button=tk.Button(home, text="EXIT",bg="red",font="arial 15",fg="orange",padx=70,pady=10,command=home.destroy)    
    exithome_button.place(relx=0.95,rely=0.03,anchor=tk.CENTER)
    
    back_button=tk.Button (home,text= "Back",bg= "blue" ,fg= "white",font="arial 15",padx=70,pady=10,command=back)
    back_button.place(relx=0.5,rely=0.6,anchor=tk.CENTER)
    
    change=tk.Button(home,text="SUBMIT",font="arial 15",bg="cyan",padx=70,pady=10,command=switch)
    change.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

    home.mainloop()

def payment():
    
    pay = tk.Tk()
    pay.title("Payment System")
    pay.config(bg="white")
    pay.geometry(f"{pay.winfo_screenwidth()}x{pay.winfo_screenheight()}")

##    response = requests.get("https://www.dalycollege.org/images/slider-1.jpg")
    img = Image.open("home_new.png")
    img = img.resize((pay.winfo_screenwidth(),pay.winfo_screenheight()), Image.LANCZOS)
##    img = img.resize((1350,800), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = tk.Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)

    
    amount_label = tk.Label(pay, text=f" Total Fare: 1000/- ",bg="#F8F8E5")
    amount_label.pack(pady=10)
    
    # Credit card number entry
    card_label = tk.Label( pay,text="Enter Credit Card Number:",font="arial 13",bg="#F8F8E5")
    card_label.pack()
    pay.card_entry = tk.Entry( pay,show="*")
    pay.card_entry.pack(pady=6)

    # Expiration date entry
    exp_label = tk.Label(pay, text=("Enter Expiration Date (MM/YY): "),font="arial 13",bg="#F8F8E5")
    exp_label.pack()
    pay.exp_entry = tk.Entry(pay)
    pay.exp_entry.pack(pady=6)

     # CVV number entry
    cvv_label = tk.Label(pay, text="Enter CVV Number:",font="arial 13",bg="#F8F8E5")
    cvv_label.pack()
    pay.cvv_entry = tk.Entry( pay,show="*")
    pay.cvv_entry.pack(pady=6)

    
    def back():
        pay.destroy()
        home()
        
    def con():
        pay.destroy()
        thankyou()
        
    back_button=tk.Button (pay,text= "Back",bg= "blue" ,fg="orange",font="arial 13",padx=70,pady=10,command=back)
    back_button.place(relx=0.5,rely=0.4,anchor=tk.CENTER)
    
    continue_button=tk.Button(pay, text="CONTINUE",bg="GREEN",font="arial 13",padx=70,pady=10,command=con)
    continue_button.pack(pady=6)
    
##    exitpay_button=tk.Button(pay, text="EXIT",bg="red",padx=70,pady=10,command=pay.destroy)
##    exitpay_button.pack(pady=8)   

  
    pay.mainloop()

    

#window for thanking customer For choosing us     

def thankyou():
    thx_window = tk.Tk()
    thx_window.title("Thank you")
    thx_window.config(bg="white")
    thx_window.attributes('-fullscreen', True)    
    thx_window.geometry(f"{thx_window.winfo_screenwidth()}x{thx_window.winfo_screenheight()}")

    
##    response = requests.get("https://www.dalycollege.org/images/slider-1.jpg")
    img = Image.open("home_new.png")
    img = img.resize((thx_window.winfo_screenwidth(),thx_window.winfo_screenheight()), Image.LANCZOS)
##    img = img.resize((1350,800), Image.LANCZOS)
    test = ImageTk.PhotoImage(img)
    bk = tk.Label(image=test)
    bk.image = test
    bk.place(x=0, y=0)
    Thx_label= tk.Label(thx_window, bg="#F8F8E5", text="PAYMENT SUCCESFULL \n\n\n THANK YOU FOR TRUSTING AK AGENCY\n\nYOUR TICKET WILL BE SEND ON YOUR\nENTERED MAIL AND PHONE NUMBER\n\n TOLL FREE NUMBER 1800 XXXXXX",font=("Arial", 20))
    Thx_label.pack(pady=10)
    def back():
        thx_window.destroy()
        welcome()

    back_button=tk.Button(thx_window,text= "Home",bg= "blue" ,fg="orange",font="arial 18",padx=70,pady=10,command=back)
    back_button.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
    
##    exitthx_button=tk.Button(thx_window, text="EXIT",bg="red",padx=70,pady=10,command=thx_window.destroy)
##    exitthx_button.pack(pady=15)


#Calling function to Start The programme   
welcome()    
