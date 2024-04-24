import csv
import os
import numpy as np
import pandas as pd

def make_df(path): # Reads the csv file in and makes it a DataFrame
    df = pd.read_csv(path)
    return df

path = os.path.realpath(__file__) 
directory = os.path.dirname(path)
dir_string = str(directory) + "/data/crime_data.csv"

all_data_df = make_df(dir_string)
print(all_data_df.head())

print(list(all_data_df))