import pandas as pd
import os 

dir = 'data'
sub_dir = 'raw'
filename = 'ward_population.csv'

file_path =os.path.join(dir, sub_dir, filename)

pop = pd.read_csv(file_path)

## Data overview : shows the first 5 rows of the data
print(pop.head())

## Data shape i.e count of rows and columns
print( pop.shape)

## Columns information
print('Columns:', list(pop.columns));

print('Data types:', pop.dtypes)

## Summary statistics for the 2024 population column
print(pop['population_2024'].describe())

