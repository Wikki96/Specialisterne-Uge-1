import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

con = mysql.connector.connect(user="root", database="northwind", password="250303")
df = pd.read_sql("SELECT * FROM orders AS o JOIN orderdetails AS od ON o.orderID = od.orderID", con)
df['TotalSales'] = df.UnitPrice * df.Quantity
groupedData = df.groupby("ShipCountry")
pricePerCountry = groupedData.sum("TotalSales")["TotalSales"]
pricePerCountry.plot(kind= "bar", subplots=True)
plt.tight_layout()
plt.show()