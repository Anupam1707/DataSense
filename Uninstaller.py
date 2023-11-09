#Uninstaller
import os
import mysql.connector
from tkinter import messagebox

with open("creds.tiak") as f:
        creds = f.read()
        creds = creds.split(",")

user = creds[0]
password = creds[1]
host = creds[2]

db_config = {
        'user': user,
        'password': password,
        'host': host,
        'auth_plugin':'mysql_native_password'
}
conn = mysql.connector.connect(**db_config, database = "datasense")
cursor = conn.cursor() 
cursor.execute("drop database datasense")
os.remove("creds.tiak")
os.remove("log.tiak")
print("Uninstalled Successfully")
messagebox.showinfo("Information", "Uninstalled DataSense")
