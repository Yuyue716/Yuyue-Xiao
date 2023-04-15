import pandas as pd
from pandas import DataFrame
import numpy as np  
import sqlalchemy
import sqlite3
import copy
import matplotlib.pyplot as plt

# read data
df_climate=pd.read_csv(r'static\climate_action.csv',encoding='gbk',low_memory=False)

#dropping non useful column and reset index
newdf = df_climate.loc[:,['Entity','Code','Year','Value']]
new_newdf=newdf.reset_index(drop=True)

#dropping non num values and make value int
new_newdf = new_newdf[[row.isnumeric() for row in new_newdf['Year']]]
new_newdf['Year'] = [int(row) for row in new_newdf['Year']]

# filling NAs
new_index=set(np.arange (1961,2020,1))

for country in list(set(new_newdf['Entity'])):
    country_years = set(new_newdf[new_newdf['Entity'] == country]['Year'])
    years_to_add = new_index - country_years
    for year in list(years_to_add):

        cou=new_newdf[new_newdf['Entity'] == country]['Code'].unique()
        new_data = pd.DataFrame({'Entity': country, 'Year': [year] ,'Code':cou,'Value': np.nan})
        new_newdf = pd.concat([new_newdf,new_data])

# Refilling NAs
new_newdf['Value']=new_newdf['Value'].interpolate()

# Store new data
new_newdf.to_csv('co-emission-per-capita.csv')

