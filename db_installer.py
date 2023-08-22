import mysql.connector
import os
import time
connection = None

user = str(input("Enter SQL Server Username : "))
password = str(input("Enter SQL Server Password : "))
host = str(input("Enter SQL Server Hostname : "))
creds = [user + ",", password+",", host]
with open("creds.tiak","w") as f:
    pass
with open("creds.tiak", "a") as f:
    for i in creds:
        f.write(i)
        
print("Setting Up")
time.sleep(2)

# Replace these with your actual database connection details
db_config = {
    'user': user,
    'password': password,
    'host': host,
}

# SQL statements to be executed
sql_commands = """
create database if not exists DataSense;
use DataSense;

create table if not exists Users (
    Username varchar(10),
    Password varchar(255)
);

create table if not exists Products (
    ProductID int primary key,
    ProductName varchar(255),
    Category varchar(50),
    Price decimal(10, 2)
);
insert into Products (ProductID, ProductName, Category, Price)
values
    (1, 'Laptop', 'Electronics', 899.99),
    (2, 'Smartphone', 'Electronics', 599.99),
    (3, 'Headphones', 'Electronics', 99.99),
    (4, 'Coffee Maker', 'Appliances', 49.99),
    (5, 'Blender', 'Appliances', 39.99),
    (6, 'Running Shoes', 'Clothing', 79.99),
    (7, 'Jeans', 'Clothing', 49.99),
    (8, 'Desk Chair', 'Furniture', 149.99),
    (9, 'Bookshelf', 'Furniture', 89.99),
    (10, 'Garden Tools Set', 'Gardening', 29.99);

create table if not exists Customers (
    CustomerID int primary key,
    FirstName varchar(50),
    LastName varchar(50),
    Email varchar(100),
    Address varchar(255)
);
insert into Customers (CustomerID, FirstName, LastName, Email, Address)
values
    (1, 'John', 'Doe', 'johndoe@email.com', '123 Main St, Anytown, USA'),
    (2, 'Jane', 'Smith', 'janesmith@email.com', '456 Elm St, Othertown, USA'),
    (3, 'Alice', 'Johnson', 'alicejohnson@email.com', '789 Oak St, Anycity, USA'),
    (4, 'Bob', 'Wilson', 'bobwilson@email.com', '101 Pine St, Sometown, USA'),
    (5, 'Eva', 'Brown', 'evabrown@email.com', '555 Cedar St, Yourtown, USA'),
    (6, 'Michael', 'Johnson', 'michael@email.com', '222 Birch St, Yetanothertown, USA'),
    (7, 'Sarah', 'Wilson', 'sarah@email.com', '303 Maple St, Anycity, USA'),
    (8, 'David', 'Brown', 'david@email.com', '444 Pine St, Sometown, USA'),
    (9, 'Olivia', 'Garcia', 'olivia@email.com', '777 Cedar St, Yourtown, USA'),
    (10, 'Daniel', 'Martinez', 'daniel@email.com', '999 Oak St, Overtherainbow, USA');

create table if not exists Orders (
    OrderID int primary key,
    CustomerID int,
    Orderdate date,
    TotalAmount decimal(10, 2),
    foreign key (CustomerID) references Customers(CustomerID)
);
insert into Orders (OrderID, CustomerID, Orderdate, TotalAmount)
values
    (1, 1, '2023-08-01', 899.99),
    (2, 2, '2023-08-02', 149.98),
    (3, 3, '2023-08-03', 349.97),
    (4, 1, '2023-08-04', 99.99),
    (5, 4, '2023-08-05', 79.99),
    (6, 3, '2023-08-06', 299.97),
    (7, 6, '2023-08-07', 179.97),
    (8, 8, '2023-08-08', 49.99),
    (9, 5, '2023-08-09', 299.97),
    (10, 9, '2023-08-10', 59.98);

create table if not exists OrderDetails (
    OrderDetailID int primary key,
    OrderID int,
    ProductID int,
    Quantity int,
    Subtotal decimal(10, 2),
    foreign key (OrderID) references Orders(OrderID),
    foreign key (ProductID) references Products(ProductID)
);
insert into OrderDetails (OrderDetailID, OrderID, ProductID, Quantity, Subtotal)
values
    (1, 1, 1, 1, 899.99),
    (2, 2, 8, 2, 299.98),
    (3, 3, 6, 3, 239.97),
    (4, 4, 3, 1, 99.99),
    (5, 5, 7, 1, 49.99),
    (6, 6, 2, 1, 599.99),
    (7, 7, 5, 2, 79.98),
    (8, 8, 10, 1, 29.99),
    (9, 9, 1, 2, 1799.98),
    (10, 10, 4, 1, 49.99);
"""

# Split the SQL commands by semicolon
sql_commands = sql_commands.split(';')

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    for command in sql_commands:
        command = command.strip()
        if command:
            cursor.execute(command)
            connection.commit()

    print("Database established successfully!!!")
    time.sleep(2)
        
except mysql.connector.Error as err:
    os.system("pip install mysql-connector-python --upgrade")
    print("please restart")

finally:
    print("Setup Complete")
    time.sleep(3)
    if connection:
        connection.close()
