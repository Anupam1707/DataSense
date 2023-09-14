import mysql.connector
import pandas as pd
import datetime
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

def log(event):
    with open("log.tiak", "a") as l:
        l.write(str(event) + " " + str(datetime.datetime.now()))
        l.write("\n")

# Establish a connection to the MySQL server
def connect_to_database():
    try:
        conn = mysql.connector.connect(**db_config, database = "datasense")
        if conn is not None:
            return conn  # Return the connection without executing "USE datasense"
    except mysql.connector.Error as err:
        print("Error:", err)
    return None

conn = connect_to_database()

def save_excel(table):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("USE datasense")
            query = f"SELECT * FROM {table}"
            try:
                data = pd.read_sql(query, conn)
                data.to_excel(f"{table}.xlsx", index=False)
            except pd.errors.DatabaseError:
                print("Incorrect Query")
        except Warning:
            pass
        log("Data Exported")

def save_csv(table):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("USE datasense")
            query = f"SELECT * FROM {table}"
            try:
                data = pd.read_sql(query, conn)
                data.to_csv(f"{table}.csv", index=False)
            except pd.errors.DatabaseError:
                print("Incorrect Query")
        except Warning:
            pass
        log("Data Exported")

def custom_query_save_csv(query):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("USE datasense")
            try:
                data = pd.read_sql(query, conn)
                data.to_csv("Custom Table.csv", index=False)
            except pd.errors.DatabaseError:
                print("Incorrect Query")
        except Warning:
            pass
        log("Data Exported")

def custom_query_save_excel(query):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("USE datasense")
            try:
                data = pd.read_sql(query, conn)
                data.to_excel("Custom Table.xlsx", index=False)
            except pd.errors.DatabaseError:
                print("Incorrect Query")
        except Warning:
            pass
        log("Data Exported")
        
def close_connection():
    if conn is not None:
        conn.close()
        
# Execute a SQL query and return the result
def execute_query(query):
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            if query.strip().lower().startswith('select'):
                r = cursor.fetchall()
                conn.commit()
                log("Data Retrieved from the Database")
                return r
            else:
                conn.commit()  # For insert queries, commit the transaction
                log("Data Modified in the Database")
        except mysql.connector.Error as err:
            print("Error:", err)
