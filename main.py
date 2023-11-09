#DataBase Analyzer Launcher

import os

modules = [
    ("from PIL import Image, ImageTk, ImageDraw", "pip install pillow"),
    ("import matplotlib.pyplot as plt", "pip install matplotlib"),
    ("import SecuriPy", "pip install SecuriPy"),
    ("import pandas as pd","pip install pandas"),
    ("import mysql.connector as sqlcon", "pip install mysql-connector"),
    ("from datetime import datetime", "pip install datetime")
]

for module, code in modules:
    try:
        exec(module)
    except ImportError:
        exec(os.system(code))
try:
    from sql_scripts import *
    from visuals import *
    from windows import *
    welcome_window()
except FileNotFoundError:
    os.system("python installer.py")
    from sql_scripts import *
    from visuals import *
    from windows import *
    welcome_window()
    