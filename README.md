# Tableau-Challenge: NYC CitiBike Data Analysis
<br>
In this challenge, I am visualizing New York City's Citibike data provided by the official CitiBike Website (https://www.citibikenyc.com/system-data). While the official website has the data dating back to Summer of 2013, I have limited the scope of my analysis from the date range of September 2017 through September 2018. <br>

![CitiBike Map](https://github.com/erikku0519/Tableau-Challenge/blob/master/Citibike.png)


## Data Pre-Processing<br>
<br>
# Data Download<br>
The website has CitiBike raw data available for the public to download. Each file repesent the Bike trip data by each month in each Manhattan or Jersey City (JC) region. 

# Data Loading & Merging<br>
There are total of 26 different raw data files (13 months * 2 areas) and each raw data may exceed 300MB in size. To make the data process smoother, I decided to automate the data loading and merging process by writing Python scripts:
<br>
`citibike_app.py`is responsible for automation of loading csv files and merging the data utilizing Python's Pandas. Upon merging the data, I exported the data as csv file.

# Import to Tableau<br>
I imported the csv file of the merged data
<br>
`citibike_app.py`is responsible for automation of loading csv files and merging the data utilizing Python's Pandas. 
<br>
## Insights from the Data<br>
Answers to below questions are answered on the Tableau Story (PDF File also attached):
<br>
* How many trips have been recorded total during the chosen period?
* By what percentage has total ridership grown?
* How has the proportion of short-term customers and annual subscribers changed?
* What are the peak hours in which bikes are used during summer months?
* What are the peak hours in which bikes are used during winter months?
* Today, what are the top 10 stations in the city for starting a journey? (Based on data, why do you hypothesize these are the top locations?)
* Today, what are the top 10 stations in the city for ending a journey? (Based on data, why?)
* Today, what are the bottom 10 stations in the city for starting a journey? (Based on data, why?)
* Today, what are the bottom 10 stations in the city for ending a journey (Based on data, why?)
* Today, what is the gender breakdown of active participants (Male v. Female)?
* How effective has gender outreach been in increasing female ridership over the timespan?
* How does the average trip duration change by age?
* What is the average distance in miles that a bike is ridden?
* Which bikes (by ID) are most likely due for repair or inspection in the timespan?
* A static map that plots all bike stations with a visual indication of the most popular locations to start and end a journey with zip code data overlaid on top.
* A dynamic map that shows how each station's popularity changes over time (by month and year) -- with commentary pointing to any interesting events that may be behind these phenomena.
* Two unexpected phenomena in the data and provide a visualization and analysis to document their presence.

