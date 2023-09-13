#DataBase Analyzer Launcher

import os

modules = [
    ("from PIL import Image, ImageTk, ImageDraw", "pip install pillow"),
    ("import numpy as np", "pip install numpy"),
    ("import matplotlib.pyplot as plt", "pip install matplotlib"),
    ("import SecuriPy", "pip install SecuriPy"),
    ("import pandas as pd","pip install pandas"),
    ("import mysql.connector as sqlcon", "pip install mysql-connector")
]

for module, code in modules:
    try:
        exec(module)
    except ImportError:
        exec(os.system(code))
from PIL import Image, ImageTk, ImageDraw
import matplotlib.pyplot as plt
import SecuriPy
import pandas as pd
import mysql.connector as sqlcon
from sql_scripts import *
from visuals import *
from windows import *
welcome_window()
