import tkinter as tk
from tkcalendar import Calendar

def get_selected_date():
    selected_date = cal.get_date()
    popup.destroy()
    dt = selected_date.split("/")
    dt = dt[::-1]
    selected_date = "-".join(dt)
    return selected_date

def date_picker():
    global cal, popup
    popup = Toplevel(root)
    popup.title("Select Date")
    popup.geometry("300x300")
    cal = Calendar(popup, selectmode="day")
    cal.pack(pady=20)
    select_button = Button(popup, text="Select Date", command=get_selected_date)
    select_button.pack()

# Create the main application window
root = tk.Tk()
root.title("Date Picker")

date_button = tk.Button(root, text="Pick a Date", command=open_date_picker)
date_button.pack(pady=20)

root.mainloop()
