## Intro to Simple Data Analysis

import numpy as np
import pandas as pd

### Read data with pandas

data = pd.read_csv('finance_liquor_sales.csv')

print(data.head())

import matplotlib.pyplot as plt

######## Grouping by zip code and summing total bottles sold for each code

da = data.groupby(['zip_code'])['bottles_sold'].sum()
print(da)


import seaborn as sns
sns.set(style="whitegrid")

####### Scatter plot

plt.figure(figsize=(12, 10), dpi=80)
plt.scatter(da.index.to_numpy(), da.to_numpy(),c=np.linspace(0,1, da.shape[0]))
plt.title("Total bottles sold")
plt.xlabel("Item zip code")
plt.ylabel("Total bottles sold")
plt.show()

### Group by store number and summing each store's sale dollars

sps = data.groupby(['store_number'])['sale_dollars'].sum()
print(sps)

total_sales = sps.to_numpy().sum()

percentage_per_store = sps.to_numpy()/total_sales

print(np.around(percentage_per_store*100, 4))

### Create a horizontal bar plot

plt.figure(figsize=(12, 10), dpi=80)
da_pd = pd.Series(percentage_per_store*100,index=sps.index)
data_sorted = da_pd.sort_values()
data_sorted.plot.barh(color='red', alpha=0.6,width=0.7)
plt.xlabel("Percentage of total Sales")
plt.title("Percentage of total Sales per Store")
plt.show()


