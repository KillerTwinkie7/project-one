import csv
import os
import numpy as np
import pandas as pd

def make_df(path): # Reads the csv file in and makes it a DataFrame
    df = pd.read_csv(path)
    return df

path = os.path.realpath(__file__)                       #| This is here just so we can avoid 
directory = os.path.dirname(path)                       #| file directory headaches
dir_string = str(directory) + "/data/crime_data.csv"    #| in the future.

all_data_df = make_df(dir_string) # Create the dataframe containing all of the data in our data set.

# print(list(all_data_df)) # Uncomment this out to see all of the categories from the main dataset (the column titles)

date_crime = pd.concat([all_data_df['Occurred Date'], all_data_df['Highest Offense Description']], axis=1) # Create a new dataframe that just has crimes and dates

# print(date_crime.sort_values(by=['Highest Offense Description'])) # Uncomment this out to see every type of crime accounted for in our data frame.

crimes = date_crime['Highest Offense Description'].unique() # This populates a list containing the different types of crimes
#print(crimes) # Uncomment this out to view the different types of crimes accounted for in the data set.

filtered_theft_crime = date_crime[date_crime['Highest Offense Description'].str.contains('theft', case=False)]      #| These two lines create two new lists containing all crimes that include
filtered_burgl_crime = date_crime[date_crime['Highest Offense Description'].str.contains('burglary', case=False)]   #| either the word 'theft' or 'burglary' to create a new dataframe

all_theft_crimes = pd.concat([filtered_theft_crime, filtered_burgl_crime], ignore_index=True) # Create the new dataframe that consists of only crimes pertaining to theft or burglaries

all_theft_crimes['Occurred Date'] = pd.to_datetime(all_theft_crimes['Occurred Date'], format='mixed') # Converts each date in the 'Occurred Date' into a more usable format.

all_theft_crimes['Season'] = pd.cut(                            #| Initialize binning     
    all_theft_crimes['Occurred Date'].dt.dayofyear,             #| Return a number for the date for easier binning
    bins= [0, 79, 171, 264, 355, 365],                          #| Range of seasons by days in each one
    labels=['Winter', 'Spring', 'Summer', 'Fall', 'Winter'],    #| Labels for each season. Winter is repeated because it loops back around into new year.     
    ordered=False                                               #| We have duplicate labels, so this is required lest an error occur
    )

season_theft_crimes = all_theft_crimes.drop(columns=['Occurred Date']) # Creates another new dataframe that only includes the season and the crime.

'''
At this point, we're left with a couple useful dataframes- all_theft_crimes and season_theft_crimes. If you find yourself
needing the specific dates in your analysis, then use all_theft_crimes, but if you just need the seasons, use
season_theft_crimes.

From here, there's a few things we need to do. We need to visualize the data, run statistical analysis, and... some
other third thing probably. I think we're largely almost done though!
'''