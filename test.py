import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
def ordet():
        custid = simpledialog.askstring(title="Test",
                                  prompt="Customer ID")
##        customer_orders = get_customer_orders(custid.get())
        print("\nCustomer Orders:")
        print(custid)
##        for order in customer_orders:
##            print(f"OrderID: {order[0]}, Date: {order[1]}, Total Amount: {order[2]}")

