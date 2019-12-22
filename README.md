# PyBer_Analysis

The goal of this week’s challenge is to use Matplotlib to create visualizations if rideshare data for PyBer to help improve access to ride -sharing services and determine affordability for the underserved neighborhoods. To explore this data, we started with a line charts, bar charts, pie charts, and scatter plots. In addition, we ensured there was no missing, malformed, or incorrect data in the dataset that could lead to poor or incorrect analysis. Once checks were completed, we merged the ride data with the city data, created DataFrames for each type of city (urban, rural, suburban), and using the groupby(), we were able to determine the number of riders for each city. Lastly, we created bubble charts to convey the results of our findings. 
To determine the relevancy of the data, we preformed statistical analytics for the riders of each city. To ensure there are no outliers we used a Box-and-Whisker Plots to visualize the summary statistics (image below).

To get the percentage of each city (including ride percentages), we used a pie chart. To calculate the percentage of drivers for each city, we displayed it in a pie chart.

# Challenge 5
The goal is to create an overall snapshot of the ride- sharing data. In addition to the scatter and pie charts we have created, our client would like to see a summary table of key metrics of the ride sharing data by city type, and a multiple-line graph that shows the average fare for each week by each city. To complete this, we used pandas to complete the following objectives:
-	Use groupby, pivot, resample, and reset index on a Dataframe
-	Use methods and attributes on a Datafarme or Series 
-	Create a new DataFrame from multiple groupby() series 
-	Format columns of a DataFrame, create a multiple-line graph, and annotate/apply styling to the chart 
In part one, we created a summary data frame that shows the total riders, drivers, and total fare, average fare per ride, and fare per driver. [See table below]
The table shows that there are more riders in the urban areas (1,625 total riders), 625 total riders in suburban areas, and 125 in rural areas. The total average riders is also the similar with urban areas having the most drivers and rural areas having the least. Similarly, the total fares are higher in the urban areas when compared to the suburban and rural areas. The average fare per rider and driver are lower in urban cities when compared  to the suburban and rural.  

For part two of this challenges, we created a multiple-line plot for the sum of the fares for each city type. The graph below shows the total fare for each city (rural, suburban and urban).

