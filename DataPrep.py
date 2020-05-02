import pandas as pd
import numpy as np

# loading data and creating data frame from csv
data=pd.read_csv('energy.csv', na_values=" ")

# we are giving the name country to the 1st column
data.rename(columns={"Unnamed: 0": "country"}, inplace=True) 

# filling the missing values with the mean energy production for that country
data.fillna(data.mean(), inplace=True)

# remove the data for the aggregate values (EU27, OECD, World)
data.drop(data.index[[34, 35, 42]], inplace=True)

# we are making country column  as index of the column continent that we will create
data.set_index("country", inplace=True)
countries = {
    'Australia': 'Australia',
    'Austria': 'Europe',
    'Belgium': 'Europe',
    'Canada': 'North America',
    'Chile': 'South America',
    'CzechRepublic': 'Europe',
    'Denmark': 'Europe',
    'Estonia': 'Europe',
    'Finland': 'Europe',
    'France': 'Europe',
    'Germany': 'Europe',
    'Greece': 'Europe',
    'Hungary': 'Europe',
    'Iceland': 'Europe',
    'Ireland': 'Europe',
    'Israel': 'Asia',
    'Italy': 'Europe',
    'Japan': 'Asia',
    'Korea': 'Asia',
    'Luxembourg': 'Europe',
    'Mexico': 'North America',
    'Netherlands': 'Europe',
    'NewZealand': 'Oceania',
    'Norway': 'Europe',
    'Poland': 'Europe',
    'Portugal': 'Europe',
    'SlovakRepublic': 'Europe',
    'Slovenia': 'Europe',
    'Spain': 'Europe',
    'Sweden': 'Europe',
    'Switzerland': 'Europe',
    'Turkey': 'Asia',
    'UnitedKingdom': 'Europe',
    'UnitedStates': 'North America',
    'Brazil': 'South America',
    'China': 'Asia',
    'India': 'Asia',
    'Indonesia': 'Asia',
    'RussianFederation': 'Europe',
    'SouthAfrica': 'Africa'}
data["Continent"] =  pd.Series(countries)

data.reset_index(level=0,inplace=True) 

# we are making Continent column  as index
data.set_index("Continent",inplace=True)

# we are computing the mean
data['mean'] = data.mean(axis=1)

'''we are creating a data frame that contains num_countries,
mean, small_production, avg_production and large_production as columns'''
df = data[["country", "mean"]]
df.rename(columns={"country": "num_countries"}, inplace=True)
dataframe = df.groupby(level=0, axis=0).count()

dataframe["mean"] = df.groupby(level=0)["mean"].mean()
totalmean = dataframe["mean"].mean()

dataframe["small_production"] = np.where(dataframe['mean'] < (totalmean -dataframe["mean"].std()), 1, 0)
df.groupby(level=0)

dataframe["avg_production"] = np.where(dataframe['mean'] > (totalmean - dataframe["mean"].std()), 1, 0)
df.groupby(level=0)

dataframe["large_production"] = np.where(dataframe['mean'] > (totalmean + dataframe["mean"].std()), 1, 0)
df.groupby(level=0)

print(dataframe)