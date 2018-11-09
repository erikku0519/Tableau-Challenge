# Tableau-Challenge: NYC CitiBike Data Analysis
<br>
In this challenge, I am visualizing New York City's Citibike data provided by the official CitiBike Website (https://www.citibikenyc.com/system-data). While the official website has the data dating back to Summer of 2013, I have limited the scope of my analysis from the date range of September 2017 through September 2018. <br>

![CitiBike Map](https://github.com/erikku0519/Tableau-Challenge/blob/master/Citibike.png)


## Data Download & Merge<br>
<br>
The website has CitiBike raw data available for the public to download. Each file repesent the Bike trip data by each month in each Manhattan or Jersey City (JC) region. As a result, there are total of 26 different raw data files (13 months * 2 areas) and each raw data may exceed 300MB in size. To make the data process smoother, I decided to automate the data loading and merging process by writing Python scripts:
<br>
`citibike_app.py`is responsible for automation of loading csv files and merging the data utilizing Python's Pandas. 

## Insights from the Data<br>
* How Many Trips Have been Recorded?<br>
* How has total ridership grown in the past year?<br>
