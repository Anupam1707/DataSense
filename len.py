files = ["db_installer.py","main.py", "sql_scripts.py", "visuals.py", "windows.py", "analytical_queries.py"]
sum = 0
for file in files:
    with open(file) as f:
        d = f.readlines()
        sum += len(d)

print(sum, " lines and coding")
