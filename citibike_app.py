### Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime as dt
import os 
import glob

citibike201709=pd.read_csv("201709-citibike-tripdata.csv")
citibike201709jc=pd.read_csv("jc-201709-citibike-tripdata.csv")




#### Read CitiBike Data ####

path ="/Users/junge011/Documents/Data_Analytics_Bootcamp/USCLOS201807DATA5/20-Tableau/Homework/CitiBike"
allFiles = glob.glob(path + "/*-citibike-tripdata.csv")
item_level_df = pd.DataFrame()
list01 = []
for file_ in allFiles:
    df01 = pd.read_csv(file_, header=0)
    list01.append(df01)
item_level_df = pd.concat(list01)
citibike_201709_201809=item_level_df

# Export as CSV File
citibike_201709_201809.to_csv("citibike_201709_201809.csv", index=False, header=True)

tail=citibike_201709_201809.tail()
tail