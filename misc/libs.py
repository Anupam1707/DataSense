"""This cscript installs and imports all necesarry libraries"""
import os

modules = [
    ("import requests", "pip install requests"),
    ("from PIL import Image, ImageTk, ImageDraw", "pip install pillow"),
    ("import numpy as np", "pip install numpy"),
    ("import matplotlib.pyplot as plt", "pip install matplotlib"),
    ("import gspread", "pip install gspread"),
    ("from oauth2client.service_account import ServiceAccountCredentials", "pip install oath2client"),
    ("import SecuriPy", "pip install SecuriPy"),
    ("from fetchify import fetch", "pip install fetchify"),
    ("import pandas as pd","pip install pandas"),
    ("import mysql.connector as sqlcon", "pip install mysql-connector")
]

for module, code in modules:
    try:
        exec(module)
    except ImportError:
        exec(os.system(code))
 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import SecuriPy
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
from io import BytesIO
import SecuriPy
import requests
import matplotlib.pyplot as plt
import numpy
from fetchify import fetch
import pandas as pd
