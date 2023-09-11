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
        select P.Category,
        sum(OD.Quantity * P.Price) TotalSalesAmount
        from Products P
        join OrderDetails OD on P.ProductID = OD.ProductID
        group by P.Category
    """)
    return lst
    
def percent_total_sales_cat():
    lst = execute_query("""
        select P.Category,
        sum(OD.Quantity * P.Price) / (select sum(Quantity * Price) from OrderDetails) * 100 Percentage
        FROM Products P
        JOIN OrderDetails OD on P.ProductID = OD.ProductID
        group by P.Category
    """)
    return lst

def total_sales_date():
    lst = execute_query("""
        SELECT Orderdate,
        sum(TotalAmount) TotalSalesAmount
        from Orders
        group by Orderdate
    """)
    return lst

def prod_qty():
    lst = execute_query("""
        select P.ProductName,
        sum(OD.Quantity) TotalQuantitySold
        from Products P
        join OrderDetails OD on P.ProductID = OD.ProductID
        group by P.ProductName
        order by TotalQuantitySold desc
    """)
    return lst
