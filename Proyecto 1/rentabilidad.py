import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Northwind.db")
"""query = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
    ''' # Productas más rentables
top_products = pd.read_sql_query(query, conn) # Hace todo para realizar la consulta
top_products.plot(x = "ProductName", y = "Revenue", kind = "bar", figsize= (10, 5), legend= False)

plt.title("10 Productos más rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation = 90)
plt.show()

query = '''
    SELECT LastName || " " || FirstName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e ON o.EmployeeID = e.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
    LIMIT 10
    ''' # Empleados más eficientes
top_employees = pd.read_sql_query(query,conn)
top_employees.plot(x="Employee", y="Total",kind="bar",figsize=(10,5), legend=False)
plt.title("10 Mejores empleados")
plt.xlabel("Empleados")
plt.ylabel("Total")
plt.xticks(rotation = 45)
plt.show()

query = '''
    SELECT LastName || " " || FirstName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e ON o.EmployeeID = e.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total ASC
    LIMIT 3
    ''' # Empleados más eficientes
button_employees = pd.read_sql_query(query,conn)
button_employees.plot(x="Employee", y="Total",kind="bar",figsize=(10,5), legend=False)
plt.title("3 Peores empleados")
plt.xlabel("Empleados")
plt.ylabel("Total")
plt.xticks(rotation = 45)
plt.show()"""
query = '''
    SELECT LastName || " " || FirstName as Employee, SUM(Quantity) as Vendido
    FROM Orders o
    JOIN Employees e ON o.EmployeeID = e.EmployeeID
    JOIN OrderDetails od ON od.OrderID = o.OrderID
    GROUP BY o.EmployeeID
    ORDER BY Vendido DESC
    LIMIT 10
    ''' # Empleados que más vendieron
top_empl_sales = pd.read_sql_query(query,conn)
top_empl_sales.plot(x="Employee", y="Vendido",kind="bar",figsize=(10,5), legend=False)
plt.title("10 Empleados articulos vendidos")
plt.xlabel("Empleados")
plt.ylabel("Vendido")
plt.xticks(rotation = 45)
plt.show()

query = '''
    SELECT LastName || " " || FirstName as Employee, SUM(Price*Quantity) as Dinero
    FROM Orders o
    JOIN Employees e ON o.EmployeeID = e.EmployeeID
    JOIN OrderDetails od ON od.OrderID = o.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    GROUP BY o.EmployeeID
    ORDER BY Dinero DESC
    LIMIT 10
    ''' # Empleados que más vendieron
top_empl_sales = pd.read_sql_query(query,conn)
top_empl_sales.plot(x="Employee", y="Dinero",kind="bar",figsize=(10,5), legend=False)
plt.title("10 Empleados más dinero vendido")
plt.xlabel("Empleados")
plt.ylabel("Dinero")
plt.xticks(rotation = 45)
plt.show()