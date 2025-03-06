import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

print("Enter Mysql user")
user = input()
print("Enter database name")
db = input()
print("Enter password")
password = input()

con = mysql.connector.connect(user=user, database=db, password=password)
orders = pd.read_sql("SELECT * FROM orders AS o JOIN orderdetails AS od ON o.orderID = od.orderID", con)
orders['TotalSales'] = orders.UnitPrice * orders.Quantity
dataByCountry = orders.groupby("ShipCountry")
salesPerCountry = dataByCountry.sum("TotalSales")["TotalSales"]
salesPerCountry.plot(kind= "bar", title="World")
plt.tight_layout()

fig, axes = plt.subplots(nrows=2, ncols=2, sharey="row")
salesPerCompany = orders.groupby(["ShipCountry", "CustomerID"]).sum("TotalSales")["TotalSales"]
salesPerCompany.loc["Germany"].plot(kind= "bar", ax=axes[1,0], title="Germany")
salesPerCompany.loc["USA"].plot(kind="bar", ax=axes[1,1], title="USA")

dataByCountryOverTime = orders.groupby(["ShipCountry", pd.Grouper(key="OrderDate", freq="3M")])
salesByCountryOverTime = dataByCountryOverTime.sum("TotalSales")["TotalSales"]
salesByCountryOverTime.loc["Germany"].plot(ax=axes[0,0], title="Germany")
salesByCountryOverTime.loc["USA"].plot(ax=axes[0,1], title="USA")


plt.tight_layout()
plt.show()