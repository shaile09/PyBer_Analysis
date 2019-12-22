# %%
# Add Matplotlib inline magic command
%matplotlib inline
# Add all dependecies to data 
import matplotlib.pyplot as plt
import pandas as pd
# Import NumPy and the stats module from SciPy.
import numpy as np
import scipy.stats as sts

# %%
# Files to load from the csv files (city_date and ride_data)
city_data_to_load = "Resources/city_data.csv"
ride_data_to_load = "Resources/ride_data.csv"

# %%
# Read the city data file and store it in a pandas DataFrame.
city_data_df = pd.read_csv(city_data_to_load)
city_data_df.head(10)

# %%
# Read the ride data file and store it in a pandas DataFrame.
ride_data_df = pd.read_csv(ride_data_to_load)
ride_data_df.head(10)

# %%
# Get the columns and the rows that are not null.
city_data_df.count()

# %%
# Get the columns and the rows that are not null.
city_data_df.isnull().sum()

# %%
# Get the data types of each column.
city_data_df.dtypes

# %%
# Get the unique values of the type of city.
city_data_df["type"].unique()

# %%
# Get the number of data points from the Urban cities.
sum(city_data_df["type"]=="Urban")

# %%
# Get the number of data points from the Suburban cities.
sum(city_data_df["type"]=="Suburban")

# %%
sum(city_data_df["type"]=="Rural")

# %%
# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the DataFrame
pyber_data_df.head()

# %%
# Create all the types of cities DataFrames.
urban_cities_df = pyber_data_df[pyber_data_df["type"] == "Urban"]
suburban_cities_df = pyber_data_df[pyber_data_df["type"] == "Suburban"]
rural_cities_df = pyber_data_df[pyber_data_df["type"] == "Rural"]

# %%
# Get the total number of rides for each type of city.
type_of_city_ride_count =pyber_data_df.groupby(["type"]).count()["ride_id"]
type_of_city_ride_count

# %%
# Get the total number of drivers for each type of city.
type_of_city_driver_total = city_data_df.groupby(["type"])["driver_count"].sum()
type_of_city_driver_total

# %%
# Get the total fares for each type of city.
type_of_city_fare_total = pyber_data_df.groupby(["type"]).sum()["fare"]
type_of_city_fare_total

# %%
# Calculate the average fare per ride.
avg_fare_per_ride = pyber_data_df.groupby(["type"]).sum()["fare"] / pyber_data_df.groupby(["type"]).count()["ride_id"]
avg_fare_per_ride

# %%
# Calculate the average fare per driver.
avg_fare_per_driver = pyber_data_df.groupby(["type"]).sum()["fare"] / city_data_df.groupby(["type"])["driver_count"].sum()
avg_fare_per_driver

# %%
# Determine the city type.
per_city_types = pyber_data_df.set_index(["type"])
per_city_types

# %%
# Adding a list of values with keys to create a new DataFrame.
pyber_summary_df = pd.DataFrame({
          "Total Rides": type_of_city_ride_count,
          "Total Drivers": type_of_city_driver_total,
          "Total Fares": type_of_city_fare_total,
          "Average Fare per Ride": avg_fare_per_ride,
          "Average Fare per Driver": avg_fare_per_driver})
# Remove the index name.
pyber_summary_df.index.name = None
pyber_summary_df

# %%
pyber_summary_df.info()

# %%
# Format the pyber summary.
# pyber_summary_df["Total Rides"] = pyber_summary_df["Total Rides"].map("{:,.2f}".format)

pyber_summary_df["Total Fares"] = pyber_summary_df["Total Fares"].map("${:,.2f}".format)

pyber_summary_df["Average Fare per Ride"] = pyber_summary_df["Average Fare per Ride"].map("${:,.2f}".format)

pyber_summary_df["Average Fare per Driver"] = pyber_summary_df["Average Fare per Driver"].map("${:,.2f}".format)

# Display the DataFrame.
pyber_summary_df

# %%
# Challenge Part 2
# Get the index of column names from the merged data file
pyber_data_df.columns

# %%
# Rename the columns in the merged DataFrame
pyber_data_df.rename(columns = {'city':'City', 'date':'Date', 'fare':'Fare', 'ride_id':'Ride Id', 'driver_count':'No Drivers', 'type':'City Type'}, inplace=True)
# List index of new columns
pyber_data_df.head(10)

# %%
# Set the dataframe to the 'Date' column
pyber_data_df.set_index('Date')

# %%
# make a new dataframe by using the copy() method from the merged data
# fares_summary_df = pyber_data_df[['Date', 'Fare', 'City Type']].copy()
# fares_summary_df
# make a new dataframe by using the copy() method from the merged data
fares_summary_df = pyber_data_df[['Date', 'Fare', 'City Type']].copy()
fares_summary_df


#%%
# Set the index to the 'Date' column
fares_summary_df.set_index('Date')

#%%
# Set the index to the datetime data type
fares_summary_df['Date'] = pd.to_datetime(fares_summary_df['Date'])
fares_summary_df.set_index('Date', inplace=True)
fares_summary_df

# %%
# Check the DataFrame using the info() method to make sure the index is a datetime data type.
fares_summary_df.info('Date')

# %%
# Get the total fares for each type of city.
city_total_fare_df = fares_summary_df.groupby(["City Type"]).sum()["Fare"]
city_total_fare_df

# %%
# Reset the index
fares_summary_df.reset_index(drop=True,)

# %%
# Check the DataFrame using the info() method
fares_summary_df.info()

# %%
# Create a pivot table
pyber_pivottable_1 = pd.pivot_table(fares_summary_df, index =['Date'], columns =['City Type'], aggfunc = np.sum)

# %%
# Create new dataFrame from the pivot table DataFrame on the given dates '2019-01-01':'2019-04-28' using loc.
by_date_df = pyber_pivottable_1.loc['2019-01-01':'2019-04-28', :]
by_date_df

# %%
# Create a new DataFrame by setting the DataFrame with resample() in weekly bins, and calculate the sum() of the fares for each week.
weekly_bins_df = by_date_df['Fare'].resample('W').sum()
weekly_bins_df

# %%
from matplotlib.pyplot import style
style.use('fivethirtyeight')
lineplot = weekly_bins_df.plot(figsize=(20,6))
plt.title("Total Fare by City", fontsize=20)
plt.ylabel("Fare ($)", fontsize=12)
plt.xlabel("Month", fontsize=12)
# plt.savefig("analysis/fig.png")

# %%
