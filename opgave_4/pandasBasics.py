import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_csv(os.path.join("opgave_4","DKHousingPricesSample100k.csv"))
print(data.head(10))
dataByRegion = data.groupby("region")
averagePurchasePriceByRegion = dataByRegion.mean("purchase_price")["purchase_price"]
print(averagePurchasePriceByRegion)
dataByHouseTypeAndRegion = data.groupby(["house_type", "region"])
plotData = dataByHouseTypeAndRegion.mean("purchase_price")["purchase_price"]
plotData = plotData.unstack()
plotData.plot(kind= "bar")
plotData.plot(kind= "bar", subplots=True, layout=(2,2))
plt.show()
