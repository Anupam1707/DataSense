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
}
# Establish a connection to the MySQL server
def connect_to_database():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print("Error:", err)
        return None

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

def close_connection(conn):
    if conn is not None:
        conn.close()
# Execute a SQL query and return the result
def execute_query(*query):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("USE datasense")
            r = cursor.fetchall()
            conn.commit()
            cursor.execute(*query)
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
    SELECT Category, SUM(Price) TotalRevenue
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

##if __name__ == "__main__":
##    # Example queries
##    product_categories = get_product_categories()
##    print("Product Categories:")
##    for category in product_categories:
##        print(category[0])
##
##    customer_id = 1  # Replace with a valid customer ID
##    customer_orders = get_customer_orders(customer_id)
##    print("\nCustomer Orders:")
##    for order in customer_orders:
##        print(f"OrderID: {order[0]}, Date: {order[1]}, Total Amount: {order[2]}")
##
##    min_price = 100  # Replace with your desired minimum price
##    high_priced_products = get_high_priced_products(min_price)
##    print(f"\nProducts with a price greater than or equal to {min_price}:")
##    for product in high_priced_products:
##        print(f"Product Name: {product[0]}, Price: {product[1]}")
##
##    customer_order_counts = get_order_count_by_customer()
##    print("\nOrder Counts by Customer:")
##    for customer in customer_order_counts:
##        print(f"Customer: {customer[0]}, Order Count: {customer[1]}")
##
##    # Additional queries (1-4)
##    start_date = '2023-08-01'
##    end_date = '2023-08-05'
##    orders_in_date_range = get_orders_in_date_range(start_date, end_date)
##    print("\nOrders in Date Range:")
##    for order in orders_in_date_range:
##        print(f"OrderID: {order[0]}, Date: {order[1]}, Total Amount: {order[2]}")
##
##    total_revenue_by_category = get_total_revenue_by_category()
##    print("\nTotal Revenue by Category:")
##    for category, total_revenue in total_revenue_by_category:
##        print(f"{category}: {total_revenue}")
##
##    customer_total_spent = get_customer_total_spent()
##    print("\nCustomer Total Spent:")
##    for customer, total_spent in customer_total_spent:
##        print(f"Customer: {customer}, Total Spent: {total_spent}")
##
##    avg_product_price_by_category = get_average_product_price_by_category()
##    print("\nAverage Product Price by Category:")
##    for category, avg_price in avg_product_price_by_category:
##        print(f"{category}: {avg_price}")
##
##    # Additional queries (5-12)
##    order_id = 1  # Replace with a valid order ID
##    order_details = get_order_details(order_id)
##    print("\nOrder Details:")
##    for detail in order_details:
##        print(f"ProductID: {detail[0]}, ProductName: {detail[1]}, Quantity: {detail[2]}, Subtotal: {detail[3]}")
##
##    category = 'Electronics'  # Replace with a valid category
##    products_in_category = get_products_in_category(category)
##    print(f"\nProducts in Category '{category}':")
##    for product in products_in_category:
##        print(f"Product Name: {product[0]}, Price: {product[1]}")
##
##    top_customers = get_customers_with_highest_spending()
##    print("\nTop Customers by Spending:")
##    for customer in top_customers:
##        print(f"Customer: {customer[0]}, Total Spent: {customer[1]}")
##
##    date = '2023-08-01'  # Replace with a valid date
##    category = 'Electronics'  # Replace with a valid category
##    orders_by_date_category = get_orders_by_date_and_category(date, category)
##    print(f"\nOrders on '{date}' in Category '{category}':")
##    for order in orders_by_date_category:
##        print(f"Product Name: {order[0]}, Order Date: {order[1]}, Quantity: {order[2]}, Subtotal: {order[3]}")
##
##    total_revenue_by_product = get_total_revenue_by_product()
##    print("\nTotal Revenue by Product:")
##    for product, total_revenue in total_revenue_by_product:
##        print(f"Product Name: {product}, Total Revenue: {total_revenue}")
##
##button1 = tk.Button(window, text="Product Categories", command=lambda: execute_query_and_display(get_product_categories))
##button2 = tk.Button(window, text="Customer Orders", command=lambda: execute_query_and_display(lambda: get_customer_orders(1)))
##button3 = tk.Button(window, text="High Priced Products", command=lambda: execute_query_and_display(lambda: get_high_priced_products(100)))
##button4 = tk.Button(window, text="Order Count by Customer", command=lambda: execute_query_and_display(get_order_count_by_customer))
##
### Additional buttons (5-12)
##button5 = tk.Button(window, text="Orders in Date Range", command=lambda: execute_query_and_display(lambda: get_orders_in_date_range('2023-08-01', '2023-08-05')))
##button6 = tk.Button(window, text="Total Revenue by Category", command=lambda: execute_query_and_display(get_total_revenue_by_category))
##button7 = tk.Button(window, text="Customer Total Spent", command=lambda: execute_query_and_display(get_customer_total_spent))
##button8 = tk.Button(window, text="Avg Product Price by Category", command=lambda: execute_query_and_display(get_average_product_price_by_category))
##button9 = tk.Button(window, text="Order Details", command=lambda: execute_query_and_display(lambda: get_order_details(1)))
##button10 = tk.Button(window, text="Products in Category", command=lambda: execute_query_and_display(lambda: get_products_in_category('Electronics')))
##button11 = tk.Button(window, text="Top Customers", command=lambda: execute_query_and_display(get_customers_with_highest_spending))
##button12 = tk.Button(window, text="Orders by Date and Category", command=lambda: execute_query_and_display(lambda: get_orders_by_date_and_category('2023-08-01', 'Electronics')))
##button13 = tk.Button(window, text="Total Revenue by Product", command=lambda: execute_query_and_display(get_total_revenue_by_product))
