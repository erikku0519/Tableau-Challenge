# Geo-Mapping-Challenge: Visualizing Data with Leaflet
<br>
In this challenge, I am visualizing earthquake data provided by the USGB (United States Geological Survey), which is responsible for providing scientific data about natural hazards, the health of our ecosystems and environment, and the impacts of climate and land-use change.<br>

## Required Files<br>
* `index.html`<br>
* `logic.js`<br>
* `config.js`<br>
* `style.css`<br>
<br>
Note: `config.js`is excluded on GitHub as it contains API Key.<br>

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

