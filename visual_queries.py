from sql_scripts import *

def product_categories():
    lst = execute_query("select distinct(Category) from Products")
    for i in range(len(lst)):
        lst[i] = lst[i][0]
    return lst

def order_dates():
    lst = execute_query("select distinct(Orderdate) from Orders")
    for i in range(len(lst)):
        lst[i] = lst[i][0]
    return lst

def products():
    lst = execute_query("select productname from products")
    for i in range(len(lst)):
        lst[i] = lst[i][0]
    return lst

def prod_price():
    lst = execute_query("select price from products")
    for i in range(len(lst)):
        lst[i] = lst[i][0]
    return lst

def customers():
    lst = execute_query("select concat(FirstName, ' ', LastName) CustomerName from Customers")
    for i in range(len(lst)):
        lst[i] = lst[i][0]
    return lst

##########################################################################
def total_sales_cat():
    lst = execute_query("""
        SELECT P.Category,
        SUM(OD.Quantity * P.Price) TotalSalesAmount
        FROM Products P
        JOIN OrderDetails OD ON P.ProductID = OD.ProductID
        GROUP BY P.Category
    """)
    return lst
    
def percent_total_sales_cat():
    lst = execute_query("""
        SELECT
            P.Category,
            SUM(OD.Quantity * P.Price) / (SELECT SUM(Quantity * Price) FROM OrderDetails) * 100 AS Percentage
        FROM
            Products P
        JOIN
            OrderDetails OD ON P.ProductID = OD.ProductID
        GROUP BY
            P.Category
    """)
    return lst

def total_sales_date():
    lst = execute_query("""
        SELECT
            Orderdate,
            SUM(TotalAmount) AS TotalSalesAmount
        FROM
            Orders
        GROUP BY
            Orderdate
    """)
    return lst

def prod_qty():
    lst = execute_query("""
        SELECT
            P.ProductName,
            SUM(OD.Quantity) AS TotalQuantitySold
        FROM
            Products P
        JOIN
            OrderDetails OD ON P.ProductID = OD.ProductID
        GROUP BY
            P.ProductName
        ORDER BY
            TotalQuantitySold DESC
    """)
    return lst
