import pandas as pd
import numpy as np
# a library that I do not own exists here. 

#data is stored named london_data
#print(london_data.head())
#print(london_data.dtypes)

#printing some specific rows
#print(london_data.iloc[100:200])

#checking the length of the dataframe
#print(len(london_data))

#saving the column 'TemperatureC' as a series
temp = london_data['TemperatureC']

#checking on the column
#print(temp.head())

#get average temp of the series
average_temp = np.average(temp)

#checking
#print(average_temp)

#calculate the temperature varience
temperature_var = np.var(temp)

#checking
#print(temperature_var)

#calculate the std of temperature
temperature_standard_deviation = np.std(temp)

#checking 
#print(temperature_standard_deviation, temperature_var, average_temp)

#checking the databade
#print(london_data.head())
#creating a variable that filters through the month 6 and gets the temperature for that month
june = london_data.loc[london_data['month'] == 6]['TemperatureC']

#checking
#print(june)

#doing the same for month 7
july = london_data.loc[london_data['month'] == 7]['TemperatureC']

#calculating the mean of june and july
print('The mean temperature of the month of June is ' + str(june.mean()))
print('The mean temperature of the month of July is ' + str(july.mean()))

#std of both those series
june_std = np.std(june)
july_std = np.std(july)

print('The Standard Deviation of the data for June is ' + str(june_std))
print('The Standard Deviation of the data for July is ' + str(july_std))

for i in range(1,13):
  month = london_data.loc[london_data['month'] == i] ['TemperatureC']
  print('The mean of the month ' + str(i) + ' is ' + str(np.average(month)))
  print('The Standard deviation of the month ' + str(i) + ' is ' + str(np.std(month)))
