from fetchify import fetch
files = ["db.py","visuals.py", "numeric.py", "window.py"]

with open("main.py","w") as f:
    pass

for file in files:
    with open("main.py","a",encoding = "utf-8" ,newline = "") as main:
        main.write(fetch(file, "ds"))
        main.write("\n###############################################\n\n")
