files = ["db_installer.py",
         "main.py",
         "sql_scripts.py",
         "visuals.py",
         "windows.py",
         "numeric_queries.py",
         "visual_queries.py",
         "uninstaller.py",
         "fonts.py"
]
sum = 0
for file in files:
    with open(file) as f:
        d = f.readlines()
        sum += len(d)

print(sum, " lines and coding")
