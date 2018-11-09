# Tableau-Challenge: NYC CitiBike Data Analysis
<br>
In this challenge, I am visualizing New York City's Citibike data provided by the official CitiBike Website (https://www.citibikenyc.com/system-data). While the official website has the data dating back to Summer of 2013, I have limited the scope of my analysis from the date range of September 2017 through September 2018. <br>

![CitiBike Map](https://github.com/erikku0519/Tableau-Challenge/blob/master/Citibike.png)


## Data Download & Merge<br>
<br>
The website has CitiBike raw data available for the public to download. Each file repesent the Bike trip data by each month in each Manhattan or Jersey City (JC) region. As a result, there are total of 26 different raw data files (13 months * 2 areas) and each raw data may exceed 300MB in size. To make the data process smoother, I decided to automate the data loading and merging process by writing Python scripts:
<br>
`citibike_app.py`is responsible for automation of loading csv files and merging the data utilizing Python's Pandas. 

## Getting the Data<br>

* The USGS provides earthquake data in a number of different formats, updated every 5 minutes. Visit the USGS GeoJSON Feed page and pick a data set to visualize. When you click on a data set, for example 'All Earthquakes from the Past 7 Days', you will be given a JSON representation of that data. You will be using the URL of this JSON to pull in the data for our visualization.

## Import & Visualize the Data<br>

* Set URL for geojson API & GET request to the usgs_URL
* Define a function we want to run once for each feature in the features array, Give each feature a popup with earthquake information (magnitude, place, and time), Create a GeoJSON layer containing the features array on the earthquakeData object, Run the onEachFeature function once for each piece of data in the array, CreateMap function with Earthquake layer.
* Create a baseMaps object of satellite, Grayscale (light), Outdoors, and Comic
* Define a layer for the plate tectonics
* Create overlay object for earthquake and plate techtonics
* Set the default view of map as satellite, earthquakes and tectonic plates layers toggled on
* Add Fault lines data
* Add the layer control to the map
* Create Color and Radius Function

