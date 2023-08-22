import requests
import os

url = "https://raw.githubusercontent.com/Anupam1707/datasense/main/"

urls = ["db.py",
        "visuals.py",
        "window.py",
        "numeric.py",
        "launch.py"]

sum = 0

d = []

for i in urls:
    d = (requests.get(url + i)).text
    with open("len.txt","w", newline = "", encoding = "utf-8") as f:
        f.write(d)
    with open("len.txt","r", encoding = "utf-8") as f:
        sum += len(f.readlines())

os.remove("len.txt")
print(f"{sum} lines and coding")
