from sql_scripts import execute_query
import os
execute_query("drop database datasense")
os.remove("creds.tiak")
os.remove("log.tiak")
print("Uninstalled Successfully")
