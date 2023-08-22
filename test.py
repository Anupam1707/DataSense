import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database credentials
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
    'database': 'DataSense'  # Replace with your database name
}

# Establish a connection to the MySQL server
def connect_to_database():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print("Error:", err)
        return None

# Close the database connection
def close_connection(conn):
    if conn is not None:
        conn.close()

# Execute a SQL query and return the result
def execute_query(query):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            close_connection(conn)
            return result
        except mysql.connector.Error as err:
            print("Error:", err)
            close_connection(conn)
            return None

# Simple analytical queries
def get_product_categories():
    query = """
    SELECT DISTINCT Category
    FROM Products
    """
    return execute_query(query)

def get_customer_orders(customer_id):
    query = f"""
    SELECT OrderID, OrderDate, TotalAmount
    FROM Orders
    WHERE CustomerID = {customer_id}
    """
    return execute_query(query)

def get_high_priced_products(min_price):
    query = f"""
    SELECT ProductName, Price
    FROM Products
    WHERE Price >= {min_price}
    """
    return execute_query(query)

def get_order_count_by_customer():
    query = """
    SELECT CONCAT(FirstName, ' ', LastName) CustomerName, COUNT(Orders.OrderID) OrderCount
    FROM Customers
    LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    GROUP BY CustomerName
    """
    return execute_query(query)

# Four additional simple analytical queries
def get_orders_in_date_range(start_date, end_date):
    query = f"""
    SELECT OrderID, OrderDate, TotalAmount
    FROM Orders
    WHERE OrderDate BETWEEN '{start_date}' AND '{end_date}'
    """
    return execute_query(query)

def get_total_revenue_by_category():
    query = """
    SELECT Category, SUM(TotalAmount) TotalRevenue
    FROM Products
    JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
    GROUP BY Category
    """
    return execute_query(query)

def get_customer_total_spent():
    query = """
    SELECT CONCAT(FirstName, ' ', LastName) CustomerName, SUM(TotalAmount) TotalSpent
    FROM Customers
    JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    GROUP BY CustomerName
    """
    return execute_query(query)

def get_average_product_price_by_category():
    query = """
    SELECT Category, AVG(Price) AvgPrice
    FROM Products
    GROUP BY Category
    """
    return execute_query(query)

def get_order_details(order_id):
    query = f"""
    SELECT OrderDetails.ProductID, Products.ProductName, OrderDetails.Quantity, OrderDetails.Subtotal
    FROM OrderDetails
    JOIN Products ON OrderDetails.ProductID = Products.ProductID
    WHERE OrderDetails.OrderID = {order_id}
    """
    return execute_query(query)

def get_products_in_category(category):
    query = f"""
    SELECT ProductName, Price
    FROM Products
    WHERE Category = '{category}'
    """
    return execute_query(query)

def get_customers_with_highest_spending():
    query = """
    SELECT CONCAT(FirstName, ' ', LastName) CustomerName, SUM(TotalAmount) TotalSpent
    FROM Customers
    JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    GROUP BY CustomerName
    ORDER BY TotalSpent DESC
    LIMIT 5
    """
    return execute_query(query)

def get_orders_by_date_and_category(date, category):
    query = f"""
    SELECT Products.ProductName, Orders.OrderDate, OrderDetails.Quantity, OrderDetails.Subtotal
    FROM Orders
    JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
    JOIN Products ON OrderDetails.ProductID = Products.ProductID
    WHERE Orders.OrderDate = '{date}' AND Products.Category = '{category}'
    """
    return execute_query(query)

def get_total_revenue_by_product():
    query = """
    SELECT Products.ProductName, SUM(OrderDetails.Subtotal) TotalRevenue
    FROM Products
    JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
    GROUP BY Products.ProductName
    ORDER BY TotalRevenue DESC
    LIMIT 5
    """
    return execute_query(query)

# Function to execute the selected analytical query
def execute_query_and_display(query_function):
    try:
        # Execute the selected query function
        result = query_function()

        # Clear the result text widget
        result_text.delete("1.0", tk.END)

        # Display the result in the text widget
        for row in result:
            result_text.insert(tk.END, str(row) + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create a Tkinter window
window = tk.Tk()
window.title("Analytical Queries")

# Create buttons for each query function
button1 = tk.Button(window, text="Product Categories", command=lambda: execute_query_and_display(get_product_categories))
button2 = tk.Button(window, text="Customer Orders", command=lambda: execute_query_and_display(lambda: get_customer_orders(1)))
button3 = tk.Button(window, text="High Priced Products", command=lambda: execute_query_and_display(lambda: get_high_priced_products(100)))
button4 = tk.Button(window, text="Order Count by Customer", command=lambda: execute_query_and_display(get_order_count_by_customer))

# Additional buttons (5-12)
button5 = tk.Button(window, text="Orders in Date Range", command=lambda: execute_query_and_display(lambda: get_orders_in_date_range('2023-08-01', '2023-08-05')))
button6 = tk.Button(window, text="Total Revenue by Category", command=lambda: execute_query_and_display(get_total_revenue_by_category))
button7 = tk.Button(window, text="Customer Total Spent", command=lambda: execute_query_and_display(get_customer_total_spent))
button8 = tk.Button(window, text="Avg Product Price by Category", command=lambda: execute_query_and_display(get_average_product_price_by_category))
button9 = tk.Button(window, text="Order Details", command=lambda: execute_query_and_display(lambda: get_order_details(1)))
button10 = tk.Button(window, text="Products in Category", command=lambda: execute_query_and_display(lambda: get_products_in_category('Electronics')))
button11 = tk.Button(window, text="Top Customers", command=lambda: execute_query_and_display(get_customers_with_highest_spending))
button12 = tk.Button(window, text="Orders by Date and Category", command=lambda: execute_query_and_display(lambda: get_orders_by_date_and_category('2023-08-01', 'Electronics')))
button13 = tk.Button(window, text="Total Revenue by Product", command=lambda: execute_query_and_display(get_total_revenue_by_product))

# Create a text widget to display query results
result_text = tk.Text(window, height=10, width=40)

# Place buttons and result_text in the window
button1.pack()
button2.pack()
button3.pack()
button4.pack()

# Additional buttons (5-12)
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()
button11.pack()
button12.pack()
button13.pack()

result_text.pack()

# Start the Tkinter main loop
window.mainloop()
