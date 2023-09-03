import mysql.connector
import pandas as pd
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
            r = cursor.fetchall()
            query = f"SELECT * FROM {table}"
            data = pd.read_sql(query, conn)
            data.to_excel(f"{table}.xlsx", index=False)
        except UserWarning:
            pass

def close_connection():
    if conn is not None:
        conn.close()
        
# Execute a SQL query and return the result
def execute_query(query):
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            if query.strip().lower().startswith('insert'):
                conn.commit()  # For INSERT queries, commit the transaction
            else:
                r = cursor.fetchall()  # For other queries, fetch the results
                conn.commit()
                return r
        except mysql.connector.Error as err:
            print("Error:", err)
