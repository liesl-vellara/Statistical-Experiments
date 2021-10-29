import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")

#checking the first five rows of the data
#print(data.head())

#checking on the columns of the data
#print(data.columns)
# 1. country
# 2. life expectancy
# 3. GDP

#checking on the datatypes 
#print(data.dtypes)
# 1. country : object
# 2. life expectancy :float64
# 3. GDP: float64

#checking on the description of the data
#print(data.describe())

#life expectancy to a array of its own
life_expectancy = data['Life Expectancy']

#checking on the the series
#print(life_expectancy.head())

#finding the quartiles of the life_expectancy
life_expectancy_quartile = np.quantile(life_expectancy, [0.25, 0.5, 0.75])

#checking on the list
#print(life_expectancy_quartile)

#ploting a histogram
#plt.hist(life_expectancy, range = (45, 83), bins=38, edgecolor = 'black')

#showing the histogram
#plt.show()

#checking the least and highest value
max_value = np.amax(life_expectancy)
min_value = np.amin(life_expectancy)

#checking
#print(max_value, min_value)

#isolating the gdp column
gdp = data['GDP']

#checking
#print(gdp.head())

#finding the gdp's median
median_gdp = np.median(gdp)

#checking
#print(median_gdp)

#getting all the gdp less than the median
low_gdp = data[data['GDP'] <= median_gdp]

#checking
#print(low_gdp.head())

#all the gdp that is more than the median
high_gdp = data[data['GDP'] > median_gdp]

#checking
#print(high_gdp.head())

#finding the quartiles of each group
low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'], [0.25, 0.5, 0.75])

high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'], [0.25, 0.5, 0.75])

#checking
#print(high_gdp_quartiles, low_gdp_quartiles)

#having graphs
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()
