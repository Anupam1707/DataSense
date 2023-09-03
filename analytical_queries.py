from sql_scripts import *
# Simple analytical queries
def get_product_categories():
        query = """select distinct(Category) from Products"""
        return execute_query(query)

def get_customer_orders(customer_id):
        query = """select OrderID, OrderDate, TotalAmount from Orders where CustomerID = {}""".format(customer_id)
        return execute_query(query)

def get_high_priced_products(min_price):
        query = """select ProductName, Price from Products where Price >= {}""".format(min_price)
        return execute_query(query)

def get_order_count_by_customer():
        query = """
        select concat(FirstName, ' ', LastName) CustomerName, count(Orders.OrderID) OrderCount
        from Customers
        left join Orders on Customers.CustomerID = Orders.CustomerID
        group by CustomerName
        """
        return execute_query(query)

    # Four additional simple analytical queries
def get_orders_in_date_range(start_date, end_date):
        query = """
        select OrderID, OrderDate, TotalAmount
        from Orders
        where OrderDate BETWEEN '{}' AND '{}'
        """.format(start_date, end_date)
        return execute_query(query)

def get_total_revenue_by_category():
        query = """
        select Category, sum(Price) TotalRevenue
        from Products
        join OrderDetails on Products.ProductID = OrderDetails.ProductID
        group by Category
        """
        return execute_query(query)

def get_customer_total_spent():
        query = """
        select concat(FirstName, ' ', LastName) CustomerName, sum(TotalAmount) TotalSpent
        from Customers
        join Orders on Customers.CustomerID = Orders.CustomerID
        group by CustomerName
        """
        return execute_query(query)

def get_average_product_price_by_category():
        query = """
        select Category, avg(Price) AvgPrice
        from Products
        group by Category
        """
        return execute_query(query)

def get_order_details(order_id):
        query = """
        select OrderDetails.ProductID, Products.ProductName, OrderDetails.Quantity, OrderDetails.Subtotal
        from OrderDetails
        join Products on OrderDetails.ProductID = Products.ProductID
        where OrderDetails.OrderID = {}
        """.format(order_id)
        return execute_query(query)

def get_products_in_category(category):
        query = """
        select ProductName, Price
        from Products
        where Category = '{}'
        """.format(category)
        return execute_query(query)

def get_customers_with_highest_spending():
        query = """
        select concat(FirstName, ' ', LastName) CustomerName, sum(TotalAmount) TotalSpent
        from Customers
        join Orders on Customers.CustomerID = Orders.CustomerID
        group by CustomerName
        order by TotalSpent desc
        limit 5
        """
        return execute_query(query)

def get_orders_by_date_and_category(date, category):
        query = """
        select Products.ProductName, Orders.OrderDate, OrderDetails.Quantity, OrderDetails.Subtotal
        from Orders
        join OrderDetails on Orders.OrderID = OrderDetails.OrderID
        join Products on OrderDetails.ProductID = Products.ProductID
        where Orders.OrderDate = '{}' and Products.Category = '{}'
        """.format(date, category)
        return execute_query(query)

def get_total_revenue_by_product():
        query = """
        select Products.ProductName, sum(OrderDetails.Subtotal) TotalRevenue
        from Products
        join OrderDetails on Products.ProductID = OrderDetails.ProductID
        group by Products.ProductName
        order by TotalRevenue desc
        limit 5
        """
        return execute_query(query)
